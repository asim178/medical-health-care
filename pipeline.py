"""
AI Mustaqbil 2.0 — Multi-Agent Healthcare Pipeline
Powered by Ollama (local LLM — no API key needed)
5 specialized agents working as a team
"""

from typing import TypedDict
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END

# ─────────────────────────────────────────────────────────────────
# LLM — Ollama (run: `ollama run llama3.2` before starting app)
# ─────────────────────────────────────────────────────────────────
llm = ChatOllama(model="llama3.2", temperature=0.2)


# ─────────────────────────────────────────────────────────────────
# SHARED STATE — flows through every agent
# ─────────────────────────────────────────────────────────────────
class MedicalState(TypedDict):
    patient_input: str
    extracted_symptoms: str
    retrieved_context: str
    diagnosis: str
    safety_check: str
    is_emergency: bool
    validated_diagnosis: str
    final_report: str


# ─────────────────────────────────────────────────────────────────
# AGENT 1 — Intake Agent
# ─────────────────────────────────────────────────────────────────
def intake_agent(state: MedicalState) -> MedicalState:
    print("🩺 [Agent 1] Intake Agent — extracting symptoms...")
    messages = [
        SystemMessage(content="""You are a medical intake specialist.
Extract and list all symptoms, duration, severity, and relevant patient details
from the patient's description. Be structured and precise.
Format: bullet points only."""),
        HumanMessage(content=state["patient_input"])
    ]
    response = llm.invoke(messages)
    state["extracted_symptoms"] = response.content
    return state


# ─────────────────────────────────────────────────────────────────
# AGENT 2 — Knowledge Agent (RAG or LLM fallback)
# ─────────────────────────────────────────────────────────────────
def knowledge_agent(state: MedicalState) -> MedicalState:
    print("📚 [Agent 2] Knowledge Agent — retrieving medical context...")
    try:
        from rag.retriever import retrieve_context
        context = retrieve_context(state["extracted_symptoms"])
    except Exception:
        messages = [
            SystemMessage(content="""You are a medical knowledge base.
Given these symptoms, provide relevant medical background:
- Possible conditions that match
- Key differentiating factors
- Red flag symptoms to watch for
Be concise and clinical."""),
            HumanMessage(content=state["extracted_symptoms"])
        ]
        context = llm.invoke(messages).content
    state["retrieved_context"] = context
    return state


# ─────────────────────────────────────────────────────────────────
# AGENT 3 — Diagnosis Agent
# ─────────────────────────────────────────────────────────────────
def diagnosis_agent(state: MedicalState) -> MedicalState:
    print("🔬 [Agent 3] Diagnosis Agent — analyzing...")
    messages = [
        SystemMessage(content="""You are an expert clinical AI assistant.
Using the extracted symptoms and medical context, suggest:
1. Most likely diagnosis (with confidence: High/Medium/Low)
2. 2-3 differential diagnoses
3. Recommended immediate actions
4. Tests to confirm diagnosis
Always add: 'This is AI-generated. Consult a licensed physician.'"""),
        HumanMessage(content=f"""
SYMPTOMS:
{state["extracted_symptoms"]}

MEDICAL CONTEXT:
{state["retrieved_context"]}
""")
    ]
    response = llm.invoke(messages)
    state["diagnosis"] = response.content
    return state


# ─────────────────────────────────────────────────────────────────
# AGENT 4 — Safety Agent (Responsible AI — emergency detection)
# ─────────────────────────────────────────────────────────────────
EMERGENCY_KEYWORDS = [
    "chest pain", "heart attack", "can't breathe", "cannot breathe",
    "difficulty breathing", "throat closing", "throat tight", "anaphylaxis",
    "stroke", "face drooping", "arm weak", "severe bleeding", "unconscious",
    "not breathing", "seizure", "overdose", "suicidal", "suicide",
    "coughing blood", "vomiting blood", "severe allergic"
]

def safety_agent(state: MedicalState) -> MedicalState:
    print("🛡️  [Agent 4] Safety Agent — checking for emergencies...")

    # Rule-based emergency detection (fast, no LLM needed)
    combined_text = (state["patient_input"] + " " + state["extracted_symptoms"]).lower()
    is_emergency = any(kw in combined_text for kw in EMERGENCY_KEYWORDS)

    messages = [
        SystemMessage(content="""You are a patient safety officer AI.
Your job:
1. Check if any symptoms indicate a MEDICAL EMERGENCY requiring immediate care.
2. Check for dangerous drug interactions if multiple medications are mentioned.
3. Flag any dangerous assumptions in the diagnosis.
4. Assign a confidence score (0.0 to 1.0) to the diagnosis.

Output format:
EMERGENCY: YES/NO
CONFIDENCE: 0.0-1.0
DRUG_INTERACTIONS: none detected / [list any found]
SAFETY_FLAGS: [any concerns]
ASSESSMENT: [2-3 sentence summary]
MANDATORY: Always end with "This AI output requires review by a licensed physician before any action is taken." """),
        HumanMessage(content=f"""
SYMPTOMS: {state["extracted_symptoms"]}
PROPOSED DIAGNOSIS: {state["diagnosis"]}
ORIGINAL INPUT: {state["patient_input"]}
""")
    ]
    response = llm.invoke(messages)
    safety_text = response.content

    # Override emergency flag if LLM also detects it
    if "EMERGENCY: YES" in safety_text.upper():
        is_emergency = True

    state["safety_check"] = safety_text
    state["is_emergency"] = is_emergency
    return state


