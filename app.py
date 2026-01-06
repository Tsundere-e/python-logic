import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time

st.set_page_config(
    page_title="Strawberry Logic Studio",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Fira+Code:wght@400;500&display=swap');

    .stApp {
        background: linear-gradient(rgba(84, 55, 71, 0.9), rgba(84, 55, 71, 0.9)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(157, 109, 132, 0.7) !important;
        border-radius: 40px !important;
        padding: 30px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3) !important;
        margin-bottom: 25px;
    }

    .stTextInput input {
        background-color: white !important;
        border-radius: 15px !important;
        border: none !important;
        height: 48px !important;
        color: #8b4367 !important;
        font-weight: 600 !important;
    }

    .stButton button {
        background: white !important;
        color: #ff69b4 !important;
        border: none !important;
        border-radius: 25px !important;
        height: 50px !important;
        width: 100% !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 0px rgba(0,0,0,0.1) !important;
    }

    .wave-stage {
        height: 350px;
        background: rgba(0,0,0,0.2);
        border-radius: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }

    .wave-container {
        position: absolute;
        width: 200%;
        height: 100%;
        display: flex;
        z-index: 1;
        animation: waveLoop 8s linear infinite;
    }

    .wave-image {
        width: 50%;
        height: 100%;
        background-image: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/wave.png");
        background-size: cover;
        background-repeat: repeat-x;
        opacity: 0.4;
    }

    @keyframes waveLoop {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }

    .berry-icon {
        font-size: 110px;
        z-index: 10;
        animation: floatBerry 4s ease-in-out infinite;
        filter: drop-shadow(0 10px 20px rgba(0,0,0,0.2));
    }

    @keyframes floatBerry {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    .gate-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin-top: 25px;
    }

    .gate-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .terminal-output {
        background: #1a0f14;
        color: #ffb6c1;
        font-family: 'Fira Code', monospace;
        padding: 20px;
        border-radius: 15px;
        font-size: 0.85rem;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

class HardwareKernel:
    def __init__(self, vcc=3.3):
        self.vcc = vcc
        self.vih = vcc * 0.7
        self.vil = vcc * 0.3
    def analyze(self, a, b):
        ba = 1 if a >= self.vih else 0
        bb = 1 if b >= self.vih else 0
        return {
            "AND": ba & bb, "OR": ba | bb, "XOR": ba ^ bb,
            "NAND": int(not(ba & bb)), "NOR": int(not(ba | bb)),
            "XNOR": int(not(ba ^ bb)), "NOT A": int(not ba), "NOT B": int(not bb)
        }

if 'history' not in st.session_state: st.session_state.history = []
if 'boot' not in st.session_state: st.session_state.boot = time.time()

st.markdown("<h1 style='text-align: center; color: white; font-size: 3rem;'>⊹ ˖ Strawberry Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Secure Login 🍓</h3>", unsafe_allow_html=True)
        st.text_input("User Email", value="engineer@strawberry.io")
        st.text_input("Password", type="password", value="logic_high")
        st.button("Access Kernel")
        st.markdown("<p style='color: #ffb6c1; font-size: 0.8rem; margin-top: 10px;'>Pulse: STREAMING | Heghe: 190 mΩ</p>", unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Data Wave 🍓</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="wave-container">
                    <div class="wave-image"></div>
                    <div class="wave-image"></div>
                </div>
                <div class="berry-icon">🍓</div>
                <div style="z-index: 10; text-align: center; color: white; margin-top: 10px;">
                    <b>WAVEFORM: ACTIVE</b>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h3 style='color: white; text-align: center;'>Bus & Signal Control</h3>", unsafe_allow_html=True)
    vcc = st.select_slider("Voltage Rail (VCC)", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
    ca, cb = st.columns(2)
    volts_a = ca.slider("Bus A (V)", 0.0, vcc, vcc)
    volts_b = cb.slider("Bus B (V)", 0.0, vcc, 0.0)
    
    kernel = HardwareKernel(vcc)
    results = kernel.analyze(volts_a, volts_b)
    st.session_state.history.append({**results, "ts": datetime.datetime.now()})
    
    st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
    for gate, val in results.items():
        st.markdown(f'<div class="gate-card"><div style="color: #ffb6c1; font-size: 0.9rem;">{gate}</div><div style="color: white; font-size: 2rem; font-weight: 900;">{val}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
t1, t2 = st.tabs(["Terminal", "Signal Analytics"])
with t1:
    uptime = int(time.time() - st.session_state.boot)
    st.markdown(f"""<div class="terminal-output">
        $ strawberry_probe --vcc {vcc}V<br>
        > INPUT_A: {volts_a}V | INPUT_B: {volts_b}V<br>
        > UPTIME: {uptime}s | TEMP: 32.4°C<br>
        > KERNEL_STATUS: OPERATIONAL
    </div>""", unsafe_allow_html=True)

with t2:
    if st.session_state.history:
        st.dataframe(pd.DataFrame(st.session_state.history).tail(10), use_container_width=True)

st.markdown("<p style='text-align: center; color: white; opacity: 0.5; margin-top: 40px;'>st.mowkanel / python-logic-pro v3.5</p>", unsafe_allow_html=True)
