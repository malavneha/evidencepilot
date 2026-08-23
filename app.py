from fastapi import FastAPI
from pydantic import BaseModel

from agent import EvidencePilot


app = FastAPI(
    title="EvidencePilot",
    description="Autonomous AI research agent for evidence-focused clinical research.",
    version="0.1.0",
)

pilot = EvidencePilot()


class ResearchRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "name": "EvidencePilot",
        "status": "ready",
        "message": "Submit a clinical research question to begin."
    }


@app.post("/research")
def research(request: ResearchRequest):
    return pilot.run(request.question)