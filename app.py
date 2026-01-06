import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import uuid

# --- CONFIGURAÇÃO DE AMBIENTE ---
st.set_page_config(
    page_title="Strawberry Logic Studio Ultra",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS ENGINE (UI BLINDADA PARA VERSÃO 2026) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Fira+Code:wght@400;500&display=swap');

    .stApp {
        background: linear-gradient(rgba(157, 109, 132, 0.95), rgba(157, 109, 132, 0.95)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* FIX: Seletor universal para as caixas rosas arredondadas */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #9d6d84 !important;
        border-radius: 45px !important;
        padding: 30px !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 25px 50px rgba(0,0,0,0.4) !important;
        margin-bottom: 20px;
    }

    /* Inner Box - Onde ficam os inputs */
    .inner-canvas {
        background: #fff0f5;
        border-radius: 35px;
        padding: 40px;
        border: 2px solid #ffb6c1;
        min-height: 520px;
        display: flex;
        flex-direction: column;
        box-shadow: inset 0 0 15px rgba(255,182,193,0.5);
    }

    /* Inputs Brancos e Arredondados */
    .stTextInput input {
        background-color: white !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 20px !important;
        height: 60px !important;
        font-weight: 600 !important;
        color: #8b4367 !important;
        padding: 0 20px !important;
    }

    /* Botões Profissionais */
    .stButton button {
        background: white !important;
        color: #ff69b4 !important;
        border: 4px solid #ffb6c1 !important;
        border-radius: 35px !important;
        height: 65px !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        box-shadow: 0 8px 0px #ffb6c1 !important;
        transition: 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .stButton button:active {
        transform: translateY(6px);
        box-shadow: 0 2px 0px #ffb6c1 !important;
    }

    /* Estilização da Wave */
    .wave-panel {
        background: linear-gradient(135deg, #ff8da1 0%, #ffc0d0 100%);
        border-radius: 30px;
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border: 2px solid white;
    }

    .berry-icon {
        font-size: 110px;
        animation: floatBerry 3.5s ease-in-out infinite;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));
    }

    @keyframes floatBerry {
        0%, 100% { transform: translateY(0) rotate(-4deg); }
        50% { transform: translateY(-40px) rotate(4deg); }
    }

    /* Grid de Portas Lógicas */
    .gate-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 30px;
        margin-top: 50px;
    }

    .gate-card {
        background: white;
        border: 7px solid #ffb6c1;
        border-radius: 40px;
        padding: 35px;
        text-align: center;
        box-shadow: 12px 12px 0px #ffb6c1;
    }

    .gate-name { font-size: 1.6rem; color: #8b4367; font-weight: 800; }
    .gate-out { font-size: 3.2rem; color: #ff69b4; font-weight: 900; }

    /* Terminal Profissional */
    .terminal-box {
        background: #1a0f14;
        color: #ffb6c1;
        font-family: 'Fira Code', monospace;
        padding: 25px;
        border-radius: 20px;
        border-left: 8px solid #ff69b4;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- HARDWARE ENGINE ---
class SiliconEngine:
    def __init__(self, vcc=3.3):
        self.vcc = vcc
        self.vih = vcc * 0.7
        self.vil = vcc * 0.3

    def get_state(self, v):
        if v >= self.vih: return 1
        if v <= self.vil: return 0
        return -1 # Undefined

    def compute(self, a, b):
        ai, bi = int(a), int(b)
        return {
            "AND": (ai & bi) & 1,
            "OR": (ai | bi) & 1,
            "XOR": (ai ^ bi) & 1,
            "NAND": (~(ai & bi)) & 1,
            "NOR": (~(ai | bi)) & 1,
            "XNOR": (~(ai ^ bi)) & 1
        }

# --- STATE MANAGEMENT ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'boot_time' not in st.session_state:
    st.session_state.boot_time = time.time()

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: white; font-size: 3.8rem; text-shadow: 6px 6px 0px #ff69b4;'>⊹ ˖ Silicon Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

# --- CORPO PRINCIPAL ---
c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("<h2 style='color: white; margin-bottom: 25px;'>× × Secure Login 🍓</h2>", unsafe_allow_html=True)
        st.markdown('<div class="inner-canvas">', unsafe_allow_html=True)
        st.text_input("Engineer Email", value="dev@strawberry.io", key="email")
        st.text_input("Access Password", type="password", value="logic_high", key="pass")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Initialize Logic Sequence"):
            st.toast("Kernel Sync OK", icon="🍓")
        st.markdown("<div style='flex-grow:1'></div>", unsafe_allow_html=True)
        st.caption("Protocol: Bitwise Simulation v5.2")
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown("<h2 style='color: white; margin-bottom: 25px;'>× × Data Wave 🍓</h2>", unsafe_allow_html=True)
        st.markdown('<div class="inner-canvas" style="padding: 15px;">', unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-panel">
                <div class="berry-icon">🍓</div>
                <div style="position: absolute; bottom: 35px; text-align: center; color: white; z-index: 10;">
                    <b style="font-size: 1.4rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">Pulse: STREAMING</b><br>
                    <span style="font-size: 0.8rem; opacity: 0.9; font-family: 'Fira Code';">Heghe: 190 mΩ | 16s backout infinite</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- RAIL DE CONTROLE ---
st.markdown("<br><h2 style='color: white; text-align: center;'>Physical Signal Layer</h2>", unsafe_allow_html=True)
r1, r2, r3 = st.columns([1, 1, 1])
v_rail = r1.select_slider("System VCC", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
va = r2.slider("Line A (Volts)", 0.0, v_rail, v_rail)
vb = r3.slider("Line B (Volts)", 0.0, v_rail, 0.0)

# PROCESSAMENTO
engine = SiliconEngine(v_rail)
bit_a, bit_b = engine.get_state(va), engine.get_state(vb)

if bit_a == -1 or bit_b == -1:
    st.error("Noise Margin Violation: Undefined State")
    results = engine.compute(0, 0)
else:
    results = engine.compute(bit_a, bit_b)

# LOGGING
st.session_state.history.append({**results, "timestamp": datetime.datetime.now()})
if len(st.session_state.history) > 50: st.session_state.history.pop(0)

# GRID DE SAÍDA


[Image of logic gate symbols and truth tables]

st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
for gate, val in results.items():
    st.markdown(f"""
        <div class="gate-card">
            <div class="gate-name">{gate}</div>
            <div class="gate-out">({val})</div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ANALYTICS
st.markdown("<br>", unsafe_allow_html=True)
t1, t2 = st.tabs(["📟 System Terminal", "📊 Forensic Data"])

with t1:
    uptime = int(time.time() - st.session_state.boot_time)
    st.markdown(f"""
    <div class="terminal-box">
        $ strawberry_kernel --verbose<br>
        > RAIL_VCC: {v_rail}V | VIH: {engine.vih:.2f}V | VIL: {engine.vil:.2f}V<br>
        > PROBE_A: {va}V (Logic {bit_a}) | PROBE_B: {vb}V (Logic {bit_b})<br>
        > UPTIME: {uptime}s<br>
        > STATUS: LISTENING_FOR_TRANSITIONS...
    </div>
    """, unsafe_allow_html=True)

with t2:
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df.tail(15), use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Export CSV Report", data=csv, file_name="silicon_dump.csv", mime="text/csv")

st.markdown("<p style='text-align: center; color: white; opacity: 0.5; margin-top: 50px;'>st.mowkanel / logic-pro-ultra v2.6.1</p>", unsafe_allow_html=True)
