"""
AI Mustaqbil 2.0 — MediAgent
Golden · White · Black theme | Dockerized | 6-Agent Pipeline
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

st.set_page_config(
    page_title="MediAgent — AI Mustaqbil 2.0",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── GOLDEN / WHITE / BLACK THEME ─────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;900&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #0a0a0a;
    color: #e8e0cc;
}
.stApp { background: #0a0a0a; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1400px; }

/* ── GOLD PALETTE ──
   Rich gold:  #C9A84C
   Soft gold:  #E8C96D
   Pale gold:  #F5E6B8
   Black:      #0a0a0a
   Dark:       #111111
   Card bg:    #141414
   Border:     #2a2218
   White:      #F5F0E8
*/

/* ── HERO ─────────────────────────────────────── */
.hero {
    position: relative;
    background: #111111;
    border: 1px solid #2a2218;
    border-top: 3px solid #C9A84C;
    border-radius: 0 0 16px 16px;
    padding: 44px 48px 40px;
    margin-bottom: 28px;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #C9A84C 0%, #F5E6B8 50%, #C9A84C 100%);
}
.hero::after {
    content: '';
    position: absolute; top: -60px; right: -60px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(201,168,76,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem; letter-spacing: 3px; text-transform: uppercase;
    color: #C9A84C; margin-bottom: 14px;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.4rem; font-weight: 900; line-height: 1;
    color: #F5F0E8; margin-bottom: 12px; letter-spacing: -1px;
}
.hero-title span { color: #C9A84C; }
.hero-sub {
    font-size: 0.92rem; font-weight: 300; color: #6b5e40; max-width: 520px; line-height: 1.7;
}
.badge-row { display: flex; gap: 8px; margin-top: 24px; flex-wrap: wrap; }
.badge {
    font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
    letter-spacing: 0.8px; padding: 5px 12px; border-radius: 2px; border: 1px solid;
}
.b-gold   { background: rgba(201,168,76,0.1);  border-color: rgba(201,168,76,0.4); color: #C9A84C; }
.b-white  { background: rgba(245,240,232,0.06); border-color: rgba(245,240,232,0.2); color: #F5F0E8; }
.b-green  { background: rgba(74,222,128,0.06);  border-color: rgba(74,222,128,0.25); color: #4ade80; }

/* ── PIPELINE TRACKER ─────────────────────────── */
.pipeline {
    display: flex; align-items: center;
    background: #111111; border: 1px solid #2a2218;
    border-radius: 12px; padding: 20px 28px;
    margin-bottom: 24px; overflow-x: auto; gap: 0;
}
.p-step { display: flex; flex-direction: column; align-items: center; gap: 8px; min-width: 88px; }
.p-icon {
    width: 48px; height: 48px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; font-size: 1.2rem;
    background: #0a0a0a; border: 1px solid #2a2218; transition: all 0.35s;
}
.p-icon.active {
    background: rgba(201,168,76,0.12); border-color: #C9A84C;
    box-shadow: 0 0 18px rgba(201,168,76,0.25);
}
.p-icon.done { background: rgba(201,168,76,0.08); border-color: #6b5030; }
.p-icon.safety-active { background: rgba(245,158,11,0.15); border-color: #f59e0b; box-shadow: 0 0 18px rgba(245,158,11,0.3); }
.p-icon.safety-done   { background: rgba(74,222,128,0.08); border-color: #166534; }
.p-label {
    font-family: 'JetBrains Mono', monospace; font-size: 0.58rem;
    letter-spacing: 0.5px; color: #3a3020; text-align: center; line-height: 1.4;
}
.p-label.active { color: #C9A84C; }
.p-label.done   { color: #6b5030; }
.p-label.safety-active { color: #f59e0b; }
.p-label.safety-done   { color: #4ade80; }
.p-arrow { color: #2a2218; font-size: 1rem; margin: 0 4px; padding-bottom: 24px; flex-shrink: 0; }

/* ── INPUT ─────────────────────────────────────── */
.input-lbl {
    font-family: 'Playfair Display', serif; font-size: 1.1rem;
    font-weight: 600; color: #F5F0E8; margin-bottom: 6px;
}
.input-sub { font-size: 0.78rem; color: #3a3020; margin-bottom: 10px; }
.stTextArea textarea {
    background: #0f0f0f !important; border: 1px solid #2a2218 !important;
    color: #e8e0cc !important; border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important; font-size: 0.92rem !important;
    padding: 14px 16px !important; line-height: 1.65 !important;
}
.stTextArea textarea:focus {
    border-color: #C9A84C !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.12) !important;
}

/* ── BUTTONS ─────────────────────────────────────── */
.stButton > button {
    background: #C9A84C !important; color: #0a0a0a !important;
    border: none !important; border-radius: 6px !important;
    padding: 11px 28px !important; font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important; font-size: 0.88rem !important;
    letter-spacing: 0.3px !important; width: 100% !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: #E8C96D !important; transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(201,168,76,0.25) !important;
}
.stButton > button:active { transform: scale(0.98) !important; }

/* ── QUICK TESTS PANEL ───────────────────────────── */
.qt-panel {
    background: #111111; border: 1px solid #2a2218;
    border-radius: 12px; padding: 20px 20px 16px;
}
.qt-title {
    font-family: 'Playfair Display', serif; font-size: 0.95rem;
    font-weight: 700; color: #C9A84C; margin-bottom: 3px;
}
.qt-sub { font-size: 0.74rem; color: #3a3020; margin-bottom: 14px; }
.qcat {
    font-family: 'JetBrains Mono', monospace; font-size: 0.62rem;
    letter-spacing: 1.2px; text-transform: uppercase; padding: 3px 9px;
    border-radius: 2px; display: inline-block; margin: 10px 0 6px;
}
.qc-red    { background: rgba(239,68,68,0.1);  color: #f87171; border: 1px solid rgba(239,68,68,0.25); }
.qc-gold   { background: rgba(201,168,76,0.1); color: #C9A84C; border: 1px solid rgba(201,168,76,0.25); }
.qc-white  { background: rgba(245,240,232,0.06); color: #c8bea0; border: 1px solid rgba(245,240,232,0.15); }
.qc-green  { background: rgba(74,222,128,0.06); color: #4ade80; border: 1px solid rgba(74,222,128,0.2); }

/* ── EMERGENCY BANNER ────────────────────────────── */
.emergency {
    background: #1a0505; border: 1px solid #7f1d1d;
    border-left: 4px solid #ef4444; border-radius: 8px;
    padding: 20px 24px; margin-bottom: 20px;
    animation: em-pulse 1.8s ease-in-out infinite;
}
@keyframes em-pulse {
    0%,100% { border-left-color: rgba(239,68,68,0.6); }
    50%      { border-left-color: #ef4444; }
}
.em-title  { font-family: 'Playfair Display', serif; font-size: 1.15rem; font-weight: 900; color: #ef4444; margin-bottom: 8px; }
.em-body   { font-size: 0.88rem; color: #fca5a5; line-height: 1.65; }

/* ── RESULT CARDS ────────────────────────────────── */
.rcard {
    background: #111111; border: 1px solid #2a2218;
    border-radius: 12px; padding: 22px 26px; margin-bottom: 14px;
}
.rcard-gold   { border-color: #C9A84C; background: #0f0d08; }
.rcard-safety { border-color: #4ade80; background: #050f08; }
.rcard-amber  { border-color: #f59e0b; background: #0e0b05; }
.rc-head  { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.rc-icon  { font-size: 1.1rem; }
.rc-title { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: #F5F0E8; }
.rc-body  { font-size: 0.87rem; color: #7a6e56; line-height: 1.8; white-space: pre-wrap; }

/* ── GOLD RULE / DIVIDER ─────────────────────────── */
.gold-rule {
    height: 1px; background: linear-gradient(90deg, transparent, #C9A84C, transparent);
    margin: 24px 0; border: none;
}

/* ── DISCLAIMER ──────────────────────────────────── */
.disclaimer {
    background: #0f0d08; border: 1px solid #3a2e10;
    border-left: 3px solid #C9A84C; border-radius: 0 8px 8px 0;
    padding: 14px 18px; color: #6b5e35; font-size: 0.8rem; line-height: 1.65; margin-top: 20px;
}

/* ── STATUS PILL ─────────────────────────────────── */
.status-pill {
    display: inline-block; font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem; letter-spacing: 1px; padding: 2px 8px;
    border-radius: 2px; margin-left: auto;
}
.sp-gold  { background: rgba(201,168,76,0.1); color: #C9A84C; border: 1px solid rgba(201,168,76,0.3); }
.sp-green { background: rgba(74,222,128,0.08); color: #4ade80; border: 1px solid rgba(74,222,128,0.25); }

/* ── SIDEBAR ─────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: #0a0a0a !important;
    border-right: 1px solid #1e1a10 !important;
}
.sb-brand  { font-family: 'Playfair Display', serif; font-size: 1.4rem; font-weight: 900; color: #F5F0E8; }
.sb-brand span { color: #C9A84C; }
.sb-tag    { font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; letter-spacing: 2px; color: #3a3020; margin-top: 3px; }
.sb-sec    { margin-bottom: 22px; }
.sb-sec-hd {
    font-family: 'JetBrains Mono', monospace; font-size: 0.6rem;
    letter-spacing: 2.5px; text-transform: uppercase; color: #2a2218;
    padding-bottom: 7px; border-bottom: 1px solid #1e1a10; margin-bottom: 10px;
}
.sb-row    { display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: #4a4030; padding: 4px 0; }
.sb-dot    { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }
.dot-gold  { background: #C9A84C; }
.dot-green { background: #4ade80; }
.dot-white { background: #9a9080; }

/* ── TABS ────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background: #111111 !important; border-radius: 8px !important;
    border: 1px solid #2a2218 !important; padding: 4px !important; gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    color: #3a3020 !important; font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important; font-size: 0.82rem !important;
    border-radius: 5px !important; padding: 8px 18px !important;
}
.stTabs [aria-selected="true"] { background: #1e1a10 !important; color: #C9A84C !important; }
.stTabs [data-baseweb="tab-panel"] { background: transparent !important; padding: 18px 0 0 !important; }

/* ── SELECTBOX ───────────────────────────────────── */
.stSelectbox > div > div {
    background: #111111 !important; border: 1px solid #2a2218 !important;
    color: #e8e0cc !important; border-radius: 6px !important;
}

/* ── EXPANDER ────────────────────────────────────── */
.streamlit-expanderHeader {
    background: #111111 !important; color: #6b5e40 !important;
    border: 1px solid #2a2218 !important; border-radius: 6px !important;
    font-size: 0.82rem !important;
}

/* ── DOWNLOAD BUTTON ─────────────────────────────── */
.stDownloadButton > button {
    background: transparent !important; color: #C9A84C !important;
    border: 1px solid #C9A84C !important; border-radius: 6px !important;
    font-size: 0.82rem !important;
}
.stDownloadButton > button:hover {
    background: rgba(201,168,76,0.1) !important;
}
</style>
""", unsafe_allow_html=True)


