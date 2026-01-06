import streamlit as st
import datetime
import pandas as pd
import time
import io

# --- 1. GLOBAL SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Strawberry Logic Studio | Pro Edition",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ADVANCED CSS UI/UX ENGINE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap');

    .stApp {
        background-image: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    .glass-panel {
        background: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #ffb6c1;
        box-shadow: 0 12px 32px rgba(255, 182, 193, 0.2);
        margin-bottom: 20px;
    }

    .stMarkdown, p, span, label, h1, h2, h3 {
        color: #8b4367 !important;
        font-weight: 700 !important;
    }

    /* Metric Card Customization */
    [data-testid="stMetric"] {
        background: white !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 25px !important;
        padding: 20px !important;
        box-shadow: 6px 6px 0px #ffb6c1 !important;
        text-align: center;
    }

    /* Refined Login Card - Matching unnamed (1).jpg */
    .outer-card {
        background: rgba(139, 67, 103, 0.4);
        padding: 25px;
        border-radius: 35px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(15px);
        height: 520px;
    }

    .inner-login-box {
        background: #fff0f5;
        border-radius: 30px;
        padding: 35px;
        height: 100%;
        border: 1px solid #ffb6c1;
        display: flex;
        flex-direction: column;
        position: relative;
    }

    .strawberry-badge {
        position: absolute;
        top: 15px;
        right: 15px;
        width: 35px;
    }

    .terminal-box {
        background: #2d1b24;
        color: #ffdae0;
        font-family: 'Fira Code', monospace;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #ff69b4;
        font-size: 0.85rem;
        height: 220px;
        overflow-y: auto;
    }

    /* Input styling to match Screenshot_57.png style */
    .stTextInput > div > div > input {
        background: white !important;
        border-radius: 25px !important;
        border: 2px solid #ffb6c1 !important;
        padding: 15px 25px !important;
        color: #8b4367 !important;
        font-weight: 500 !important;
    }

    .stButton > button {
        background: white !important;
        color: #ff69b4 !important;
        border: 2px solid #ff69b4 !important;
        border-radius: 30px !important;
        font-weight: 700 !important;
        width: 100%;
        height: 50px !important;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: #ff69b4 !important;
        color: white !important;
    }

    /* Data Wave Animation Area */
    .wave-container {
        background: linear-gradient(180deg, #ff9a9e 0%, #fecfef 100%);
        border-radius: 30px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border: 1px solid white;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- 3. BACKEND LOGIC CORE ---
class LogicController:
    def __init__(self):
        self.operations = {
            "AND": lambda a, b: a & b,
            "OR": lambda a, b: a | b,
            "XOR": lambda a, b: a ^ b,
            "NAND": lambda a, b: int(not (a & b)),
            "NOR": lambda a, b: int(not (a | b)),
            "XNOR": lambda a, b: int(a == b)
        }

    def process_signals(self, a, b):
        results = {name: op(a, b) for name, op in self.operations.items()}
        results["NOT_A"], results["NOT_B"] = int(not a), int(not b)
        return results

# --- 4. STATE AND DATA MANAGEMENT ---
def initialize_session():
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = [f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Core Initialized."]
    if 'history_db' not in st.session_state:
        st.session_state.history_db = pd.DataFrame(columns=['Timestamp', 'A', 'B', 'AND', 'OR', 'XOR'])

def log_event(msg):
    ts = datetime.datetime.now().strftime('%H:%M:%S')
    st.session_state.system_logs.append(f"[{ts}] {msg}")
    if len(st.session_state.system_logs) > 8: st.session_state.system_logs.pop(0)

# --- 5. MAIN APPLICATION INTERFACE ---
def main():
    initialize_session()
    logic_unit = LogicController()

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    h1, h2 = st.columns([1, 4])
    with h1: st.image("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/Gemini_Generated_Image_pt31c1pt31c1pt31.jpg", width=140)
    with h2:
        st.title("🍓 Strawberry Logic Studio Ultimate")
        st.write("#### Professional Digital Integrated Circuit Simulator v4.0")
    st.markdown('</div>', unsafe_allow_html=True)

    lp, rp = st.columns([2, 3])
    with lp:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("⊹ ˖ Signal Control ♡⸝⸝")
        csw1, csw2 = st.columns(2)
        with csw1: sig_a = st.toggle("Primary Bus A", key="ba")
        with csw2: sig_b = st.toggle("Primary Bus B", key="bb")
        bit_a, bit_b = int(sig_a), int(sig_b)
        st.divider()
        volt = st.slider("Simulated Voltage (V)", 1.8, 5.0, 3.3)
        if st.button("Clear History"):
            st.session_state.history_db = st.session_state.history_db.iloc[0:0]
            log_event("Purged system history.")
        st.markdown('</div>', unsafe_allow_html=True)

    with rp:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("🖥️ Hardware Execution Logs")
        cur_log = f"SIGNAL: A={bit_a}, B={bit_b} (V={volt}V)"
        if st.session_state.system_logs[-1][11:] != cur_log: log_event(cur_log)
        logs = "<br>".join(st.session_state.system_logs)
        st.markdown(f'<div class="terminal-box">{logs}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    res = logic_unit.process_signals(bit_a, bit_b)

    # --- SHOWCASE ROW: LOGIN & DATA WAVE ---
    st.markdown('<div class="glass-panel" style="background: transparent; box-shadow: none; border: none;">', unsafe_allow_html=True)
    col_l, col_r = st.columns([1, 1], gap="large")

    with col_l:
        st.markdown(f'''
            <div class="outer-card">
                <div class="inner-login-box">
                    <img src="https://raw.githubusercontent.com/Tsundere-e/python-logic/main/strawberry_icon_small.png" class="strawberry-badge">
                    <h2 style="color: #8b4367; margin-bottom: 5px;">× × Secure Login 🍓 ♡⸝⸝</h2>
                    <p style="font-size: 0.9rem; color: #8b4367; opacity: 0.7; margin-bottom: 25px;">Enter your credentials</p>
        ''', unsafe_allow_html=True)
        st.text_input("Email", placeholder="user@strawberry.com", label_visibility="visible", key="ui_m")
        st.text_input("Password", type="password", placeholder="••••••••", label_visibility="visible", key="ui_p")
        st.markdown('<p style="text-align: right; font-size: 0.8rem; color: #ff69b4; cursor: pointer;">Forget Password?</p>', unsafe_allow_html=True)
        if st.button("Log In", key="login_trigger"): st.balloons()
        st.markdown('<p style="text-align: center; margin-top: auto; color: #8b4367;">Don\'t have an account? <span style="color: #ff69b4; text-decoration: underline; cursor: pointer;">Register</span></p></div></div>', unsafe_allow_html=True)

    with col_r:
        st.markdown('''
            <div class="outer-card">
                <div class="inner-login-box" style="padding: 0; overflow: hidden; background: transparent;">
                    <div style="padding: 25px; position: absolute; z-index: 2;">
                        <h2 style="color: white !important;">× × Strawberry Wave 🍓 ♡⸝⸝</h2>
                    </div>
                    <div class="wave-container">
                        <img src="https://raw.githubusercontent.com/Tsundere-e/python-logic/main/wave_strawberry.png" style="width: 80%; filter: drop-shadow(0 0 20px white);">
                    </div>
                    <div style="position: absolute; bottom: 20px; width: 100%; text-align: center; color: white; font-weight: bold;">
                        Real-time Pulse: ACTIVE
                    </div>
                </div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- METRICS ---
    st.subheader("⊹ ˖ Digital Output Matrix ♡⸝⸝")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AND GATE", res["AND"])
    m2.metric("OR GATE", res["OR"])
    m3.metric("XOR GATE", res["XOR"])
    m4.metric("NOT A", res["NOT_A"])

    st.divider()
    with st.expander("📊 System Analytics & Data Export"):
        st.dataframe(st.session_state.history_db, use_container_width=True)
        st.download_button("Export Session CSV", "Data...", "logic.csv")

    st.markdown("<p style='text-align: center; opacity: 0.5;'>Strawberry Logic Engine v4.0.0 | High-Fidelity UI Build</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
