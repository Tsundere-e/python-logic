import streamlit as st
import datetime
import pandas as pd
import time
import io

# --- 1. CONFIGURATION & ENGINE ---
st.set_page_config(
    page_title="Strawberry Logic Studio | Pro",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE ULTIMATE CSS ENGINE (EXACT MATCH) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap');

    /* Global Overlay */
    .stApp {
        background: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* Fixed Card Container (Ref: unnamed (1).jpg) */
    .card-wrapper {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 40px 0;
    }

    .outer-shell {
        background: #9d6d84;
        border-radius: 35px;
        padding: 25px;
        width: 500px;
        height: 600px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        display: flex;
        flex-direction: column;
        border: 1px solid rgba(255,255,255,0.2);
    }

    .shell-header {
        color: white;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
        padding-left: 10px;
    }

    /* THE FIX: Inner Box for Streamlit Widgets */
    .inner-white-box {
        background: #fff0f5;
        border-radius: 25px;
        flex-grow: 1;
        padding: 35px;
        position: relative;
        border: 1px solid rgba(255,182,193,0.5);
        display: block;
    }

    /* Widget Injection Overrides */
    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 15px !important;
        height: 50px !important;
        color: #8b4367 !important;
    }

    .stButton > button {
        background: white !important;
        color: #ff69b4 !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 25px !important;
        width: 100% !important;
        height: 50px !important;
        font-weight: 700 !important;
        margin-top: 10px;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: #ff69b4 !important;
        color: white !important;
        border: 2px solid white !important;
    }

    /* Visual Data Wave Container */
    .wave-display {
        background: linear-gradient(180deg, #ff9a9e 0%, #fecfef 100%);
        border-radius: 20px;
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    }

    .berry-icon {
        font-size: 100px;
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
        animation: float 4s ease-in-out infinite;
        z-index: 5;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-25px) rotate(5deg); }
    }

    /* Metric Styling (Ref: image_6e77b2.jpg) */
    .metric-card {
        background: white;
        border: 5px solid #ff69b4;
        border-radius: 40px;
        padding: 30px;
        text-align: center;
        box-shadow: 8px 8px 0px #ffb6c1;
        min-width: 200px;
    }

    .metric-label { font-size: 1.8rem; color: #8b4367; font-weight: 700; }
    .metric-value { font-size: 2.5rem; color: #ff69b4; font-weight: 700; }

    /* Terminal Styling */
    .terminal {
        background: rgba(45, 27, 36, 0.95);
        color: #ffb6c1;
        font-family: 'Fira Code', monospace;
        padding: 20px;
        border-radius: 20px;
        height: 150px;
        overflow-y: auto;
        border-left: 10px solid #ff69b4;
        font-size: 0.9rem;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIC CONTROLLER CLASS ---
class StrawberryEngine:
    def __init__(self):
        self.state_a = 0
        self.state_b = 0
    
    def compute(self, a, b):
        self.state_a = int(a)
        self.state_b = int(b)
        return {
            "AND": self.state_a & self.state_b,
            "OR": self.state_a | self.state_b,
            "XOR": self.state_a ^ self.state_b,
            "NAND": int(not (self.state_a & self.state_b)),
            "NOR": int(not (self.state_a | self.state_b)),
            "XNOR": int(self.state_a == self.state_b),
            "NOT_A": int(not self.state_a),
            "NOT_B": int(not self.state_b)
        }

# --- 4. SESSION MANAGEMENT ---
if 'engine' not in st.session_state:
    st.session_state.engine = StrawberryEngine()
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Time', 'A', 'B', 'Gate', 'Output'])

def add_log(msg):
    t = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.logs.append(f"> [{t}] {msg}")
    if len(st.session_state.logs) > 5: st.session_state.logs.pop(0)

# --- 5. MAIN INTERFACE ---
def main():
    # Header
    st.markdown("""
        <div style="background: rgba(255,255,255,0.8); padding: 20px; border-radius: 25px; margin-bottom: 30px; border: 2px solid #ffb6c1;">
            <h1 style="margin:0; color: #8b4367;">🍓 Strawberry Logic Studio Ultimate</h1>
            <p style="margin:0; color: #ff69b4; font-weight: 700;">Hardware Simulation Framework v4.1.0</p>
        </div>
    """, unsafe_allow_html=True)

    # Upper Controls
    c_left, c_right = st.columns([2, 3])
    
    with c_left:
        st.markdown('<div style="background:rgba(255,255,255,0.8); padding:20px; border-radius:20px; border:1px solid #ffb6c1;">', unsafe_allow_html=True)
        st.subheader("⊹ ˖ Bus Control ♡⸝⸝")
        s1, s2 = st.columns(2)
        in_a = s1.toggle("Bus A Signal", key="t_a")
        in_b = s2.toggle("Bus B Signal", key="t_b")
        v = st.slider("Voltage (V)", 1.2, 5.0, 3.3)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_right:
        st.markdown('<div style="background:rgba(255,255,255,0.8); padding:20px; border-radius:20px; border:1px solid #ffb6c1;">', unsafe_allow_html=True)
        st.subheader("🖥️ Logic Terminal")
        log_msg = f"SIGNAL CHANGE: A={int(in_a)} B={int(in_b)} @ {v}V"
        if not st.session_state.logs or log_msg not in st.session_state.logs[-1]: add_log(log_msg)
        terminal_html = "<br>".join(st.session_state.logs)
        st.markdown(f'<div class="terminal">{terminal_html}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # EXECUTION
    results = st.session_state.engine.compute(in_a, in_b)

    # --- THE DUAL CARDS SECTION (EXACT REFERENCE) ---
    st.markdown('<div class="card-wrapper">', unsafe_allow_html=True)
    
    # LOGIN CARD
    st.markdown('<div class="outer-shell"><div class="shell-header">× × Secure Login 🍓 ♡⸝⸝</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="inner-white-box">', unsafe_allow_html=True)
        st.text_input("Email", value="user@strawberry.com", key="login_email")
        st.text_input("Password", type="password", value="123456", key="login_pass")
        st.markdown('<p style="font-size: 0.8rem; color: #ff69b4; text-align: right; cursor: pointer;">Forget Password?</p>', unsafe_allow_html=True)
        if st.button("Log In"): st.balloons()
        st.markdown('<p style="text-align: center; font-size: 0.8rem; margin-top: 40px; color: #8b4367;">Don\'t have an account? <span style="color: #ff69b4; text-decoration: underline;">Register</span></p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # DATA WAVE CARD
    st.markdown('<div class="outer-shell"><div class="shell-header">× × Strawberry Data Wave 🍓 ♡⸝⸝</div>', unsafe_allow_html=True)
    st.markdown('<div class="inner-white-box" style="padding: 15px;">', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="wave-display">
            <div class="berry-icon">🍓</div>
            <div style="position: absolute; bottom: 20px; width: 100%; text-align: center; color: white;">
                <div style="font-weight: 700; font-size: 1.1rem;">Pulse: {"HIGH" if in_a or in_b else "LOW"}</div>
                <div style="font-size: 0.8rem; opacity: 0.8;">Heghe: 190 mΩ | 16s backout infinite</div>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # --- METRIC GRID (Ref: image_6e77b2.jpg) ---
    st.markdown("<br><h2 style='text-align: center; color: white; text-shadow: 2px 2px #ff69b4;'>⊹ ˖ Digital Matrix ♡⸝⸝</h2>", unsafe_allow_html=True)
    
    row1_1, row1_2, row1_3, row1_4 = st.columns(4)
    with row1_1: st.markdown(f'<div class="metric-card"><div class="metric-label">AND</div><div class="metric-value">({results["AND"]})</div></div>', unsafe_allow_html=True)
    with row1_2: st.markdown(f'<div class="metric-card"><div class="metric-label">OR</div><div class="metric-value">({results["OR"]})</div></div>', unsafe_allow_html=True)
    with row1_3: st.markdown(f'<div class="metric-card"><div class="metric-label">XOR</div><div class="metric-value">({results["XOR"]})</div></div>', unsafe_allow_html=True)
    with row1_4: st.markdown(f'<div class="metric-card"><div class="metric-label">NAND</div><div class="metric-value">({results["NAND"]})</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    row2_1, row2_2, row2_3, row2_4 = st.columns(4)
    with row2_1: st.markdown(f'<div class="metric-card"><div class="metric-label">NOR</div><div class="metric-value">({results["NOR"]})</div></div>', unsafe_allow_html=True)
    with row2_2: st.markdown(f'<div class="metric-card"><div class="metric-label">XNOR</div><div class="metric-value">({results["XNOR"]})</div></div>', unsafe_allow_html=True)
    with row2_3: st.markdown(f'<div class="metric-card"><div class="metric-label">NOT A</div><div class="metric-value">({results["NOT_A"]})</div></div>', unsafe_allow_html=True)
    with row2_4: st.markdown(f'<div class="metric-card"><div class="metric-label">NOT B</div><div class="metric-value">({results["NOT_B"]})</div></div>', unsafe_allow_html=True)

    # Data Export Logic
    new_data = {'Time': datetime.datetime.now().strftime("%H:%M:%S"), 'A': int(in_a), 'B': int(in_b), 'Gate': 'ALL', 'Output': str(results)}
    st.session_state.history = pd.concat([st.session_state.history, pd.DataFrame([new_data])], ignore_index=True)
    
    st.divider()
    with st.expander("📊 Advanced Analytics & Debugger"):
        st.dataframe(st.session_state.history.tail(10), use_container_width=True)
        csv = st.session_state.history.to_csv(index=False).encode('utf-8')
        st.download_button("Download Logic Report", data=csv, file_name="strawberry_report.csv", mime="text/csv")

    st.markdown("<p style='text-align: center; color: white; opacity: 0.6; padding: 40px;'>st.mowkanel / python-logic • Professional Build • 2026</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Kisses
