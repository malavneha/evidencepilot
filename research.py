"""
EvidencePilot research orchestration.

Coordinates the major stages of the evidence-focused research workflow.
"""

from dataclasses import dataclass
from typing import List

from evidence import EvidenceItem, EvidenceRetriever


@dataclass
class ResearchPlan:
    """Structured plan generated from a research question."""

    question: str
    objectives: List[str]


@dataclass
class ResearchResult:
    """Final result returned by the research pipeline."""

    question: str
    plan: ResearchPlan
    evidence: List[EvidenceItem]
    evidence_gaps: List[str]


class ResearchPipeline:
    """Coordinates evidence retrieval and research analysis."""

    def __init__(self):
        self.retriever = EvidenceRetriever()

    def create_plan(self, question: str) -> ResearchPlan:
        """Create a simple structured research plan."""

        question = question.strip()

        return ResearchPlan(
            question=question,
            objectives=[
                "Identify relevant clinical evidence.",
                "Assess the type and relevance of available evidence.",
                "Identify important evidence gaps and uncertainties.",
            ],
        )

    def retrieve_evidence(
        self,
        question: str,
    ) -> List[EvidenceItem]:
        """Retrieve evidence for the research question."""

        return self.retriever.search(question)

    def identify_gaps(
        self,
        evidence: List[EvidenceItem],
    ) -> List[str]:
        """Identify potential gaps in the currently available evidence."""

        if not evidence:
            return [
                "No evidence has been retrieved.",
                "Additional source retrieval is required.",
                "The research question cannot yet be supported by retrieved evidence.",
            ]

        return [
            "Review whether important populations are represented.",
            "Check whether important outcomes are adequately studied.",
            "Look for conflicting findings between sources.",
            "Identify limitations in study design or available evidence.",
        ]

    def run(self, question: str) -> ResearchResult:
        """Run the complete research workflow."""

        question = question.strip()

        if not question:
            raise ValueError("Research question cannot be empty.")

        plan = self.create_plan(question)
        evidence = self.retrieve_evidence(question)
        gaps = self.identify_gaps(evidence)

        return ResearchResult(
            question=question,
            plan=plan,
            evidence=evidence,
            evidence_gaps=gaps,
        )