import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import base64

st.set_page_config(
    page_title="Tsunderee Logic Studio",
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
        background: rgba(157, 109, 132, 0.65) !important;
        border-radius: 40px !important;
        padding: 35px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 25px 50px rgba(0,0,0,0.4) !important;
        margin-bottom: 25px;
    }

    .stTextInput input {
        background-color: white !important;
        border-radius: 15px !important;
        border: none !important;
        height: 50px !important;
        color: #8b4367 !important;
        font-weight: 600 !important;
        padding: 0 20px !important;
    }

    .stButton button {
        background: white !important;
        color: #ff69b4 !important;
        border: none !important;
        border-radius: 25px !important;
        height: 55px !important;
        width: 100% !important;
        font-weight: 800 !important;
        box-shadow: 0 5px 0px rgba(0,0,0,0.1) !important;
        transition: 0.2s;
    }

    .stButton button:active {
        transform: translateY(3px);
        box-shadow: 0 2px 0px rgba(0,0,0,0.1) !important;
    }

    .wave-stage {
        height: 380px;
        background: rgba(0,0,0,0.25);
        border-radius: 35px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.05);
    }

    .wave-wrapper {
        position: absolute;
        width: 100%; 
        height: 100%;
        z-index: 1;
    }

    .wave-tile {
        width: 100%;
        height: 100%;
        background-image: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/wave.gif");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.6;
        z-index: 1;
    }

    @keyframes waveScroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }

    .berry-core {
        font-size: 120px;
        z-index: 10;
        animation: floatBerry 3.5s ease-in-out infinite;
        filter: drop-shadow(0 20px 30px rgba(0,0,0,0.4));
    }

    @keyframes floatBerry {
        0%, 100% { transform: translateY(0) rotate(-3deg); }
        50% { transform: translateY(-30px) rotate(3deg); }
    }

    .gate-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 15px;
        margin-top: 25px;
    }

    .gate-card {
        background: rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
    }

    .gate-title { color: #ffb6c1; font-weight: 700; font-size: 0.9rem; margin-bottom: 5px; }
    .gate-value { color: white; font-size: 2.2rem; font-weight: 900; }

    .terminal-box {
        background: #120a0e;
        color: #ffb6c1;
        font-family: 'Fira Code', monospace;
        padding: 25px;
        border-radius: 20px;
        font-size: 0.85rem;
        border-left: 6px solid #ff69b4;
    }

    .stSlider > div > div > div > div {
        background: #ffb6c1 !important;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

class SiliconKernel:
    def __init__(self, rail_v):
        self.vcc = rail_v
        self.threshold = rail_v * 0.65
        self.temp = 32.8
    
    def read(self, v):
        return 1 if v >= self.threshold else 0

    def compute(self, a, b):
        return {
            "AND": a & b, "OR": a | b, "XOR": a ^ b,
            "NAND": int(not (a & b)), "NOR": int(not (a | b)),
            "XNOR": int(not (a ^ b)), "NOT A": int(not a), "NOT B": int(not b),
            "BUS A": a, "BUS B": b
        }

if 'log_data' not in st.session_state: st.session_state.log_data = []
if 'session_id' not in st.session_state: st.session_state.session_id = time.time()

st.markdown("<h1 style='text-align: center; color: white; font-size: 3.5rem; margin-bottom: 20px;'>⊹ ˖ Strawberry Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

c_ui, c_wave = st.columns(2)

with c_ui:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Secure Login 🍓</h3>", unsafe_allow_html=True)
        st.text_input("Engineer Email", value="dev@strawberry.com", key="email_field")
        st.text_input("Access Token", type="password", value="Skibidi", key="pass_field")
        if st.button("Initialize Auth Sequence"):
            st.toast("System Online", icon="🍓")
        st.markdown("<p style='color: #ffb6c1; font-size: 0.8rem; margin-top: 15px; text-align: center;'>Heghe: 190 mΩ | 16s backout style</p>", unsafe_allow_html=True)

with c_wave:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Data Wave 🍓</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="wave-wrapper">
                    <div class="wave-tile"></div>
                    <div class="wave-tile"></div>
                </div>
                <div class="berry-core">🍓</div>
                <div style="z-index: 10; text-align: center; color: white; margin-top: 15px;">
                    <b style="font-size: 1.2rem; letter-spacing: 2px;">Pulse: STREAMING</b>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<h3 style='color: white; text-align: center; margin-bottom: 30px;'>× × Physical Rail & Bus Control × ×</h3>", unsafe_allow_html=True)
    vcc_sel = st.select_slider("Select System VCC Rail (Voltage)", options=[1.2, 1.8, 3.3, 5.0, 12.0], value=3.3)
    
    col_a, col_b = st.columns(2)
    bus_a_v = col_a.slider("Bus A Signal Injection (V)", 0.0, vcc_sel, vcc_sel)
    bus_b_v = col_b.slider("Bus B Signal Injection (V)", 0.0, vcc_sel, 0.0)
    
    kernel = SiliconKernel(vcc_sel)
    bit_a = kernel.read(bus_a_v)
    bit_b = kernel.read(bus_b_v)
    
    res_matrix = kernel.compute(bit_a, bit_b)
    
    entry = {**res_matrix, "VCC": vcc_sel, "A_V": bus_a_v, "B_V": bus_b_v, "TS": datetime.datetime.now().strftime("%H:%M:%S")}
    st.session_state.log_data.append(entry)
    if len(st.session_state.log_data) > 100: st.session_state.log_data.pop(0)

    st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
    for g, v in res_matrix.items():
        st.markdown(f'<div class="gate-card"><div class="gate-title">{g}</div><div class="gate-value">{v}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
t_sys, t_data, t_perf = st.tabs(["📟 Terminal", "📊 History", "🌡️ Analytics"])

with t_sys:
    uptime_s = int(time.time() - st.session_state.session_id)
    st.markdown(f"""
    <div class="terminal-box">
        $ strawberry_kernel --status<br>
        > VOLTAGE_RAIL: {vcc_sel}V | THRESHOLD: {kernel.threshold:.2f}V<br>
        > SIGNAL_A: {bus_a_v}V (LOGIC {bit_a}) | SIGNAL_B: {bus_b_v}V (LOGIC {bit_b})<br>
        > UPTIME: {uptime_s}s | KERNEL_TEMP: {kernel.temp:.2f}°C<br>
        > STATUS: STABLE_OPERATIONAL
    </div>
    """, unsafe_allow_html=True)

with t_data:
    if st.session_state.log_data:
        df_logs = pd.DataFrame(st.session_state.log_data)
        st.dataframe(df_logs.tail(20), use_container_width=True)
        st.download_button("Export Data Dump", df_logs.to_csv(index=False).encode('utf-8'), "logic_dump.csv")

with t_perf:
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Rail Stability", "99.98%")
    col_m2.metric("Power Draw", f"{(vcc_sel * 0.12):.2f} mW")
    col_m3.metric("Junction Temp", f"{kernel.temp}°C", "Normal")

st.markdown("<p style='text-align: center; color: white; opacity: 0.4; margin-top: 60px;'>st.mowkanel / strawberry-logic-final-v4.0.0</p>", unsafe_allow_html=True)





