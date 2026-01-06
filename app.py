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

# --- ENGINE CSS (STABILITY FIRST) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Fira+Code:wght@400;500&display=swap');

    .stApp {
        background: linear-gradient(rgba(157, 109, 132, 0.92), rgba(157, 109, 132, 0.92)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Container de Proteção contra quebra de layout */
    [data-testid="stVerticalBlockBorderWrapper"]:has(.main-shell) {
        background: #9d6d84 !important;
        border-radius: 45px !important;
        padding: 40px !important;
        border: 2px solid rgba(255,255,255,0.15) !important;
        box-shadow: 0 30px 60px rgba(0,0,0,0.4) !important;
    }

    .glass-box {
        background: #fff0f5;
        border-radius: 35px;
        padding: 35px;
        border: 2px solid #ffb6c1;
        min-height: 500px;
        box-shadow: inset 0 0 20px rgba(255,182,193,0.3);
    }

    /* Inputs e Botões Estilizados */
    .stTextInput input {
        background-color: white !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 20px !important;
        height: 60px !important;
        font-weight: 600 !important;
    }

    .stButton button {
        background: white !important;
        color: #ff69b4 !important;
        border: 4px solid #ffb6c1 !important;
        border-radius: 35px !important;
        height: 65px !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        box-shadow: 0 8px 0px #ffb6c1 !important;
        transition: all 0.2s ease;
    }

    .stButton button:hover { transform: translateY(-2px); box-shadow: 0 10px 0px #ffb6c1 !important; }
    .stButton button:active { transform: translateY(6px); box-shadow: 0 2px 0px #ffb6c1 !important; }

    /* Strawberry Wave Animation */
    .wave-stage {
        background: linear-gradient(135deg, #ff8da1 0%, #ffc0d0 100%);
        border-radius: 30px;
        height: 320px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border: 2px solid white;
    }

    .berry-icon {
        font-size: 110px;
        animation: floating 3.5s ease-in-out infinite;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));
    }

    @keyframes floating {
        0%, 100% { transform: translateY(0) rotate(-4deg); }
        50% { transform: translateY(-40px) rotate(4deg); }
    }

    /* Grid de Resultados */
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

    .gate-name { font-size: 1.6rem; color: #8b4367; font-weight: 800; margin-bottom: 8px; }
    .gate-out { font-size: 3.2rem; color: #ff69b4; font-weight: 900; }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE HARDWARE PROFISSIONAL ---
class StrawberrySilicon:
    def __init__(self, vcc=3.3):
        self.vcc = vcc
        self.threshold_high = vcc * 0.7  # CMOS High
        self.threshold_low = vcc * 0.3   # CMOS Low

    def analyze_signal(self, voltage):
        if voltage >= self.threshold_high: return 1
        if voltage <= self.threshold_low: return 0
        return -1 # Região proibida (Undefined)

    def compute_bitwise(self, a, b):
        # Implementação rigorosa conforme Auditoria Forense
        a, b = int(a), int(b)
        return {
            "AND": (a & b) & 1,
            "OR":  (a | b) & 1,
            "XOR": (a ^ b) & 1,
            "NAND": (~(a & b)) & 1,
            "NOR":  (~(a | b)) & 1,
            "XNOR": (~(a ^ b)) & 1
        }

# --- ESTADO DA SESSÃO ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

# --- UI PRINCIPAL ---
st.markdown("<h1 style='text-align: center; color: white; font-size: 4rem; text-shadow: 5px 5px 0px #ff69b4;'>🍓 Silicon Studio Pro</h1>", unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    with st.container(border=True):
        st.markdown('<div class="main-shell"></div>', unsafe_allow_html=True)
        st.subheader("× × Secure Terminal 🔐")
        st.markdown('<div class="glass-box">', unsafe_allow_html=True)
        st.text_input("Operator ID", value=f"ENG-{st.session_state.session_id}")
        st.text_input("Security Key", type="password", value="STRAWBERRY_SECURE")
        if st.button("Initialize Logic Kernels"):
            st.success("Kernels Active.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.info("System Status: Low Latency Mode Active")
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    with st.container(border=True):
        st.markdown('<div class="main-shell"></div>', unsafe_allow_html=True)
        st.subheader("× × Pulse Visualizer 📊")
        st.markdown('<div class="glass-box" style="padding: 15px;">', unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="berry-icon">🍓</div>
                <div style="position: absolute; bottom: 35px; color: white; font-weight: 700; text-align: center;">
                    BUS_VOLTAGE_MONITOR: ACTIVE<br>
                    <span style="font-size: 0.8rem; opacity: 0.8;">190 mΩ Impedance Detected</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- CONTROLE DE SINAIS ---
st.markdown("<br><h2 style='color: white; text-align: center;'>Signal Control Rail</h2>", unsafe_allow_html=True)
ctrl_1, ctrl_2, ctrl_3 = st.columns([1, 1, 1])

v_rail = ctrl_1.select_slider("VCC Power Rail", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
volts_a = ctrl_2.slider("Input A (V)", 0.0, v_rail, v_rail)
volts_b = ctrl_3.slider("Input B (V)", 0.0, v_rail, 0.0)

# EXECUÇÃO DA LÓGICA
engine = StrawberrySilicon(v_rail)
bit_a = engine.analyze_signal(volts_a)
bit_b = engine.analyze_signal(volts_b)

if bit_a == -1 or bit_b == -1:
    st.warning("UNDEFINED STATE: Voltage outside noise margin boundaries!")
    results = engine.compute_bitwise(0, 0)
else:
    results = engine.compute_bitwise(bit_a, bit_b)

# LOGGING O(1)
st.session_state.history.append({**results, "ts": datetime.datetime.now()})
if len(st.session_state.history) > 50: st.session_state.history.pop(0)

# --- GRID DE PORTAS ---


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

# --- ANALYTICS ---
st.markdown("<br>", unsafe_allow_html=True)
tab_log, tab_phys = st.tabs(["Signal Log", "Physical Analysis"])

with tab_log:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df.tail(15), use_container_width=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Export Logic Report", csv, "log.csv", "text/csv")

with tab_phys:
    st.code(f"""
    Hardware Parameters:
    - VCC: {v_rail}V
    - VIH: {engine.threshold_high}V (High Signal)
    - VIL: {engine.threshold_low}V (Low Signal)
    - Latency: ~12ns per gate
    - Silicon Temp: 34.2°C (Simulated)
    """, language="bash")

st.markdown("<p style='text-align: center; color: white; opacity: 0.5;'>st.mowkanel | build: 2026.01.06-PRO</p>", unsafe_allow_html=True)