# ── DATA ──────────────────────────────────────────────────────────
QUICK_CASES = {
    "EMERGENCY": {
        "tag": "qc-red",
        "cases": {
            "Cardiac Emergency":      "Severe chest pain radiating to my left arm and jaw, profuse sweating, shortness of breath, nausea. Pain started 20 minutes ago and is getting worse rapidly.",
            "Severe Allergic Reaction": "After eating shrimp I developed hives all over my body, my throat feels tight and is closing, difficulty breathing, tongue swelling. Started 10 minutes ago.",
        }
    },
    "INFECTIONS & ILLNESS": {
        "tag": "qc-gold",
        "cases": {
            "Dengue Fever":       "High fever of 103.5F for 3 days. Severe headache behind eyes. Red rash on arms and torso. Joint and muscle pain. Extreme fatigue. Live in Karachi near mosquito-prone area.",
            "UTI":                "Burning when urinating for 2 days. Frequent urge but little comes out. Pelvic pressure and pain. Urine looks cloudy with strong smell. No fever.",
            "Asthma Attack":      "Chest very tight, wheezing, shortness of breath especially at night. Inhaler not helping much. Persistent cough. Known asthma history.",
        }
    },
    "CHRONIC CONDITIONS": {
        "tag": "qc-white",
        "cases": {
            "Type 2 Diabetes":    "Excessive thirst and urination for 3 weeks. Blurry vision, fatigue, slow healing cut on foot. Weight gain past year. Strong family history of diabetes.",
            "Migraine":           "Throbbing pain on left side of head, nausea, vomiting, light and sound sensitivity. Lasts 4-6 hours. Preceded by zigzag visual patterns.",
        }
    },
    "MENTAL HEALTH": {
        "tag": "qc-green",
        "cases": {
            "Depression & Anxiety": "Feeling hopeless and empty for 2 months. Lost interest in all activities. Sleeping too much or too little. Difficulty concentrating. Constant anxious thoughts.",
            "Drug Interaction":     "I take metformin 500mg, lisinopril 10mg, and aspirin 81mg daily. Want to start ibuprofen for joint pain. Is this safe combination?",
        }
    }
}

