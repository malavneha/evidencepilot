"""
EvidencePilot research orchestration.

Coordinates the major stages of the evidence-focused research workflow.
"""

from dataclasses import dataclass
from typing import List

from evidence import EvidenceItem, EvidenceRetriever


@dataclass
class ResearchResult:
    question: str
    evidence: List[EvidenceItem]
    evidence_gaps: List[str]


class ResearchPipeline:
    """Coordinates evidence retrieval and research analysis."""

    def __init__(self):
        self.retriever = EvidenceRetriever()

    def retrieve_evidence(self, question: str) -> List[EvidenceItem]:
        """Retrieve evidence for the research question."""
        return self.retriever.search(question)

    def identify_gaps(
        self,
        evidence: List[EvidenceItem],
    ) -> List[str]:
        """Identify potential gaps in the currently available evidence."""

        if not evidence:
            return [
                "No evidence has been retrieved yet.",
                "Additional source retrieval is required.",
            ]

        return [
            "Review whether important populations are represented.",
            "Check whether important outcomes are adequately studied.",
            "Look for conflicting findings between sources.",
            "Identify limitations in study design or available evidence.",
        ]

    def run(self, question: str) -> ResearchResult:
        """Run the research pipeline."""

        evidence = self.retrieve_evidence(question)
        gaps = self.identify_gaps(evidence)

        return ResearchResult(
            question=question,
            evidence=evidence,
            evidence_gaps=gaps,
        )