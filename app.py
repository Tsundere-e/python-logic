import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import uuid
import io

st.set_page_config(
    page_title="Strawberry Logic Studio Pro",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(157, 109, 132, 0.85) !important;
        border-radius: 40px !important;
        padding: 35px !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3) !important;
        margin-bottom: 25px;
    }

    .stTextInput input {
        background-color: white !important;
        border-radius: 20px !important;
        border: none !important;
        height: 55px !important;
        color: #8b4367 !important;
        font-weight: 600 !important;
        padding: 0 20px !important;
    }

    .stButton button {
        background: white !important;
        color: #ff69b4 !important;
        border: none !important;
        border-radius: 30px !important;
        height: 55px !important;
        width: 100% !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 6px 0px rgba(0,0,0,0.1) !important;
        transition: 0.2s ease;
    }

    .stButton button:active {
        transform: translateY(4px);
        box-shadow: 0 2px 0px rgba(0,0,0,0.1) !important;
    }

    .wave-stage {
        height: 350px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: white;
        position: relative;
    }

    .berry-core {
        font-size: 110px;
        animation: float 4s ease-in-out infinite;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.3));
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(-5deg); }
        50% { transform: translateY(-30px) rotate(5deg); }
    }

    .gate-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }

    .gate-card {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        padding: 25px;
        text-align: center;
        backdrop-filter: blur(5px);
    }

    .gate-name { color: #ffb6c1; font-weight: 700; font-size: 1.2rem; }
    .gate-val { color: white; font-size: 2.5rem; font-weight: 900; }

    .terminal-view {
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

class SiliconKernel:
    def __init__(self, vcc=3.3):
        self.vcc = vcc
        self.vih = vcc * 0.7
        self.vil = vcc * 0.3
        self.temp = 32.5

    def read_voltage(self, v):
        if v >= self.vih: return 1
        if v <= self.vil: return 0
        return -1

    def compute_all(self, a, b):
        a_i, b_i = int(a), int(b)
        return {
            "AND": (a_i & b_i) & 1,
            "OR": (a_i | b_i) & 1,
            "XOR": (a_i ^ b_i) & 1,
            "NAND": (~(a_i & b_i)) & 1,
            "NOR": (~(a_i | b_i)) & 1,
            "XNOR": (~(a_i ^ b_i)) & 1
        }

    def get_thermal(self):
        self.temp += np.random.uniform(-0.1, 0.1)
        return self.temp

if 'session_history' not in st.session_state:
    st.session_state.session_history = []
if 'boot_time' not in st.session_state:
    st.session_state.boot_time = time.time()

st.markdown("<h1 style='text-align: center; color: white; font-size: 3.5rem; padding: 20px;'>⊹ ˖ Strawberry Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    with st.container(border=True):
        st.markdown("<h2 style='color: white;'>× × Secure Login 🍓</h2>", unsafe_allow_html=True)
        st.text_input("Engineer Email", value="dev@strawberry.io", key="email")
        st.text_input("Access Token", type="password", value="PRO_KERNEL_2026", key="token")
        if st.button("Initialize Auth Sequence"):
            st.toast("System Authenticated", icon="🍓")
        st.markdown("<br><p style='color: #ffb6c1; font-size: 0.8rem;'>Protocol: Silicon-Level Auth v5.2</p>", unsafe_allow_html=True)

with col_right:
    with st.container(border=True):
        st.markdown("<h2 style='color: white;'>× × Data Wave 🍓</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="berry-core">🍓</div>
                <div style="margin-top: 10px; text-align: center;">
                    <b style="font-size: 1.4rem;">Pulse: STREAMING</b><br>
                    <span style="font-size: 0.8rem; opacity: 0.8; font-family: 'Fira Code';">Heghe: 190 mΩ | 16s backout infinite</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2 style='color: white; text-align: center;'>Physical Logic Rail</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    v_sel = c1.select_slider("VCC (Volts)", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
    v_a = c2.slider("Signal A (V)", 0.0, v_sel, v_sel)
    v_b = c3.slider("Signal B (V)", 0.0, v_sel, 0.0)

    kernel = SiliconKernel(v_sel)
    bit_a = kernel.read_voltage(v_a)
    bit_b = kernel.read_voltage(v_b)

    if bit_a == -1 or bit_b == -1:
        st.error("Noise Margin Violation: Undefined State")
        logic_res = kernel.compute_all(0, 0)
    else:
        logic_res = kernel.compute_all(bit_a, bit_b)

    st.session_state.session_history.append({**logic_res, "ts": datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]})
    if len(st.session_state.session_history) > 50: st.session_state.session_history.pop(0)

    st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
    for g, v in logic_res.items():
        st.markdown(f'<div class="gate-card"><div class="gate-name">{g}</div><div class="gate-val">{v}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
t1, t2 = st.tabs(["📟 System Kernel", "📊 Signal Analytics"])

with t1:
    uptime = int(time.time() - st.session_state.boot_time)
    st.markdown(f"""
    <div class="terminal-view">
        $ strawberry_os --status<br>
        > VCC: {v_sel}V | VIH: {kernel.vih:.2f}V | VIL: {kernel.vil:.2f}V<br>
        > INPUT_A: {v_a}V (Logic {bit_a}) | INPUT_B: {v_b}V (Logic {bit_b})<br>
        > CORE_TEMP: {kernel.get_thermal():.2f}°C<br>
        > UPTIME: {uptime}s | STATE: STABLE
    </div>
    """, unsafe_allow_html=True)

with t2:
    if st.session_state.session_history:
        df = pd.DataFrame(st.session_state.session_history)
        st.dataframe(df.tail(15), use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Export CSV Forensic Log", data=csv, file_name="logic_dump.csv")

st.markdown("<p style='text-align: center; color: white; opacity: 0.5; margin-top: 50px;'>st.mowkanel / python-logic-pro v2.7.0</p>", unsafe_allow_html=True)