AGENTS = [
    ("🩺", "Intake\nExtract"),
    ("📚", "Knowledge\nRAG"),
    ("🔬", "Diagnosis\nAnalysis"),
    ("🛡️",  "Safety\nCheck"),
    ("⚖️",  "Critic\nValidation"),
    ("📋", "Report\nSummary"),
]


# ── SESSION STATE ─────────────────────────────────────────────────
for k, v in [("sym",""), ("results", None), ("emergency", False)]:
    if k not in st.session_state:
        st.session_state[k] = v


# ── SIDEBAR ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:12px 0 28px'>
        <div class='sb-brand'>Medi<span>Agent</span></div>
        <div class='sb-tag'>AI MUSTAQBIL 2.0</div>
    </div>

    <div class='sb-sec'>
        <div class='sb-sec-hd'>System</div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>LangGraph pipeline<span class='status-pill sp-gold' style='margin-left:auto'>ACTIVE</span></div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>FAISS vector store<span class='status-pill sp-gold' style='margin-left:auto'>READY</span></div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>Ollama local LLM<span class='status-pill sp-gold' style='margin-left:auto'>LOCAL</span></div>
        <div class='sb-row'><span class='sb-dot dot-green'></span>6-agent pipeline<span class='status-pill sp-green' style='margin-left:auto'>READY</span></div>
    </div>

    <div class='sb-sec'>
        <div class='sb-sec-hd'>Pipeline</div>
        <div class='sb-row'><span class='sb-dot dot-white'></span>1. Intake — symptom extraction</div>
        <div class='sb-row'><span class='sb-dot dot-white'></span>2. Knowledge — RAG retrieval</div>
        <div class='sb-row'><span class='sb-dot dot-white'></span>3. Diagnosis — clinical analysis</div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>4. Safety — emergency check</div>
        <div class='sb-row'><span class='sb-dot dot-white'></span>5. Critic — validation layer</div>
        <div class='sb-row'><span class='sb-dot dot-green'></span>6. Report — patient summary</div>
    </div>

    <div class='sb-sec'>
        <div class='sb-sec-hd'>Responsible AI</div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>Emergency auto-detection</div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>Drug interaction checks</div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>Mandatory human referral</div>
        <div class='sb-row'><span class='sb-dot dot-gold'></span>Confidence scoring</div>
    </div>
    """, unsafe_allow_html=True)

    model = st.selectbox("Ollama Model", ["llama3.2", "llama3.1", "mistral", "gemma2", "phi3"], index=0)

    # Ollama host — key for Docker networking
    ollama_host = st.text_input(
        "Ollama Host",
        value=os.environ.get("OLLAMA_HOST", "http://host.docker.internal:11434"),
        help="Docker: http://host.docker.internal:11434 | Local: http://localhost:11434"
    )


# ── HERO ──────────────────────────────────────────────────────────
st.markdown("""
<div class='hero'>
    <div class='hero-eyebrow'>AI Mustaqbil 2.0 · Healthcare & Public Health · Multi-Agent System</div>
    <h1 class='hero-title'>Medi<span>Agent</span></h1>
    <p class='hero-sub'>Six specialized AI agents collaborate in sequence — powered entirely by your local Ollama model. Zero API cost. Zero data leaves your machine.</p>
    <div class='badge-row'>
        <span class='badge b-gold'>6-AGENT PIPELINE</span>
        <span class='badge b-white'>100% LOCAL</span>
        <span class='badge b-green'>SAFETY CHECKED</span>
        <span class='badge b-gold'>RAG ENABLED</span>
        <span class='badge b-white'>DOCKERIZED</span>
        <span class='badge b-green'>RESPONSIBLE AI</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ── PIPELINE TRACKER ──────────────────────────────────────────────
