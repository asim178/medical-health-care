"""
AI Mustaqbil 2.0 — MediAgent UI (Upgraded)
Multi-agent healthcare pipeline — Ollama powered, fully local
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

st.set_page_config(
    page_title="MediAgent — AI Mustaqbil 2.0",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background: #050810; }
.stApp { background: #050810; color: #c8d4e8; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 2rem 2rem !important; max-width: 1400px; }

.hero {
    position: relative; background: #0b1220;
    border: 1px solid #1a2840; border-radius: 20px;
    padding: 40px 44px 36px; margin-bottom: 28px; overflow: hidden;
}
.hero::after {
    content: ''; position: absolute; top: 0; right: 0;
    width: 340px; height: 340px;
    background: radial-gradient(circle at 80% 20%, rgba(56,189,248,0.07) 0%, transparent 65%);
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace; font-size: 0.7rem;
    letter-spacing: 2.5px; color: #38bdf8; text-transform: uppercase; margin-bottom: 12px;
}
.hero-title {
    font-family: 'Syne', sans-serif; font-size: 3rem; font-weight: 800;
    color: #f0f6ff; line-height: 1.05; margin-bottom: 10px; letter-spacing: -1px;
}
.hero-title em { color: #38bdf8; font-style: normal; }
.hero-sub { color: #5a7fa8; font-size: 0.95rem; font-weight: 300; max-width: 560px; line-height: 1.6; }
.badge-row { display: flex; gap: 8px; margin-top: 22px; flex-wrap: wrap; }
.badge {
    font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
    letter-spacing: 0.5px; padding: 4px 12px; border-radius: 4px; border: 1px solid;
}
.badge-blue  { background: rgba(56,189,248,0.08); border-color: rgba(56,189,248,0.25); color: #38bdf8; }
.badge-green { background: rgba(52,211,153,0.08); border-color: rgba(52,211,153,0.25); color: #34d399; }
.badge-amber { background: rgba(251,191,36,0.08); border-color: rgba(251,191,36,0.25); color: #fbbf24; }

.pipeline {
    display: flex; align-items: center; gap: 0; background: #0b1220;
    border: 1px solid #1a2840; border-radius: 14px; padding: 18px 28px;
    margin-bottom: 24px; overflow-x: auto;
}
.p-step { display: flex; flex-direction: column; align-items: center; gap: 7px; min-width: 90px; }
.p-icon {
    width: 46px; height: 46px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center; font-size: 1.2rem;
    background: #111c2e; border: 1px solid #1e3050; transition: all 0.3s;
}
.p-icon.active { background: rgba(56,189,248,0.12); border-color: #38bdf8; box-shadow: 0 0 16px rgba(56,189,248,0.2); }
.p-icon.done { background: rgba(52,211,153,0.1); border-color: #34d399; }
.p-icon.safety-done { background: rgba(251,191,36,0.1); border-color: #fbbf24; }
.p-label {
    font-family: 'JetBrains Mono', monospace; font-size: 0.6rem;
    letter-spacing: 0.5px; color: #2d4a6a; text-align: center; line-height: 1.4;
}
.p-label.active { color: #38bdf8; }
.p-label.done { color: #34d399; }
.p-label.safety-done { color: #fbbf24; }
.p-arrow { color: #1a2840; font-size: 1rem; margin: 0 6px; padding-bottom: 22px; flex-shrink: 0; }

.input-label {
    font-family: 'Syne', sans-serif; font-size: 0.85rem; font-weight: 600;
    color: #8aafc8; letter-spacing: 0.5px; margin-bottom: 10px;
}
.stTextArea textarea {
    background: #060d1a !important; border: 1px solid #1a2840 !important;
    color: #c8d4e8 !important; border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important; font-size: 0.93rem !important;
    padding: 14px 16px !important; line-height: 1.6 !important;
}
.stTextArea textarea:focus { border-color: #38bdf8 !important; box-shadow: 0 0 0 2px rgba(56,189,248,0.1) !important; }

.stButton > button {
    background: #38bdf8 !important; color: #050810 !important;
    border: none !important; border-radius: 10px !important; padding: 11px 28px !important;
    font-family: 'Syne', sans-serif !important; font-weight: 700 !important;
    font-size: 0.88rem !important; width: 100% !important; transition: all 0.2s !important;
}
.stButton > button:hover { background: #7dd3fc !important; transform: translateY(-1px) !important; }

.qtest-title {
    font-family: 'Syne', sans-serif; font-size: 0.78rem; font-weight: 700;
    color: #38bdf8; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 4px;
}
.qtest-sub { font-size: 0.75rem; color: #3a5570; margin-bottom: 12px; }
.qcat {
    font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; letter-spacing: 1px;
    padding: 3px 10px; border-radius: 4px; margin-bottom: 8px; margin-top: 10px; display: inline-block;
}
.qcat-red    { background: rgba(239,68,68,0.12);   color: #f87171; border: 1px solid rgba(239,68,68,0.2); }
.qcat-blue   { background: rgba(56,189,248,0.08);   color: #38bdf8; border: 1px solid rgba(56,189,248,0.2); }
.qcat-purple { background: rgba(167,139,250,0.08);  color: #a78bfa; border: 1px solid rgba(167,139,250,0.2); }
.qcat-green  { background: rgba(52,211,153,0.08);   color: #34d399; border: 1px solid rgba(52,211,153,0.2); }

.emergency-alert {
    background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.5);
    border-radius: 12px; padding: 20px 24px; margin-bottom: 20px;
    animation: pulse-border 1.5s ease-in-out infinite;
}
@keyframes pulse-border {
    0%, 100% { border-color: rgba(239,68,68,0.4); }
    50% { border-color: rgba(239,68,68,0.9); }
}
.emergency-title { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 800; color: #f87171; margin-bottom: 8px; }
.emergency-body { color: #fca5a5; font-size: 0.9rem; line-height: 1.6; }

.rcard { background: #0b1220; border: 1px solid #1a2840; border-radius: 14px; padding: 22px 26px; margin-bottom: 16px; }
.rcard.highlight { border-color: #38bdf8; background: #0c1828; }
.rcard.safety { border-color: #fbbf24; background: #0e120a; }
.rc-head { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.rc-icon { font-size: 1.2rem; }
.rc-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #e8f0fc; }
.rc-body { color: #7a9ab8; font-size: 0.88rem; line-height: 1.75; white-space: pre-wrap; }

.disclaimer {
    background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.25);
    border-radius: 10px; padding: 14px 18px; color: #d4a017;
    font-size: 0.82rem; line-height: 1.6; margin-top: 20px;
}

section[data-testid="stSidebar"] { background: #070c16 !important; border-right: 1px solid #111e30 !important; }
.sb-logo { font-family: 'Syne', sans-serif; font-size: 1.3rem; font-weight: 800; color: #f0f6ff; margin-bottom: 4px; }
.sb-logo em { color: #38bdf8; font-style: normal; }
.sb-tagline { font-size: 0.72rem; color: #2d4a6a; font-family: 'JetBrains Mono', monospace; }
.sb-section { margin-bottom: 20px; }
.sb-section-title {
    font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; letter-spacing: 2px;
    color: #2d4a6a; text-transform: uppercase; margin-bottom: 10px;
    padding-bottom: 6px; border-bottom: 1px solid #111e30;
}
.sb-item { display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: #4a6a88; padding: 5px 0; }
.sb-dot { width: 5px; height: 5px; border-radius: 50%; background: #38bdf8; flex-shrink: 0; }
.sb-dot-green { background: #34d399; }
.sb-dot-amber { background: #fbbf24; }
.status-ok {
    display: inline-block; font-size: 0.62rem; padding: 2px 7px; border-radius: 3px;
    background: rgba(52,211,153,0.1); color: #34d399; border: 1px solid rgba(52,211,153,0.2);
    font-family: 'JetBrains Mono', monospace; margin-left: auto;
}

.stTabs [data-baseweb="tab-list"] {
    background: #0b1220 !important; border-radius: 10px !important;
    border: 1px solid #1a2840 !important; gap: 0 !important; padding: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    color: #3a5570 !important; font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important; font-size: 0.8rem !important;
    border-radius: 7px !important; padding: 8px 18px !important;
}
.stTabs [aria-selected="true"] { background: #1a2840 !important; color: #c8d4e8 !important; }
.stTabs [data-baseweb="tab-panel"] { background: transparent !important; padding: 20px 0 0 0 !important; }
.stSelectbox > div > div { background: #0b1220 !important; border: 1px solid #1a2840 !important; color: #c8d4e8 !important; border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)


# ── Quick test cases ──────────────────────────────────────────────
QUICK_CASES = {
    "EMERGENCY CASES": {
        "color": "qcat-red",
        "cases": {
            "Cardiac Emergency": "Severe chest pain radiating to my left arm and jaw, profuse sweating, shortness of breath, nausea. Pain started 20 minutes ago and is intensifying. I feel like something is seriously wrong.",
            "Severe Allergic Reaction": "After eating shrimp I developed hives all over my body, my throat feels tight, I have difficulty breathing and my tongue is swelling. This started about 10 minutes ago.",
        }
    },
    "INFECTIONS & ILLNESS": {
        "color": "qcat-blue",
        "cases": {
            "Dengue Fever": "High fever of 103.5F for the past 3 days. Severe headache behind my eyes. Red rash on arms and torso. Body aches especially in lower back and joints. Extremely tired. I live in an area with high mosquito activity in Karachi.",
            "Urinary Tract Infection": "Burning when urinating for 2 days. Frequent urge to urinate but little comes out. Pelvic pain and pressure. Urine looks cloudy and smells strong. No fever currently.",
            "Asthma Attack": "Chest is very tight, wheezing when I breathe, shortness of breath especially at night. Using inhaler but not helping much. Coughing a lot. History of asthma.",
        }
    },
    "CHRONIC CONDITIONS": {
        "color": "qcat-purple",
        "cases": {
            "Type 2 Diabetes": "Excessive thirst and frequent urination for 3 weeks. Blurry vision, fatigue, slow healing cut on foot. Weight gain over past year. Strong family history of diabetes.",
            "Migraine Headaches": "Throbbing pain on left side of head, nausea, vomiting, sensitivity to light and sound. Lasts 4 to 6 hours. Preceded by seeing zigzag lines.",
        }
    },
    "MENTAL HEALTH": {
        "color": "qcat-green",
        "cases": {
            "Depression & Anxiety": "Feeling hopeless and empty for 2 months. Lost interest in activities I used to enjoy. Sleep problems, either too much or too little. Difficulty concentrating. Constant anxious thoughts.",
            "Drug Interaction Check": "I take metformin 500mg for diabetes, lisinopril 10mg for blood pressure, and aspirin 81mg daily. I want to start ibuprofen for joint pain. Is this safe?",
        }
    }
}

# ── Session state ─────────────────────────────────────────────────
if "symptom_text" not in st.session_state:
    st.session_state.symptom_text = ""
if "results" not in st.session_state:
    st.session_state.results = None
if "emergency" not in st.session_state:
    st.session_state.emergency = False

# ── Sidebar ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 10px 0 24px 0;'>
        <div class='sb-logo'>Medi<em>Agent</em></div>
        <div class='sb-tagline'>AI MUSTAQBIL 2.0 // HEALTHCARE TRACK</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sb-section'>
        <div class='sb-section-title'>System Status</div>
        <div class='sb-item'><span class='sb-dot'></span> LangGraph pipeline <span class='status-ok'>ACTIVE</span></div>
        <div class='sb-item'><span class='sb-dot'></span> FAISS vector store <span class='status-ok'>READY</span></div>
        <div class='sb-item'><span class='sb-dot sb-dot-amber'></span> Ollama local LLM <span class='status-ok'>LOCAL</span></div>
        <div class='sb-item'><span class='sb-dot sb-dot-green'></span> 6-agent pipeline <span class='status-ok'>READY</span></div>
    </div>
    <div class='sb-section'>
        <div class='sb-section-title'>Agent Pipeline</div>
        <div class='sb-item'><span class='sb-dot'></span> 1. Intake — symptom extraction</div>
        <div class='sb-item'><span class='sb-dot'></span> 2. Knowledge — RAG retrieval</div>
        <div class='sb-item'><span class='sb-dot'></span> 3. Diagnosis — clinical analysis</div>
        <div class='sb-item'><span class='sb-dot sb-dot-amber'></span> 4. Safety — emergency check</div>
        <div class='sb-item'><span class='sb-dot'></span> 5. Critic — validation layer</div>
        <div class='sb-item'><span class='sb-dot sb-dot-green'></span> 6. Report — patient summary</div>
    </div>
    <div class='sb-section'>
        <div class='sb-section-title'>Responsible AI</div>
        <div class='sb-item'><span class='sb-dot sb-dot-amber'></span> Emergency auto-detection</div>
        <div class='sb-item'><span class='sb-dot sb-dot-amber'></span> Drug interaction checks</div>
        <div class='sb-item'><span class='sb-dot sb-dot-amber'></span> Mandatory human referral</div>
        <div class='sb-item'><span class='sb-dot sb-dot-amber'></span> Confidence scoring</div>
    </div>
    """, unsafe_allow_html=True)

    model = st.selectbox("Ollama Model", ["llama3.2", "llama3.1", "mistral", "gemma2", "phi3"], index=0)

