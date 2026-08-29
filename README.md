# EvidencePilot 🔎

### **An AI-powered evidence research agent that turns complex clinical questions into a structured research workflow.**

EvidencePilot is an AI-powered research workflow designed to help users investigate clinical and biomedical questions using structured evidence retrieval, research planning, and evidence-gap analysis.

Instead of simply generating an answer, EvidencePilot breaks a research question into a structured workflow and produces an evidence-focused research brief.

## 🚀 Live Demo

**API / Interactive Documentation:**
☆
https://evidencepilot-424908950993.asia-south2.run.app/docs

☆https://evidencepilot.onrender.com/docs

**Live Service:**

☆ https://evidencepilot.onrender.com

☆ https://evidencepilot-424908950993.asia-south2.run.app/docs

## 💻 Source Code

https://github.com/malavneha/evidencepilot

## Blog link

https://nehamalavai-builder.blogspot.com/2026/08/building-evidencepilot-evidence.html

## Linkdin post link

https://www.linkedin.com/posts/dr-neha-malav-743a25332_ai-generativeai-gemini-activity-7499047519289745408-Z9lo

## Video demo

https://youtube.com/shorts/gH1DQYhbmCE?si=Cce5WbWS-EXsEdYO

##screenshots
[screenshot][aspirin.jpg]
[screenshot](aspirin..jpg)


## Inspiration

Clinical research can require researchers to move through many sources, extract relevant findings, compare evidence, and identify unanswered questions. For complex questions, this process can become repetitive and difficult to organize.

With a medical background and a growing interest in AI and research, I wanted to explore how an AI agent could help structure this process while keeping evidence and uncertainty visible.

## ✨ What EvidencePilot Does

Given a clinical research question, EvidencePilot:

1. Accepts the research question
2. Creates a structured research plan
3. Identifies relevant clinical evidence
4. Retrieves and structures available evidence
5. Identifies evidence gaps and uncertainties
6. Uses Gemini for evidence-focused reasoning and synthesis
7. Produces a structured research response

### Example Question

> What is the cardiovascular benefit of GLP-1 receptor agonists in adults with type 2 diabetes?

>question": "What are the benefits of aspirin?"

The system generates a research plan and organizes the available evidence and evidence gaps rather than simply returning an unsupported answer.

## 🧠 AI & Google Technologies

- Google GenAI SDK (`google-genai`)
- Gemini
- Google Agent Development Kit
- Google Cloud Run
- FastAPI
- Pydantic
- Python
- Docker

## 📚 Evidence Source

Evidence retrieval is designed around biomedical literature and PubMed/NCBI resources.

The goal is to make research outputs more transparent, structured, and evidence-focused.

## 🏗️ Architecture