def render_pipeline(active=-1, done=[], em=False):
    html = "<div class='pipeline'>"
    for i, (icon, label) in enumerate(AGENTS):
        is_safety = (i == 3)
        if i in done:
            cls = ("safety-done" if is_safety else "done")
        elif i == active:
            cls = ("safety-active" if is_safety else "active")
        else:
            cls = ""
        html += f"""
        <div class='p-step'>
            <div class='p-icon {cls}'>{icon}</div>
            <div class='p-label {cls}'>{label.replace(chr(10),'<br>')}</div>
        </div>"""
        if i < len(AGENTS) - 1:
            html += "<div class='p-arrow'>›</div>"
    html += "</div>"
    return html

pipe_slot = st.empty()
pipe_slot.markdown(render_pipeline(), unsafe_allow_html=True)


# ── INPUT + QUICK CASES ───────────────────────────────────────────
col_in, col_qt = st.columns([3, 2], gap="medium")

with col_in:
    st.markdown("<div class='input-lbl'>🩺 Describe Your Symptoms</div>", unsafe_allow_html=True)
    st.markdown("<div class='input-sub'>Include duration, severity, and any relevant medical history for best results</div>", unsafe_allow_html=True)

    sym_input = st.text_area(
        "sym", value=st.session_state.sym,
        placeholder="e.g. High fever of 103°F for 3 days, severe headache behind my eyes, red rash spreading on arms and torso, intense body aches...",
        height=155, label_visibility="collapsed"
    )

    c1, c2 = st.columns([4, 1])
    with c1:
        run_btn = st.button("⬥  Analyze Symptoms", use_container_width=True)
    with c2:
        if st.button("Clear", use_container_width=True):
            st.session_state.sym = ""
            st.session_state.results = None
            st.session_state.emergency = False
            st.rerun()

