# MediAgent — AI Mustaqbil 2.0
### Multi-Agent Healthcare AI System | Healthcare & Public Health Track

A 6-agent LangGraph pipeline for intelligent medical triage, powered entirely by Ollama (local LLM). No API keys. No data leaves your machine.

---

## Architecture

```
Patient Input
    │
    ▼
[Agent 1] Intake Agent       — extracts & structures symptoms
    │
    ▼
[Agent 2] Knowledge Agent    — RAG retrieval from medical knowledge base (FAISS)
    │
    ▼
[Agent 3] Diagnosis Agent    — clinical analysis & differential diagnosis
    │
    ▼
[Agent 4] Safety Agent  ★   — emergency detection, drug interactions, confidence score
    │
    ▼
[Agent 5] Critic Agent       — validates & challenges the diagnosis
    │
    ▼
[Agent 6] Report Agent       — patient-friendly summary with mandatory referral
```

---

## Quick Start (Docker — Recommended)

### Prerequisites
- Docker Desktop installed and running
- Ollama installed on your host machine

### Step 1 — Start Ollama (on your host, NOT inside Docker)
```powershell
ollama run llama3.2
```

### Step 2 — Build and run the container
```powershell
docker-compose up --build
```

### Step 3 — Open the app
```
http://localhost:8501
```

### Stop the app
```powershell
docker-compose down
```

---

## Quick Start (Without Docker)

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start Ollama in a separate terminal
ollama run llama3.2

# 3. Run the app
streamlit run app.py
```

---

## Project Structure

```
mediagent/
├── app.py                  # Streamlit UI — golden/black theme
├── pipeline.py             # 6-agent LangGraph pipeline
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .streamlit/
│   └── config.toml         # Streamlit server config
└── rag/
    ├── retriever.py        # FAISS vector store + Ollama embeddings
    ├── docs/               # Drop .txt or .pdf medical docs here
    │   └── medical_knowledge.txt
    └── faiss_index/        # Auto-generated index (gitignored)
```

---

## Responsible AI Features

| Feature | Implementation |
|---|---|
| Emergency detection | Rule-based keyword scan + LLM confirmation |
| Drug interaction check | Safety Agent scans for medication combinations |
| Confidence scoring | Every diagnosis gets a 0.0–1.0 score |
| Mandatory disclaimer | Hardcoded into every report output |
| Human referral | Final report always ends with physician referral |

---

## Evaluation Criteria Alignment

| Criterion | Score | How we address it |
|---|---|---|
| Agent Collaboration | 20 | 6 agents with structured state handoffs via LangGraph |
| Technical Depth | 20 | LangGraph + FAISS RAG + Ollama embeddings |
| Innovation | 15 | Safety Agent debates diagnosis; local-only architecture |
| Real-world Impact | 15 | Pakistan-specific (dengue, 1122 emergency) |
| Responsible AI | 10 | Emergency detection, drug checks, confidence scores |
| Demo & Code | 20 | Clean codebase, live pipeline tracker, download report |

---

## Hackathon
**AI Mustaqbil 2.0** | Healthcare & Public Health Track | NASTP Karachi | March 27–28, 2026
