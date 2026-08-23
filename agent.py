"""
EvidencePilot
Autonomous clinical research agent
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ResearchTask:
    question: str
    subtasks: List[str]


class EvidencePilot:
    """
    Coordinates a multi-step research workflow.

    The Gemini/Google ADK implementation will be connected
    once the Google Cloud environment is configured.
    """

    def plan_research(self, question: str) -> ResearchTask:
        """Break a complex research question into smaller tasks."""
        subtasks = [
            "Define the research question and key concepts",
            "Identify relevant evidence",
            "Extract important findings",
            "Evaluate evidence quality and limitations",
            "Identify evidence gaps",
            "Synthesize findings into a research brief",
        ]

        return ResearchTask(
            question=question,
            subtasks=subtasks,
        )

    def run(self, question: str) -> dict:
        """Run the EvidencePilot research workflow."""
        task = self.plan_research(question)

        return {
            "question": task.question,
            "workflow": task.subtasks,
            "status": "planned",
        }


if __name__ == "__main__":
    pilot = EvidencePilot()

    question = (
        "What are the major evidence gaps in current "
        "treatments for a clinical condition?"
    )

    result = pilot.run(question)

    print("EvidencePilot")
    print("=" * 40)
    print(f"Research question: {result['question']}")
    print("\nPlanned workflow:")

    for number, step in enumerate(result["workflow"], start=1):
        print(f"{number}. {step}")