with col_qt:
    st.markdown("""
    <div class='qt-panel'>
        <div class='qt-title'>Quick Test Cases</div>
        <div class='qt-sub'>Click to auto-fill the symptom box</div>
    """, unsafe_allow_html=True)

    for cat, data in QUICK_CASES.items():
        st.markdown(f"<div class='qcat {data['tag']}'>{cat}</div>", unsafe_allow_html=True)
        for name, text in data["cases"].items():
            if st.button(name, key=f"q_{name}", use_container_width=True):
                st.session_state.sym = text
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ── RUN PIPELINE ──────────────────────────────────────────────────
if run_btn and sym_input.strip():
    try:
        from langchain_ollama import ChatOllama
        import pipeline as pipe_mod

        base_url = ollama_host.rstrip("/")
        pipe_mod.llm = ChatOllama(model=model, temperature=0.2, base_url=base_url)
    except Exception as e:
        st.error(f"Pipeline load error: {e}")
        st.stop()

    status_slot = st.empty()
    done_steps, em_flag = [], False

    state = {
        "patient_input": sym_input,
        "extracted_symptoms": "", "retrieved_context": "",
        "diagnosis": "", "safety_check": "", "is_emergency": False,
        "validated_diagnosis": "", "final_report": ""
    }

    steps = [
        ("intake_agent",    0, "Intake"),
        ("knowledge_agent", 1, "Knowledge"),
        ("diagnosis_agent", 2, "Diagnosis"),
        ("safety_agent",    3, "Safety"),
        ("critic_agent",    4, "Critic"),
        ("report_agent",    5, "Report"),
    ]

    for fn_name, idx, lbl in steps:
        pipe_slot.markdown(render_pipeline(active=idx, done=done_steps, em=em_flag), unsafe_allow_html=True)
        status_slot.markdown(
            f"<p style='font-family:JetBrains Mono,monospace;font-size:0.78rem;color:#C9A84C;margin-top:6px'>"
            f"▶ Agent {idx+1} / 6 — {lbl} running...</p>",
            unsafe_allow_html=True
        )
        fn = getattr(pipe_mod, fn_name, None)
        if fn is None:
            st.warning(f"{fn_name} not found in pipeline.py — skipping.")
            done_steps.append(idx)
            continue
        try:
            state = fn(state)
        except Exception as e:
            st.error(f"Agent {lbl} error: {e}")
            st.stop()

        done_steps.append(idx)
        if fn_name == "safety_agent" and state.get("is_emergency"):
            em_flag = True
        time.sleep(0.04)

    pipe_slot.markdown(render_pipeline(active=-1, done=done_steps, em=em_flag), unsafe_allow_html=True)
    status_slot.markdown(
        "<p style='font-family:JetBrains Mono,monospace;font-size:0.78rem;color:#4ade80;margin-top:6px'>"
        "✓ All 6 agents completed successfully</p>",
        unsafe_allow_html=True
    )
    st.session_state.results = state
    st.session_state.emergency = em_flag

