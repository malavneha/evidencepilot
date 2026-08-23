from evidence import EvidenceItem
from research import ResearchPipeline


def test_pipeline_returns_research_result():
    pipeline = ResearchPipeline()

    result = pipeline.run(
        "What are the evidence gaps in a clinical treatment?"
    )

    assert result.question.startswith("What are")
    assert isinstance(result.evidence, list)
    assert isinstance(result.evidence_gaps, list)


def test_evidence_item_structure():
    item = EvidenceItem(
        title="Example study",
        source="Example Journal",
        url="https://example.com",
        summary="Example evidence summary.",
        evidence_type="Research study",
    )

    assert item.title == "Example study"
    assert item.source == "Example Journal"
    assert item.url.startswith("https://")