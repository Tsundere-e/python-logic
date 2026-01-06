import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import base64

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
        background: linear-gradient(rgba(84, 55, 71, 0.85), rgba(84, 55, 71, 0.85)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(157, 109, 132, 0.6) !important;
        border-radius: 35px !important;
        padding: 30px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 20px 50px rgba(0,0,0,0.3) !important;
        margin-bottom: 25px;
    }

    .stTextInput input {
        background-color: #fff !important;
        border-radius: 12px !important;
        border: none !important;
        height: 45px !important;
        color: #8b4367 !important;
        font-weight: 600 !important;
    }

    .stButton button {
        background: #fff !important;
        color: #ff69b4 !important;
        border: none !important;
        border-radius: 20px !important;
        height: 48px !important;
        width: 140px !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 0px rgba(0,0,0,0.1) !important;
        transition: 0.3s;
    }

    .stButton button:hover {
        transform: scale(1.02);
    }

    .wave-stage {
        height: 320px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 25px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }

    .wave-anim {
        position: absolute;
        width: 250%;
        height: 250%;
        background-image: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/wave.png");
        background-size: cover;
        opacity: 0.35;
        animation: waveLoop 12s linear infinite;
        z-index: 1;
    }

    @keyframes waveLoop {
        from { transform: translate(-25%, -25%) rotate(0deg); }
        to { transform: translate(-25%, -25%) rotate(360deg); }
    }

    .berry-icon {
        font-size: 100px;
        z-index: 10;
        animation: floatBerry 4s ease-in-out infinite;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.3));
    }

    @keyframes floatBerry {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-20px) scale(1.05); }
    }

    .gate-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 15px;
        margin-top: 25px;
    }

    .gate-card {
        background: rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    .gate-label { color: #ffb6c1; font-weight: 700; font-size: 1rem; }
    .gate-state { color: #fff; font-size: 2.5rem; font-weight: 900; }

    .terminal-output {
        background: #120a0e;
        color: #ffb6c1;
        font-family: 'Fira Code', monospace;
        padding: 20px;
        border-radius: 15px;
        font-size: 0.85rem;
        border-left: 5px solid #ff69b4;
    }

    .stSlider > div > div > div > div {
        background: #ffb6c1 !important;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

class SiliconEngine:
    def __init__(self, voltage_rail):
        self.vcc = voltage_rail
        self.vih = voltage_rail * 0.75
        self.vil = voltage_rail * 0.25
        self.resistance = 190.0
    
    def get_logic(self, volt):
        if volt >= self.vih: return 1
        if volt <= self.vil: return 0
        return -1

    def solve(self, a, b):
        ai, bi = int(a), int(b)
        return {
            "AND": ai & bi,
            "OR": ai | bi,
            "XOR": ai ^ bi,
            "NAND": int(not (ai & bi)),
            "NOR": int(not (ai | bi)),
            "XNOR": int(not (ai ^ bi)),
            "BUFF A": ai,
            "BUFF B": bi,
            "NOT A": int(not ai),
            "NOT B": int(not bi)
        }

if 'signal_logs' not in st.session_state:
    st.session_state.signal_logs = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()

st.markdown("<h1 style='text-align: center; color: white; font-size: 3.2rem; margin-bottom: 30px;'>⊹ ˖ Strawberry Studio Pro ♡⸝⸝</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Secure Login 🍓</h3>", unsafe_allow_html=True)
        st.text_input("User Email", value="engineer@strawberryrd.com", key="login_mail")
        st.text_input("Access Key", type="password", value="logic_high_3.3", key="login_pass")
        if st.button("Initialize Auth"):
            st.toast("System Online", icon="🍓")
        st.markdown("<p style='color: #ffb6c1; font-size: 0.85rem; margin-top: 15px; text-align: center;'>Don't have an account? <span style='text-decoration: underline;'>Register</span></p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Strawberry Data Wave 🍓</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-stage">
                <div class="wave-anim"></div>
                <div class="berry-icon">🍓</div>
                <div style="z-index: 10; text-align: center; color: white; margin-top: 15px;">
                    <b style="font-size: 1.1rem; letter-spacing: 1px;">Pulse: STREAMING</b><br>
                    <span style="font-size: 0.75rem; opacity: 0.8; font-family: 'Fira Code';">Heghe: 190 mΩ | 16s backout infinite style</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<h3 style='color: white; text-align: center; margin-bottom: 25px;'>× × Bus Control Center × ×</h3>", unsafe_allow_html=True)
    vcc_val = st.select_slider("System VCC Rail (Voltage Selection)", options=[1.2, 1.8, 3.3, 5.0, 12.0], value=3.3)
    
    col_bus_a, col_bus_b = st.columns(2)
    bus_a_v = col_bus_a.slider("Bus A Signal Injection (Volts)", 0.0, vcc_val, vcc_val)
    bus_b_v = col_bus_b.slider("Bus B Signal Injection (Volts)", 0.0, vcc_val, 0.0)
    
    engine = SiliconEngine(vcc_val)
    logic_a = engine.get_logic(bus_a_v)
    logic_b = engine.get_logic(bus_b_v)
    
    if logic_a == -1 or logic_b == -1:
        st.warning("Signal Floating: Logic State Undefined (High Impedance Detection)")
        bit_a, bit_b = 0, 0
    else:
        bit_a, bit_b = logic_a, logic_b

    matrix = engine.solve(bit_a, bit_b)
    
    log_entry = {
        **matrix, 
        "VCC": vcc_val, 
        "Volt_A": bus_a_v, 
        "Volt_B": bus_b_v, 
        "Timestamp": datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    }
    st.session_state.signal_logs.append(log_entry)
    
    if len(st.session_state.signal_logs) > 100:
        st.session_state.signal_logs.pop(0)

    st.markdown('<div class="gate-grid">', unsafe_allow_html=True)
    for gate, state in matrix.items():
        st.markdown(f"""
            <div class="gate-card">
                <div class="gate-label">{gate}</div>
                <div class="gate-state">{state}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
t_core, t_log, t_phys = st.tabs(["📟 Logic Kernel", "📊 Signal Dump", "🌡️ Parameters"])

with t_core:
    up_time = int(time.time() - st.session_state.session_start)
    st.markdown(f"""
    <div class="terminal-output">
        $ strawberry_os --analyze --verbose --kernel_v3.2<br>
        > RAIL_VOLTAGE_DETECTED: {vcc_val}V | SYSTEM_IMPEDANCE: {engine.resistance} mΩ<br>
        > THRESHOLD_HIGH (VIH): {engine.vih:.2f}V | THRESHOLD_LOW (VIL): {engine.vil:.2f}V<br>
        > SIGNAL_PROBE_A: {bus_a_v}V -> RESOLVED_LOGIC: {logic_a}<br>
        > SIGNAL_PROBE_B: {bus_b_v}V -> RESOLVED_LOGIC: {logic_b}<br>
        > SYSTEM_UPTIME: {up_time}s | KERNEL_STATE: 0x00_STABLE_READY<br>
        > BUFFER_SIZE: {len(st.session_state.signal_logs)}/100 ENTRIES
    </div>
    """, unsafe_allow_html=True)

with t_log:
    if st.session_state.signal_logs:
        df = pd.DataFrame(st.session_state.signal_logs)
        st.dataframe(df.tail(20), use_container_width=True)
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Export Logic Forensics Report (CSV)", csv_data, "logic_forensics_dump.csv", "text/csv")

with t_phys:
    p1, p2, p3 = st.columns(3)
    p1.metric("Rail Stability", "99.8%", "+0.02%", help="System voltage jitter assessment")
    p2.metric("Power Draw", f"{(vcc_val * 0.15):.2f} mW", help="Estimated core power dissipation")
    p3.metric("Junction Temp", "36.2 °C", "Safe", help="Simulated silicon temperature")

st.markdown("<p style='text-align: center; color: white; opacity: 0.4; margin-top: 60px;'>st.mowkanel / python-logic (unsuate-html) v6.6.2 Final Stable</p>", unsafe_allow_html=True)