```text
Clinical Research Question
          ↓
   Research Planning
          ↓
   Evidence Retrieval
          ↓
 Evidence Structuring
          ↓
    Gap Analysis
          ↓
 Gemini Reasoning & Synthesis
          ↓
   Evidence-Focused Brief

------------------

##☁️ Deployment
Google Cloud Run was used as part of the development and deployment workflow. 
-----------
## Agentic Workflow

EvidencePilot is designed as a workflow rather than a single prompt-response system. Each stage has a specific role:

- **Planner** — breaks the clinical question into research objectives.
- **Retriever** — searches relevant PubMed literature.
- **Evidence Organizer** — structures retrieved evidence.
- **Gap Analyzer** — identifies missing evidence and uncertainties.
- **Synthesis Layer** — prepares the evidence-focused research output.

This separation makes the workflow easier to inspect, reproduce, and extend.
-----------------------------
🧪 Testing

my Testing questn is
{
  "question": "What are the benefits of aspirin?"
}

Open the interactive API documentation:

https://evidencepilot-424908950993.asia-south2.run.app/docs

https://evidencepilot.onrender.com/docs⁠
[screenshot][aspirin.jpg]
[screenshot](aspirin..jpg)

Use the POST /research endpoint with a clinical research question and review the generated research plan, evidence, and evidence gaps.
-------------
🎯 Why EvidencePilot?

Clinical research often requires searching across large amounts of literature, understanding study relevance, and identifying uncertainty.
EvidencePilot aims to make this process more structured by combining:
Autonomous research planning
Evidence retrieval
Evidence-gap identification
Gemini-powered synthesis
A reproducible API workflow
-----------
## How It Works

A user provides a clinical research question. EvidencePilot creates a structured research plan and uses evidence retrieval to identify relevant PubMed literature. The retrieved information is then organized into an evidence-focused response with explicit evidence gaps and uncertainties.

The workflow is designed to help researchers move from an open-ended question toward a more structured research process while keeping evidence and uncertainty visible.
--------
## What I Learned

Building EvidencePilot helped me learn how to combine AI reasoning with external evidence retrieval, structure an agentic research workflow, build an API with FastAPI, containerize an application with Docker, and deploy a working AI application.

The project also taught me an important practical lesson: building an AI agent is not only about the model—it is about designing a reliable workflow around the model, evidence sources, uncertainty, and reproducible execution.

---------------

📌 Hackathon Project
Built for the Google Cloud / Gemini hackathon to demonstrate an evidence-focused autonomous research workflow using Google AI technologies.
Built with Python, FastAPI, Google GenAI SDK, Gemini, and Google Cloud technologies.

-----------------
### Spin-up Instructions

Follow these steps to run EvidencePilot locally.

●Prerequisites

- Python 3.10 or later
- Git
- Google Cloud CLI
- A Google Cloud project
- Google Cloud credentials configured for Vertex AI

1. Clone the repository

git clone https://github.com/malavneha/evidencepilot.git
cd evidencepilot

2. Create a virtual environment

python -m venv .venv

Activate the virtual environment:

Windows:

.venv\Scripts\activate

macOS/Linux:

source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a ".env" file in the project root.

Add the required Google Cloud / Vertex AI configuration:

GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=global
GOOGLE_GENAI_USE_VERTEXAI=1

Replace "your-project-id" with your Google Cloud project ID.

5. Authenticate with Google Cloud

gcloud auth login

Set your Google Cloud project:

gcloud config set project YOUR_PROJECT_ID

Replace "YOUR_PROJECT_ID" with your Google Cloud project ID.

6. Run EvidencePilot locally

Start the FastAPI application with Uvicorn:

uvicorn app:app --reload

The application will be available at:

http://127.0.0.1:8000

7. Open the API documentation

EvidencePilot provides interactive API documentation through FastAPI.

Open:

http://127.0.0.1:8000/docs

8. Docker

EvidencePilot includes a Dockerfile configured to run the FastAPI application with Uvicorn on port 8080.
Build the Docker image:

docker build -t evidencepilot .

Run the container locally:

docker run -p 8080:8080 evidencepilot

The containerized application will be available at:

http://localhost:8080

Interactive API documentation:
http://localhost:8080/docs

9. Verify the application

Open the application/API documentation in your browser and verify that the EvidencePilot endpoints are available and responding.

10. Cloud deployment

EvidencePilot is containerized using Docker and is designed to be deployable to Google Cloud Run.

The Docker container can be built with:

docker build -t evidencepilot .

After configuring Google Cloud and enabling the required services, the container can be deployed to Cloud Run using:

gcloud run deploy evidencepilot \
  --source . \
  --region YOUR_REGION \
  --allow-unauthenticated

Replace "YOUR_REGION" with your Google Cloud deployment region.


11. Verify the Cloud Run deployment

After deployment, Google Cloud will provide a Cloud Run service URL.

Open the URL in a browser and verify that the EvidencePilot service is running.

The deployment can also be verified in:

Google Cloud Console → Cloud Run → EvidencePilot

. 
##👩🏻‍⚕️ Developer

Dr Neha Malav
MBBS/Ai/ML/gen ai/data analytics
malavneha855@gmail.com

☆linkdin

https://www.linkedin.com/in/dr-neha-malav-743a25332
 



