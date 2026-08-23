"""
EvidencePilot
Autonomous AI research agent for evidence-focused clinical research.

The agent is designed to:
1. Understand a complex research question.
2. Plan the investigation.
3. Gather and organize evidence.
4. Evaluate evidence quality and limitations.
5. Identify evidence gaps.
6. Produce a structured research brief.

External evidence retrieval will be connected to Google tools/services
during the Google Cloud deployment phase.
"""

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


MODEL = "gemini-3.6-flash"


def create_research_plan(question: str) -> str:
    """Create a structured research plan for a complex clinical question.

    Use this tool when a user provides a research question that needs
    multiple investigation steps.

    Args:
        question: The clinical or biomedical research question.

    Returns:
        A structured research plan.
    """

    return f"""
RESEARCH QUESTION
{question}

RESEARCH PLAN

1. Define the research question
   - Identify the population
   - Identify the intervention/exposure
   - Identify the comparator when relevant
   - Identify important outcomes

2. Identify evidence to retrieve
   - Systematic reviews and meta-analyses
   - Randomized or controlled studies
   - Observational evidence when relevant
   - Clinical guidelines or authoritative sources

3. Extract evidence
   - Study population
   - Study design
   - Intervention/exposure
   - Comparator
   - Main outcomes
   - Important limitations

4. Evaluate the evidence
   - Consistency
   - Strength of evidence
   - Potential sources of bias
   - Important uncertainty

5. Identify evidence gaps
   - Missing populations
   - Missing outcomes
   - Conflicting findings
   - Areas with insufficient evidence

6. Synthesize the findings
   - Separate evidence from interpretation
   - Preserve source traceability
   - Clearly communicate uncertainty
"""


def evaluate_research_quality(evidence_summary: str) -> str:
    """Evaluate a collected evidence summary.

    Use this after evidence has been gathered and summarized.

    Args:
        evidence_summary: A summary of the evidence collected during research.

    Returns:
        A structured quality and limitation assessment.
    """

    return f"""
EVIDENCE QUALITY REVIEW

Evidence provided:
{evidence_summary}

Evaluate the evidence using these dimensions:

- Source quality
- Study design
- Sample/population relevance
- Consistency between findings
- Potential bias or confounding
- Strength of conclusions
- Important uncertainty
- Missing information

Do not invent evidence.
Clearly distinguish what is supported by the supplied evidence
from what remains uncertain.
"""


def identify_evidence_gaps(evidence_summary: str) -> str:
    """Identify unanswered questions and evidence gaps.

    Use this after reviewing the available evidence.

    Args:
        evidence_summary: A summary of the evidence collected.

    Returns:
        A structured list of evidence gaps and unanswered questions.
    """

    return f"""
EVIDENCE GAP ANALYSIS

Evidence reviewed:
{evidence_summary}

Identify:

1. Questions that remain unanswered.
2. Populations that may be underrepresented.
3. Outcomes that have insufficient evidence.
4. Conflicting or inconsistent findings.
5. Important methodological limitations.
6. Research questions that could reasonably be investigated next.

Do not manufacture gaps that are not supported by the supplied evidence.
Mark uncertainty explicitly.
"""


root_agent = Agent(
    name="evidence_pilot",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
You are EvidencePilot, an autonomous research assistant designed
to support evidence-focused clinical and biomedical research.

Your job is NOT to replace clinicians or researchers.

For every complex research question:

1. Understand the user's question.
2. Use create_research_plan to break the problem into research tasks.
3. Organize the evidence gathered by the research workflow.
4. Use evaluate_research_quality when evidence has been collected.
5. Use identify_evidence_gaps to identify unanswered questions.
6. Produce a structured research brief.

Your output should contain:

- Research question
- Research approach
- Key evidence
- Evidence quality and limitations
- Conflicting or uncertain findings
- Evidence gaps
- Suggested next research questions

IMPORTANT RULES:

- Never invent citations, studies, statistics, or medical facts.
- Never claim that a source was searched if it was not actually searched.
- Clearly distinguish retrieved evidence from your own synthesis.
- State uncertainty when evidence is incomplete.
- Do not provide individualized medical diagnosis or treatment advice.
- Encourage appropriate expert review for clinical decisions.

The goal is transparent, traceable, useful research assistance.
""",
    tools=[
        create_research_plan,
        evaluate_research_quality,
        identify_evidence_gaps,
    ],
)


app = App(
    root_agent=root_agent,
    name="evidencepilot",
)