"""
Evidence retrieval and source management for EvidencePilot.

This module keeps evidence retrieval separate from the reasoning agent.
That makes source traceability easier to maintain and allows the retrieval
backend to be upgraded without redesigning the research workflow.
"""

from dataclasses import dataclass
from typing import List


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
    Evidence retrieval interface.

    The initial implementation provides a safe structure for evidence.
    The production implementation will connect this interface to the
    approved retrieval/search service during deployment.
    """

    def search(self, query: str) -> List[EvidenceItem]:
        """
        Search for evidence related to a research query.

        Args:
            query: Research query.

        Returns:
            A list of EvidenceItem objects.
        """

        # Retrieval backend will be connected during deployment.
        return []

    def format_for_agent(
        self,
        evidence: List[EvidenceItem],
    ) -> str:
        """Convert retrieved evidence into a traceable agent input."""

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