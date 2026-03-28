# 🏥 MediAgent — AI Mustaqbil 2.0
### Multi-Agent Healthcare AI System | Powered by Ollama (100% Local)

---

## 🎯 What is MediAgent?

MediAgent is a **multi-agent AI pipeline** that simulates a full medical triage workflow using 5 specialized AI agents — all running **locally via Ollama** with zero API costs.

A patient describes their symptoms → 5 agents think, collaborate, and validate → A comprehensive clinical report is generated.

---

## 🤖 The 5-Agent Pipeline

```
Patient Input
     │
     ▼
[Agent 1: Intake]      — Extracts symptoms, duration, severity from natural language
     │
     ▼
[Agent 2: Knowledge]   — Retrieves relevant medical context via RAG (FAISS)
     │
     ▼
[Agent 3: Diagnosis]   — Synthesizes a clinical diagnosis with confidence level
     │
     ▼
[Agent 4: Critic]      — Validates the diagnosis, flags errors or missing differentials
     │
     ▼
[Agent 5: Report]      — Generates a clean, patient-friendly summary report
```

---

## 🚀 Quick Start

### Step 1 — Install Ollama & pull a model
```bash
# Install from https://ollama.com
ollama pull llama3.2
```

### Step 2 — Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — (Optional) Add your own medical docs
```
Drop any .txt or .pdf files into:  rag/docs/
Then run:  python rag/retriever.py
```

### Step 4 — Launch the app
```bash
cd ui
streamlit run app.py
```

---

## 📁 Project Structure

```
hackathon_kit/
├── agents/
│   └── pipeline.py          # 5-agent LangGraph pipeline (Ollama-powered)
├── rag/
│   ├── retriever.py         # FAISS vector store + Ollama embeddings
│   └── docs/
│       └── medical_knowledge.txt   # Sample medical knowledge base
├── ui/
│   └── app.py               # Streamlit UI (beautiful dark medical theme)
├── requirements.txt
└── README.md
```

---

## 🏆 Why This Wins (Evaluation Criteria Coverage)

| Criterion | How MediAgent covers it |
|---|---|
| **Innovation** | 5-agent debate/validation loop (critic agent is unique) |
| **Technical Depth** | LangGraph state machine + RAG + local LLM |
| **Agent Collaboration** | Each agent builds on the previous one's output |
| **Real-world Impact** | Pakistan-relevant diseases in knowledge base |
| **Code Quality** | Modular, readable, documented |
| **Demo** | Live Streamlit UI with step-by-step agent tracker |

---

## 🎤 2-Minute Pitch Script

> "Healthcare access in Pakistan is limited — especially for quick triage in rural areas.
> MediAgent solves this by running **5 AI agents in sequence** — intake, knowledge retrieval,
> diagnosis, validation, and reporting — all **locally on any laptop** with no internet needed.
> The critic agent is what makes this unique: it actually **debates and validates** the diagnosis
> before the patient sees it, reducing AI hallucination risk. Let me show you a live demo."

---

## ⚠️ Disclaimer

MediAgent is a **hackathon prototype** for demonstration purposes only.
It is not a substitute for professional medical advice.
Always consult a licensed physician for medical decisions.