# ─────────────────────────────────────────────────────────────────
# AGENT 5 — Critic Agent (validates the diagnosis)
# ─────────────────────────────────────────────────────────────────
def critic_agent(state: MedicalState) -> MedicalState:
    print("⚖️  [Agent 5] Critic Agent — validating diagnosis...")
    messages = [
        SystemMessage(content="""You are a senior medical reviewer AI.
Review the diagnosis critically:
- Does it logically follow from the symptoms?
- Are there missing differentials?
- Is the confidence level appropriate?
- Any dangerous assumptions or red flags missed?
Output: APPROVED or REVISED + explanation + corrected diagnosis if needed."""),
        HumanMessage(content=f"""
ORIGINAL SYMPTOMS:
{state["extracted_symptoms"]}

PROPOSED DIAGNOSIS:
{state["diagnosis"]}

SAFETY ASSESSMENT:
{state["safety_check"]}
""")
    ]
    response = llm.invoke(messages)
    state["validated_diagnosis"] = response.content
    return state


# ─────────────────────────────────────────────────────────────────
# AGENT 5 — Report Agent (patient-friendly output)
# ─────────────────────────────────────────────────────────────────
def report_agent(state: MedicalState) -> MedicalState:
    print("📋 [Agent 6] Report Agent — generating final report...")
    emergency_note = "\n⚠️ EMERGENCY SERVICES REQUIRED — Call 1122 immediately.\n" if state.get("is_emergency") else ""
    messages = [
        SystemMessage(content="""You are a medical report writer.
Write a clear, empathetic, patient-friendly summary report with:
- Summary of reported symptoms
- Primary concern / likely diagnosis
- What to do next (step-by-step)
- When to seek emergency care
- Important disclaimer: This AI system does not replace a licensed physician. Always consult a doctor.
Use simple language. Format with clear headings."""),
        HumanMessage(content=f"""
{emergency_note}
SYMPTOMS: {state["extracted_symptoms"]}
SAFETY ASSESSMENT: {state["safety_check"]}
VALIDATED DIAGNOSIS: {state["validated_diagnosis"]}
""")
    ]
    response = llm.invoke(messages)
    final = response.content
    # Hardcoded safety disclaimer — always appended
    final += "\n\n---\n⚠️ IMPORTANT: This report was generated by an AI system for demonstration purposes only. It does not constitute medical advice. Please consult a licensed physician before taking any medical action."
    state["final_report"] = final
    return state


# ─────────────────────────────────────────────────────────────────
# BUILD THE MULTI-AGENT GRAPH
# ─────────────────────────────────────────────────────────────────
def build_pipeline():
    graph = StateGraph(MedicalState)
    graph.add_node("intake",    intake_agent)
    graph.add_node("knowledge", knowledge_agent)
    graph.add_node("diagnosis", diagnosis_agent)
    graph.add_node("safety",    safety_agent)
    graph.add_node("critic",    critic_agent)
    graph.add_node("report",    report_agent)
    graph.set_entry_point("intake")
    graph.add_edge("intake",    "knowledge")
    graph.add_edge("knowledge", "diagnosis")
    graph.add_edge("diagnosis", "safety")
    graph.add_edge("safety",    "critic")
    graph.add_edge("critic",    "report")
    graph.add_edge("report",    END)
    return graph.compile()


def run_pipeline(patient_input: str) -> MedicalState:
    pipeline = build_pipeline()
    initial_state = MedicalState(
        patient_input=patient_input,
        extracted_symptoms="",
        retrieved_context="",
        diagnosis="",
        safety_check="",
        is_emergency=False,
        validated_diagnosis="",
        final_report=""
    )
    return pipeline.invoke(initial_state)


if __name__ == "__main__":
    test = "I have had a high fever of 103F for 3 days, severe headache, pain behind my eyes, and a rash on my arms."
    result = run_pipeline(test)
    print("\n" + "="*60)
    print(result["final_report"])