# ── Hero ──────────────────────────────────────────────────────────
st.markdown("""
<div class='hero'>
    <div class='hero-eyebrow'>AI Mustaqbil 2.0 · Healthcare & Public Health · Multi-Agent System</div>
    <h1 class='hero-title'>Medi<em>Agent</em></h1>
    <p class='hero-sub'>6 specialized AI agents working in collaboration — powered entirely by your local Ollama model. No API. No data leaves your machine.</p>
    <div class='badge-row'>
        <span class='badge badge-blue'>6-AGENT PIPELINE</span>
        <span class='badge badge-green'>100% LOCAL & PRIVATE</span>
        <span class='badge badge-amber'>SAFETY CHECKED</span>
        <span class='badge badge-blue'>RAG ENABLED</span>
        <span class='badge badge-green'>RESPONSIBLE AI</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Pipeline tracker ──────────────────────────────────────────────
AGENTS = [
    ("🩺", "Intake\nExtraction"),
    ("📚", "Knowledge\nRAG"),
    ("🔬", "Diagnosis\nAnalysis"),
    ("🛡️", "Safety\nCheck"),
    ("⚖️", "Critic\nValidation"),
    ("📋", "Report\nSummary"),
]

def render_pipeline(active=-1, done=[], safety_done=False):
    html = "<div class='pipeline'>"
    for i, (icon, label) in enumerate(AGENTS):
        if i in done:
            cls = "safety-done" if (i == 3 and safety_done) else "done"
        elif i == active:
            cls = "active"
        else:
            cls = ""
        html += f"""
        <div class='p-step'>
            <div class='p-icon {cls}'>{icon}</div>
            <div class='p-label {cls}'>{label.replace(chr(10), '<br>')}</div>
        </div>"""
        if i < len(AGENTS) - 1:
            html += "<div class='p-arrow'>→</div>"
    html += "</div>"
    return html

pipeline_slot = st.empty()
pipeline_slot.markdown(render_pipeline(), unsafe_allow_html=True)

# ── Input + quick tests ───────────────────────────────────────────
col_main, col_tests = st.columns([3, 2])

with col_main:
    st.markdown("<div class='input-label'>🩺 Describe Your Symptoms</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.8rem;color:#2d4a6a;margin-bottom:10px'>Be detailed — include duration, severity, and any relevant medical history</div>", unsafe_allow_html=True)

    patient_input = st.text_area(
        "symptoms",
        value=st.session_state.symptom_text,
        placeholder="e.g. High fever of 103F for 3 days, severe headache behind my eyes, red rash on arms and torso, body aches...",
        height=150,
        label_visibility="collapsed"
    )

    c1, c2 = st.columns([3, 1])
    with c1:
        analyze_btn = st.button("🔍  Analyze Symptoms", use_container_width=True)
    with c2:
        if st.button("Clear", use_container_width=True):
            st.session_state.symptom_text = ""
            st.session_state.results = None
            st.session_state.emergency = False
            st.rerun()

with col_tests:
    st.markdown("<div class='qtest-title'>Quick Test Cases</div>", unsafe_allow_html=True)
    st.markdown("<div class='qtest-sub'>Click any button to auto-fill symptoms</div>", unsafe_allow_html=True)

    for category, data in QUICK_CASES.items():
        st.markdown(f"<div class='qcat {data['color']}'>{category}</div>", unsafe_allow_html=True)
        for case_name, case_text in data["cases"].items():
            if st.button(f"  {case_name}", key=f"qt_{case_name}", use_container_width=True):
                st.session_state.symptom_text = case_text
                st.rerun()

# ── Run pipeline ──────────────────────────────────────────────────
if analyze_btn and patient_input.strip():
    try:
        from langchain_ollama import ChatOllama
        import pipeline as pipe_module
        pipe_module.llm = ChatOllama(model=model, temperature=0.2)
    except Exception as e:
        st.error(f"Could not load pipeline: {e}. Make sure Ollama is running and pipeline.py is in the same folder.")
        st.stop()

    status_slot = st.empty()
    done_steps = []
    safety_triggered = False

    state = {
        "patient_input": patient_input,
        "extracted_symptoms": "",
        "retrieved_context": "",
        "diagnosis": "",
        "safety_check": "",
        "is_emergency": False,
        "validated_diagnosis": "",
        "final_report": ""
    }

    agent_fns = [
        ("intake_agent", 0),
        ("knowledge_agent", 1),
        ("diagnosis_agent", 2),
        ("safety_agent", 3),
        ("critic_agent", 4),
        ("report_agent", 5),
    ]
    labels = ["Intake", "Knowledge", "Diagnosis", "Safety", "Critic", "Report"]

    for fn_name, idx in agent_fns:
        pipeline_slot.markdown(render_pipeline(active=idx, done=done_steps, safety_done=safety_triggered), unsafe_allow_html=True)
        status_slot.markdown(
            f"<p style='color:#38bdf8;font-size:0.82rem;font-family:JetBrains Mono,monospace;margin-top:8px'>▶ Agent {idx+1} ({labels[idx]}) running...</p>",
            unsafe_allow_html=True
        )
        fn = getattr(pipe_module, fn_name, None)
        if fn is None:
            st.warning(f"Function {fn_name} not found in pipeline.py — skipping.")
            done_steps.append(idx)
            continue
        state = fn(state)
        done_steps.append(idx)
        if fn_name == "safety_agent" and state.get("is_emergency"):
            safety_triggered = True
        time.sleep(0.05)

    pipeline_slot.markdown(render_pipeline(active=-1, done=done_steps, safety_done=safety_triggered), unsafe_allow_html=True)
    status_slot.markdown(
        "<p style='color:#34d399;font-size:0.82rem;font-family:JetBrains Mono,monospace;margin-top:8px'>✓ All 6 agents complete</p>",
        unsafe_allow_html=True
    )
    st.session_state.results = state
    st.session_state.emergency = safety_triggered

# ── Results ───────────────────────────────────────────────────────
if st.session_state.results:
    state = st.session_state.results
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if st.session_state.emergency:
        st.markdown("""
        <div class='emergency-alert'>
            <div class='emergency-title'>🚨 EMERGENCY DETECTED — CALL EMERGENCY SERVICES NOW</div>
            <div class='emergency-body'>
                The Safety Agent has identified potentially life-threatening symptoms.<br>
                <strong>Do not wait. Call 1122 (Pakistan) or your local emergency number immediately.</strong><br>
                Do not rely on this AI system for emergency medical decisions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋  Final Report", "🔬  Detailed Analysis", "🗂  Agent Outputs"])

    with tab1:
        st.markdown(f"""
        <div class='rcard highlight'>
            <div class='rc-head'><span class='rc-icon'>📋</span><span class='rc-title'>Patient Report</span></div>
            <div class='rc-body'>{state.get('final_report','No report generated.')}</div>
        </div>
        """, unsafe_allow_html=True)
        col_dl, _ = st.columns([1, 2])
        with col_dl:
            st.download_button("⬇️  Download Report (.txt)", data=state.get("final_report", ""),
                               file_name="mediagent_report.txt", mime="text/plain", use_container_width=True)

    with tab2:
        st.markdown(f"""
        <div class='rcard'>
            <div class='rc-head'><span class='rc-icon'>🩺</span><span class='rc-title'>Extracted Symptoms</span></div>
            <div class='rc-body'>{state.get('extracted_symptoms','')}</div>
        </div>
        <div class='rcard'>
            <div class='rc-head'><span class='rc-icon'>🔬</span><span class='rc-title'>Clinical Diagnosis</span></div>
            <div class='rc-body'>{state.get('diagnosis','')}</div>
        </div>
        <div class='rcard safety'>
            <div class='rc-head'><span class='rc-icon'>🛡️</span><span class='rc-title'>Safety Agent Assessment</span></div>
            <div class='rc-body'>{state.get('safety_check','')}</div>
        </div>
        <div class='rcard'>
            <div class='rc-head'><span class='rc-icon'>⚖️</span><span class='rc-title'>Critic Validation</span></div>
            <div class='rc-body'>{state.get('validated_diagnosis','')}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        with st.expander("📚 Knowledge Retrieved (RAG Context)"):
            st.code(state.get("retrieved_context", ""), language="markdown")
        with st.expander("🩺 Raw Symptom Extraction"):
            st.code(state.get("extracted_symptoms", ""), language="markdown")
        with st.expander("🔬 Raw Diagnosis Output"):
            st.code(state.get("diagnosis", ""), language="markdown")
        with st.expander("🛡️ Safety Agent Raw Output"):
            st.code(state.get("safety_check", ""), language="markdown")
        with st.expander("⚖️ Critic Raw Output"):
            st.code(state.get("validated_diagnosis", ""), language="markdown")

    st.markdown("""
    <div class='disclaimer'>
        ⚠️ <strong>Medical Disclaimer:</strong> MediAgent is an AI prototype built for AI Mustaqbil 2.0 — for educational and demonstration purposes only.
        It does not replace professional medical advice, diagnosis, or treatment.
        Always consult a licensed physician for any medical concerns.
        In an emergency, call 1122 (Pakistan) or your local emergency services immediately.
    </div>
    """, unsafe_allow_html=True)

elif analyze_btn and not patient_input.strip():
    st.warning("Please describe your symptoms before analyzing.")
