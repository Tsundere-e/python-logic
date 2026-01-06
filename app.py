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
        margin-bottom: 20px;
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
        background: rgba(0,0,0,0.1);
        border-radius: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }

    .wave-anim {
        position: absolute;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent 45%, rgba(255,255,255,0.1) 50%, transparent 55%);
        background-size: 200% 200%;
        animation: waveShift 4s infinite linear;
    }

    @keyframes waveShift {
        0% { background-position: -100% -100%; }
        100% { background-position: 100% 100%; }
    }

    .berry-icon {
        font-size: 110px;
        z-index: 10;
        animation: floatBerry 4s ease-in-out infinite;
        filter: drop-shadow(0 10px 20px rgba(0,0,0,0.2));
    }

    @keyframes floatBerry {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-25px); }
    }

    .gate-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }

    .gate-card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
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

class HardwareCore:
    def __init__(self, vcc):
        self.vcc = vcc
        self.vih = vcc * 0.7
        self.vil = vcc * 0.3
    def process(self, a, b):
        ai, bi = int(a >= self.vih), int(b >= self.vih)
        return {
            "AND": ai & bi,
            "OR": ai | bi,
            "XOR": ai ^ bi,
            "NAND": int(not (ai & bi)),
            "NOR": int(not (ai | bi)),
            "XNOR": int(not (ai ^ bi)),
            "NOT_A": int(not ai),
            "NOT_B": int(not bi)
        }

if 'logs' not in st.session_state: st.session_state.logs = []
if 'start' not in st.session_state: st.session_state.start = time.time()

st.markdown("<h1 style='text-align: center; color: white; font-size: 3rem;'>⊹ ˖ Strawberry Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Secure Login 🍓</h3>", unsafe_allow_html=True)
        st.text_input("Email", value="engineer@strawberry.io")
        st.text_input("Token", type="password", value="L0G1C_2026")
        st.button("Auth Sequence")
        st.markdown("<p style='color: #ffb6c1; font-size: 0.8rem; margin-top: 10px;'>Heghe: 190 mΩ | 16s backout infinite</p>", unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Data Wave 🍓</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="wave-anim"></div>
                <div class="berry-icon">🍓</div>
                <div style="z-index: 10; text-align: center; color: white; margin-top: 10px;">
                    <b style="font-size: 1.2rem;">Pulse: STREAMING</b>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<h3 style='color: white; text-align: center;'>Bus & Rail Control</h3>", unsafe_allow_html=True)
    v_rail = st.select_slider("System Voltage (VCC)", options=[1.2, 1.8, 3.3, 5.0, 12.0], value=3.3)
    col_a, col_b = st.columns(2)
    bus_a = col_a.slider("Bus A Signal (V)", 0.0, v_rail, v_rail)
    bus_b = col_b.slider("Bus B Signal (V)", 0.0, v_rail, 0.0)
    
    hw = HardwareCore(v_rail)
    res = hw.process(bus_a, bus_b)
    
    log_entry = {**res, "VCC": v_rail, "A": bus_a, "B": bus_b, "TS": datetime.datetime.now().strftime("%H:%M:%S")}
    st.session_state.logs.append(log_entry)
    if len(st.session_state.logs) > 100: st.session_state.logs.pop(0)
    
    st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
    for k, v in res.items():
        st.markdown(f'<div class="gate-card"><div style="color: #ffb6c1; font-weight: bold;">{k}</div><div style="color: white; font-size: 2.2rem; font-weight: 900;">{v}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
t1, t2, t3 = st.tabs(["Terminal", "Signal History", "Physical Parameters"])

with t1:
    uptime = int(time.time() - st.session_state.start)
    st.markdown(f"""<div class="terminal-output">
        $ probe_init --vcc {v_rail}V --uptime {uptime}s<br>
        > ANALYZING BUS_A: {bus_a}V (STATUS: {'HIGH' if bus_a >= hw.vih else 'LOW'})<br>
        > ANALYZING BUS_B: {bus_b}V (STATUS: {'HIGH' if bus_b >= hw.vih else 'LOW'})<br>
        > THRESHOLD_DETECTION: VIH={hw.vih:.2f}V / VIL={hw.vil:.2f}V<br>
        > LOGIC_CORE: {len(res)} GATES OPERATIONAL
    </div>""", unsafe_allow_html=True)

with t2:
    if st.session_state.logs:
        df = pd.DataFrame(st.session_state.logs)
        st.dataframe(df.tail(20), use_container_width=True)
        st.download_button("Download Signal Dump", df.to_csv().encode('utf-8'), "signals.csv")

with t3:
    col_p1, col_p2 = st.columns(2)
    col_p1.metric("Operating VCC", f"{v_rail}V")
    col_p1.metric("Input Impedance", "190 mΩ")
    col_p2.metric("Propagation Delay", "12 ns")
    col_p2.metric("Thermal Junction", "34.5 °C")

st.markdown("<p style='text-align: center; color: white; opacity: 0.4; margin-top: 50px;'>st.mowkanel / python-logic-pro-full v3.0</p>", unsafe_allow_html=True)
