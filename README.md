# EvidencePilot 🔎

### An Autonomous, Evidence-Focused Clinical Research Agent

EvidencePilot is an AI-powered research workflow designed to help users investigate clinical and biomedical questions using structured evidence retrieval, research planning, and evidence-gap analysis.

Instead of simply generating an answer, EvidencePilot breaks a research question into a structured workflow and produces an evidence-focused research brief.

## 🚀 Live Demo

**API / Interactive Documentation:**

https://evidencepilot.onrender.com/docs

**Live Service:**

https://evidencepilot.onrender.com

## 💻 Source Code

https://github.com/malavneha/evidencepilot

## blog link

https://nehamalavai-builder.blogspot.com/2026/08/building-evidencepilot-evidence.html
## video demo

https://youtube.com/shorts/gH1DQYhbmCE?si=Cce5WbWS-EXsEdYO

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
Google Cloud Run was used as part of the development and deployment workflow. However, deployment on Cloud Run was blocked by a Google Cloud billing/account issue.
The issue was reported to Google Cloud support and the hackathon managers. To ensure that the project remained publicly accessible and testable, the working service was deployed on Render.
Current public deployment:
https://evidencepilot.onrender.com⁠
-----------
🧪 Testing

Open the interactive API documentation:
https://evidencepilot.onrender.com/docs⁠�
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
---------------
📌 Hackathon Project
Built for the Google Cloud / Gemini hackathon to demonstrate an evidence-focused autonomous research workflow using Google AI technologies.
Built with Python, FastAPI, Google GenAI SDK, Gemini, and Google Cloud technologies.

----------
. 
##👩🏻‍⚕️ Developer

Dr Neha Malav
MBBS/Ai/ML/gen ai/data analytics

linkdin

https://www.linkedin.com/in/dr-neha-malav-743a25332



