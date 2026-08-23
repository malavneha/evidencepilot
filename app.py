from fastapi import FastAPI
from pydantic import BaseModel

from research import ResearchPipeline


app = FastAPI(
    title="EvidencePilot",
    description=(
        "Autonomous AI research agent for "
        "evidence-focused clinical research."
    ),
    version="0.2.0",
)

pipeline = ResearchPipeline()


class ResearchRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "name": "EvidencePilot",
        "status": "ready",
        "description": (
            "Autonomous evidence-focused research workflow."
        ),
    }


@app.post("/research")
def research(request: ResearchRequest):
    result = pipeline.run(request.question)

    return {
        "question": result.question,
        "evidence": [
            {
                "title": item.title,
                "source": item.source,
                "url": item.url,
                "summary": item.summary,
                "evidence_type": item.evidence_type,
            }
            for item in result.evidence
        ],
        "evidence_gaps": result.evidence_gaps,
    }