elif run_btn:
    st.warning("Please enter symptoms before analyzing.")


# ── RESULTS ───────────────────────────────────────────────────────
if st.session_state.results:
    s = st.session_state.results
    st.markdown("<hr class='gold-rule'>", unsafe_allow_html=True)

    if st.session_state.emergency:
        st.markdown("""
        <div class='emergency'>
            <div class='em-title'>🚨 EMERGENCY DETECTED — CALL EMERGENCY SERVICES NOW</div>
            <div class='em-body'>
                The Safety Agent identified potentially life-threatening symptoms.<br>
                <strong>Call 1122 (Pakistan) or your local emergency number immediately.</strong>
                Do not rely on this AI system for emergency decisions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋  Final Report", "🔬  Detailed Analysis", "🗂  Raw Agent Outputs"])

    with tab1:
        st.markdown(f"""
        <div class='rcard rcard-gold'>
            <div class='rc-head'><span class='rc-icon'>📋</span><span class='rc-title'>Patient Report</span></div>
            <div class='rc-body'>{s.get('final_report','No report generated.')}</div>
        </div>
        """, unsafe_allow_html=True)
        c1, _ = st.columns([1, 2])
        with c1:
            st.download_button(
                "⬇  Download Report (.txt)",
                data=s.get("final_report", ""),
                file_name="mediagent_report.txt",
                mime="text/plain",
                use_container_width=True
            )

    with tab2:
        st.markdown(f"""
        <div class='rcard'>
            <div class='rc-head'><span class='rc-icon'>🩺</span><span class='rc-title'>Extracted Symptoms</span></div>
            <div class='rc-body'>{s.get('extracted_symptoms','')}</div>
        </div>
        <div class='rcard'>
            <div class='rc-head'><span class='rc-icon'>🔬</span><span class='rc-title'>Clinical Diagnosis</span></div>
            <div class='rc-body'>{s.get('diagnosis','')}</div>
        </div>
        <div class='rcard rcard-amber'>
            <div class='rc-head'><span class='rc-icon'>🛡️</span><span class='rc-title'>Safety Assessment</span></div>
            <div class='rc-body'>{s.get('safety_check','')}</div>
        </div>
        <div class='rcard rcard-safety'>
            <div class='rc-head'><span class='rc-icon'>⚖️</span><span class='rc-title'>Critic Validation</span></div>
            <div class='rc-body'>{s.get('validated_diagnosis','')}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        for title, key in [
            ("📚 RAG Knowledge Context", "retrieved_context"),
            ("🩺 Raw Intake Output",      "extracted_symptoms"),
            ("🔬 Raw Diagnosis Output",   "diagnosis"),
            ("🛡️ Raw Safety Output",      "safety_check"),
            ("⚖️ Raw Critic Output",      "validated_diagnosis"),
        ]:
            with st.expander(title):
                st.code(s.get(key, ""), language="markdown")

    st.markdown("""
    <div class='disclaimer'>
        <strong>⚠ Medical Disclaimer —</strong> MediAgent is an AI prototype developed for AI Mustaqbil 2.0.
        It is for educational and demonstration purposes only and does not constitute medical advice,
        diagnosis, or treatment. Always consult a licensed physician before taking any medical action.
        In an emergency, call <strong>1122</strong> (Pakistan) or your local emergency services immediately.
    </div>
    """, unsafe_allow_html=True)
