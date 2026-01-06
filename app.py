import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import uuid
import io

# --- AMBIENTE E CONFIGURAÇÃO ---
st.set_page_config(
    page_title="Strawberry Logic Studio Ultra",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS ENGINE (UI REFORÇADA) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Fira+Code:wght@400;500&display=swap');

    .stApp {
        background: linear-gradient(rgba(157, 109, 132, 0.95), rgba(157, 109, 132, 0.95)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Container de Proteção do Layout */
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
        min-height: 520px;
        display: flex;
        flex-direction: column;
        box-shadow: inset 0 0 20px rgba(255,182,193,0.3);
    }

    /* Inputs e Botões */
    .stTextInput input {
        background-color: white !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 20px !important;
        height: 60px !important;
        font-weight: 600 !important;
        color: #8b4367 !important;
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
    }

    .stButton button:active {
        transform: translateY(6px);
        box-shadow: 0 2px 0px #ffb6c1 !important;
    }

    /* Wave Animation */
    .wave-stage {
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
        animation: floating 3.5s ease-in-out infinite;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));
    }

    @keyframes floating {
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

    .terminal-output {
        background: #1a0f14;
        color: #ffb6c1;
        font-family: 'Fira Code', monospace;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #ff69b4;
        font-size: 0.9rem;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- ENGINE TÉCNICA (AUDITORIA FORENSE) ---
class SiliconCore:
    def __init__(self, vcc=3.3):
        self.vcc = vcc
        self.vih = vcc * 0.7
        self.vil = vcc * 0.3

    def get_logic_state(self, voltage):
        if voltage >= self.vih: return 1
        if voltage <= self.vil: return 0
        return -1 # Undefined

    def compute_matrix(self, a, b):
        a_i, b_i = int(a), int(b)
        return {
            "AND": (a_i & b_i) & 1,
            "OR": (a_i | b_i) & 1,
            "XOR": (a_i ^ b_i) & 1,
            "NAND": (~(a_i & b_i)) & 1,
            "NOR": (~(a_i | b_i)) & 1,
            "XNOR": (~(a_i ^ b_i)) & 1
        }

    def simulate_thermal(self):
        return np.random.uniform(32.0, 38.5)

# --- SESSÃO E PERSISTÊNCIA ---
if 'log_buffer' not in st.session_state:
    st.session_state.log_buffer = []
if 'boot_ts' not in st.session_state:
    st.session_state.boot_ts = time.time()

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: white; font-size: 4rem; text-shadow: 6px 6px 0px #ff69b4;'>⊹ ˖ Silicon Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown('<div class="main-shell"></div>', unsafe_allow_html=True)
        st.markdown("<h2 style='color: white;'>× × Secure Login 🍓</h2>", unsafe_allow_html=True)
        st.markdown('<div class="glass-box">', unsafe_allow_html=True)
        st.text_input("Engineer Email", value="dev@strawberry.io")
        st.text_input("Access Token", type="password", value="ST-PRO-2026")
        if st.button("Initialize Logic Sequence"):
            st.toast("Kernel Sync OK", icon="🍓")
        st.markdown("<div style='flex-grow:1'></div>", unsafe_allow_html=True)
        st.caption("Protocol: Bitwise Simulation v5.2")
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown('<div class="main-shell"></div>', unsafe_allow_html=True)
        st.markdown("<h2 style='color: white;'>× × Data Wave 🍓</h2>", unsafe_allow_html=True)
        st.markdown('<div class="glass-box" style="padding: 15px;">', unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="berry-icon">🍓</div>
                <div style="position: absolute; bottom: 35px; text-align: center; color: white; z-index: 10;">
                    <b style="font-size: 1.4rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">Pulse: STREAMING</b><br>
                    <span style="font-size: 0.8rem; opacity: 0.9; font-family: 'Fira Code';">Heghe: 190 mΩ | 16s backout infinite</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- RAIL DE CONTROLE ---
st.markdown("<br><h2 style='color: white; text-align: center;'>Physical Layer Controls</h2>", unsafe_allow_html=True)
r1, r2, r3 = st.columns([1, 1, 1])
v_rail = r1.select_slider("System VCC", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
volts_a = r2.slider("Line A (Volts)", 0.0, v_rail, v_rail)
volts_b = r3.slider("Line B (Volts)", 0.0, v_rail, 0.0)

# PROCESSAMENTO
engine = SiliconCore(v_rail)
bit_a, bit_b = engine.get_logic_state(volts_a), engine.get_logic_state(volts_b)

if bit_a == -1 or bit_b == -1:
    st.error("Noise Margin Violation: Undefined State Detected")
    results = engine.compute_matrix(0, 0)
else:
    results = engine.compute_matrix(bit_a, bit_b)

# LOGGING
st.session_state.log_buffer.append({**results, "timestamp": datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]})
if len(st.session_state.log_buffer) > 50: st.session_state.log_buffer.pop(0)

# GRID DE SAÍDA
st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
for gate, val in results.items():
    st.markdown(f"""
        <div class="gate-card">
            <div class="gate-name">{gate}</div>
            <div class="gate-out">({val})</div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ANALYTICS TABS
st.markdown("<br>", unsafe_allow_html=True)
t1, t2 = st.tabs(["📟 System Terminal", "📊 Forensic Data"])

with t1:
    uptime = int(time.time() - st.session_state.boot_ts)
    st.markdown(f"""
    <div class="terminal-output">
        $ strawberry_kernel --verbose<br>
        > RAIL_VCC: {v_rail}V | VIH_MIN: {engine.vih:.2f}V | VIL_MAX: {engine.vil:.2f}V<br>
        > PROBE_A: {volts_a}V (Logic {bit_a}) | PROBE_B: {volts_b}V (Logic {bit_b})<br>
        > THERMAL_SENSORS: {engine.simulate_thermal():.2f}°C<br>
        > SYSTEM_UPTIME: {uptime}s<br>
        > LISTENING_FOR_TRANSITIONS...
    </div>
    """, unsafe_allow_html=True)

with t2:
    if st.session_state.log_buffer:
        df = pd.DataFrame(st.session_state.log_buffer)
        st.dataframe(df.tail(15), use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Export Signal Log (CSV)", data=csv, file_name="silicon_dump.csv", mime="text/csv")

st.markdown("<p style='text-align: center; color: white; opacity: 0.5; margin-top: 50px;'>st.mowkanel / python-logic-pro-ultra v2.6</p>", unsafe_allow_html=True)
