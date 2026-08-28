"""
Evidence retrieval and source management for EvidencePilot.

Uses PubMed as the initial evidence retrieval backend.
The retrieval layer remains separate from the reasoning agent so that
additional sources can be added later without redesigning the workflow.
"""

from dataclasses import dataclass
from typing import List
from urllib.parse import quote
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


@dataclass
class EvidenceItem:
    """A single piece of retrieved evidence."""

    title: str
    source: str
    url: str
    summary: str
    evidence_type: str


class EvidenceRetriever:
    """
    PubMed evidence retrieval backend.

    PubMed is used as the initial clinical literature source.
    """

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    MAX_RESULTS = 5

    def _request(self, url: str) -> bytes:
        """Make a safe HTTP request to PubMed."""

        request = Request(
            url,
            headers={
                "User-Agent": "EvidencePilot/0.1"
            },
        )

        with urlopen(request, timeout=15) as response:
            return response.read()

    def _search_pubmed(self, query: str) -> List[str]:
        """Find PubMed IDs matching the research question."""

        url = (
            f"{self.BASE_URL}/esearch.fcgi"
            f"?db=pubmed"
            f"&term={quote(query)}"
            f"&retmax={self.MAX_RESULTS}"
            f"&retmode=xml"
            f"&sort=relevance"
        )

        xml_data = self._request(url)
        root = ET.fromstring(xml_data)

        return [
            element.text
            for element in root.findall(".//Id")
            if element.text
        ]

    def _fetch_articles(
        self,
        pubmed_ids: List[str],
    ) -> List[EvidenceItem]:
        """Fetch article metadata and abstracts from PubMed."""

        if not pubmed_ids:
            return []

        ids = ",".join(pubmed_ids)

        url = (
            f"{self.BASE_URL}/efetch.fcgi"
            f"?db=pubmed"
            f"&id={ids}"
            f"&retmode=xml"
        )

        xml_data = self._request(url)
        root = ET.fromstring(xml_data)

        evidence = []

        for article in root.findall(".//PubmedArticle"):
            title_element = article.find(
                ".//ArticleTitle"
            )

            title = (
                "".join(title_element.itertext()).strip()
                if title_element is not None
                else "Untitled article"
            )

            abstract_parts = []

            for abstract_text in article.findall(
                ".//Abstract/AbstractText"
            ):
                text = "".join(abstract_text.itertext()).strip()

                if text:
                    label = abstract_text.attrib.get("Label")

                    if label:
                        abstract_parts.append(
                            f"{label}: {text}"
                        )
                    else:
                        abstract_parts.append(text)

            summary = " ".join(abstract_parts).strip()

            publication_types = [
                "".join(item.itertext()).strip()
                for item in article.findall(
                    ".//PublicationType"
                )
            ]

            evidence_type = (
                ", ".join(publication_types[:3])
                if publication_types
                else "Research article"
            )

            pmid_element = article.find(".//PMID")

            pmid = (
                pmid_element.text
                if pmid_element is not None
                else ""
            )

            if not pmid:
                continue

            evidence.append(
                EvidenceItem(
                    title=title,
                    source="PubMed",
                    url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    summary=summary
                    or "No abstract available.",
                    evidence_type=evidence_type,
                )
            )

        return evidence

    def search(self, query: str) -> List[EvidenceItem]:
        """
        Search PubMed for evidence related to a research question.

        Args:
            query: Clinical research question.

        Returns:
            A list of EvidenceItem objects.
        """

        query = query.strip()

        if not query:
            return []

        try:
            pubmed_ids = self._search_pubmed(query)

            return self._fetch_articles(pubmed_ids)

        except Exception:
            # Retrieval failures should not crash the entire API.
            return []

    def format_for_agent(
        self,
        evidence: List[EvidenceItem],
    ) -> str:
        """Convert retrieved evidence into traceable agent input."""

        if not evidence:
            return "No retrieved evidence is currently available."

        sections = []

        for index, item in enumerate(evidence, start=1):
            sections.append(
                f"""
SOURCE {index}

Title: {item.title}
Source: {item.source}
URL: {item.url}
Evidence type: {item.evidence_type}

Summary:
{item.summary}
""".strip()
            )

        return "\n\n".join(sections)