import streamlit as st
import datetime
import pandas as pd
import time
import numpy as np
from PIL import Image
import io

# --- 1. SETTING THE STAGE (CORE CONFIG) ---
st.set_page_config(
    page_title="Strawberry Logic Studio | Pro Edition",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE ULTIMATE CSS INJECTION (ADVANCED UI/UX) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap');

    /* Global Body Overrides */
    .stApp {
        background: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* THE MAGIC FIX: This forces Streamlit blocks to respect our custom containers */
    [data-testid="stVerticalBlock"] > div:has(div.inner-white-box) {
        gap: 0 !important;
    }

    /* Card Shell - Based on unnamed (1).jpg */
    .outer-card-shell {
        background: #9d6d84;
        border-radius: 40px;
        padding: 30px;
        width: 100%;
        max-width: 480px;
        min-height: 620px;
        margin: 15px auto;
        display: flex;
        flex-direction: column;
        box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.15);
        transition: transform 0.3s ease;
    }

    .shell-title {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 12px;
        letter-spacing: -0.5px;
    }

    /* Inner Container - THE COMPONENT ANCHOR */
    .inner-white-box {
        background: #fff0f5;
        border-radius: 30px;
        padding: 40px 30px;
        flex-grow: 1;
        border: 2px solid rgba(255,182,193,0.3);
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    /* Input Polishing - Ref: Screenshot_57.png */
    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 20px !important;
        height: 55px !important;
        padding: 0 20px !important;
        color: #8b4367 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(255,182,193,0.1) !important;
    }

    /* Custom Button Design */
    .stButton > button {
        background: white !important;
        color: #ff69b4 !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 30px !important;
        width: 100% !important;
        height: 55px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        margin-top: 20px;
        box-shadow: 0 6px 0px #ffb6c1 !important;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 0px #ffb6c1 !important;
        background: #fffafa !important;
    }

    .stButton > button:active {
        transform: translateY(4px);
        box-shadow: 0 2px 0px #ffb6c1 !important;
    }

    /* Data Wave Graphics Module */
    .wave-display-module {
        background: linear-gradient(180deg, #ff8da1 0%, #ffc0d0 100%);
        border-radius: 25px;
        height: 100%;
        min-height: 380px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
        border: 1px solid white;
    }

    .wave-berry {
        font-size: 110px;
        animation: floating-berry 5s ease-in-out infinite;
        z-index: 10;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));
    }

    @keyframes floating-berry {
        0%, 100% { transform: translateY(0) rotate(-3deg) scale(1); }
        50% { transform: translateY(-35px) rotate(3deg) scale(1.05); }
    }

    /* Metric Grid Evolution - Ref: Screenshot_56.png */
    .logic-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 25px;
        padding: 40px;
    }

    .metric-card-pro {
        background: white;
        border: 6px solid #ffb6c1;
        border-radius: 45px;
        padding: 35px;
        text-align: center;
        box-shadow: 10px 10px 0px #ffb6c1;
        transition: all 0.3s ease;
    }

    .metric-card-pro:hover {
        transform: translate(-5px, -5px);
        box-shadow: 15px 15px 0px #ff69b4;
    }

    .metric-title { font-size: 1.6rem; color: #8b4367; font-weight: 700; margin-bottom: 8px; }
    .metric-val { font-size: 2.8rem; color: #ff69b4; font-weight: 700; }

    /* Hide Default Elements */
    header, footer { visibility: hidden; }
    .stDeployButton { display:none; }
</style>
""", unsafe_allow_html=True)

# --- 3. ADVANCED LOGIC KERNEL ---
class SignalProcessor:
    """Handles deep boolean algebraic calculations for the studio"""
    def __init__(self):
        self.clock_speed = "1.2GHz"
        self.thermal_threshold = 75.0
    
    def analyze(self, a, b):
        """Processes two-bit input streams"""
        bits = [int(a), int(b)]
        return {
            "AND": bits[0] & bits[1],
            "OR": bits[0] | bits[1],
            "XOR": bits[0] ^ bits[1],
            "NAND": int(not (bits[0] & bits[1])),
            "NOR": int(not (bits[0] | bits[1])),
            "XNOR": int(bits[0] == bits[1]),
            "IMP": int(not bits[0] or bits[1]),
            "BUFFER": bits[0]
        }

# --- 4. DATA PIPELINE ---
def initialize_system():
    if 'kernel' not in st.session_state:
        st.session_state.kernel = SignalProcessor()
    if 'telemetry' not in st.session_state:
        st.session_state.telemetry = []
    if 'uptime' not in st.session_state:
        st.session_state.uptime = time.time()

def record_telemetry(data):
    ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    st.session_state.telemetry.append(f"[{ts}] CORE_SIG: {data}")
    if len(st.session_state.telemetry) > 8:
        st.session_state.telemetry.pop(0)

# --- 5. INTERFACE EXECUTION (THE 300 LINE TARGET) ---
def render_app():
    initialize_system()
    
    # Title Branding
    st.markdown("""
        <div style="background: rgba(255,255,255,0.7); padding: 25px; border-radius: 30px; margin-bottom: 40px; border: 2px solid #ffb6c1; backdrop-filter: blur(5px);">
            <div style="display: flex; align-items: center; gap: 20px;">
                <span style="font-size: 50px;">🍓</span>
                <div>
                    <h1 style="color: #8b4367; margin:0; font-size: 2.2rem;">Strawberry Logic Studio | Professional Edition</h1>
                    <p style="color: #ff69b4; font-weight: 700; margin:0; opacity: 0.8;">Integrated Silicon Simulation Environment v4.5.0-LTS</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Control Panel Layout
    ctrl_left, ctrl_right = st.columns([1, 1], gap="large")
    
    with ctrl_left:
        st.markdown('<div style="background:rgba(255,255,255,0.8); padding:25px; border-radius:25px; border:1px solid #ffb6c1;">', unsafe_allow_html=True)
        st.subheader("⊹ ˖ Hardware Bus Configuration ♡⸝⸝")
        sub_c1, sub_c2 = st.columns(2)
        bus_a = sub_c1.toggle("Enable Bus A", help="Toggle primary input A signal")
        bus_b = sub_c2.toggle("Enable Bus B", help="Toggle primary input B signal")
        st.divider()
        v_set = st.select_slider("System Voltage Rail (Vcc)", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
        st.caption(f"Status: Synchronized | Frequency: {st.session_state.kernel.clock_speed}")
        st.markdown('</div>', unsafe_allow_html=True)

    with ctrl_right:
        record_telemetry(f"A={int(bus_a)} B={int(bus_b)} V={v_set}")
        st.markdown('<div style="background:rgba(255,255,255,0.8); padding:25px; border-radius:25px; border:1px solid #ffb6c1; min-height: 195px;">', unsafe_allow_html=True)
        st.subheader("🖥️ Real-time Kernel Logs")
        log_str = "<br>".join(st.session_state.telemetry)
        st.markdown(f'<div style="background:#2d1b24; color:#ffb6c1; padding:20px; border-radius:15px; font-family:\'Fira Code\',monospace; font-size:0.85rem; height:120px; overflow-y:auto; border-left:6px solid #ff69b4;">{log_str}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Compute Logic results
    logic_results = st.session_state.kernel.analyze(bus_a, bus_b)

    # --- DUAL CARD SECTION (THE CROWN JEWEL) ---
    # Using a wrapper to force center alignment
    st.write("") # Spacing
    
    # CSS GRID WRAPPER FOR CARDS
    st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 40px; justify-content: center; padding: 20px 0;">', unsafe_allow_html=True)

    # CARD A: THE LOGIN SIMULATOR
    st.markdown('<div class="outer-card-shell"><div class="shell-title">× × Secure Login Simulator 🍓 ♡⸝⸝</div>', unsafe_allow_html=True)
    # The Inner box is where Streamlit components are actually "injected"
    st.markdown('<div class="inner-white-box">', unsafe_allow_html=True)
    st.text_input("User Access Email", value="developer@strawberry.com", key="ui_email")
    st.text_input("Encryption Key / Password", type="password", value="logic_master_2026", key="ui_pass")
    st.markdown('<p style="text-align: right; font-size: 0.85rem; color: #ff69b4; font-weight: 700; cursor: pointer;">Forgot Keyframe?</p>', unsafe_allow_html=True)
    if st.button("Initialize Auth Sequence", key="ui_btn"):
        st.balloons()
        st.toast("Credentials Validated!", icon="🍓")
    st.markdown('<div style="margin-top: auto; text-align: center; font-size: 0.85rem; color: #8b4367;">New Hardware Detected? <span style="color:#ff69b4; text-decoration:underline; font-weight:700;">Provision Here</span></div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    # CARD B: THE STRAWBERRY WAVE (DATA VIS)
    st.markdown('<div class="outer-card-shell"><div class="shell-title">× × Strawberry Wave 🍓 ♡⸝⸝</div>', unsafe_allow_html=True)
    st.markdown('<div class="inner-white-box" style="padding: 15px;">', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="wave-display-module">
            <div class="wave-berry">🍓</div>
            <div style="position: absolute; bottom: 25px; width: 100%; text-align: center; color: white; z-index: 15;">
                <div style="font-weight: 700; font-size: 1.3rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">Real-time Pulse: {"HIGH" if (bus_a or bus_b) else "LOW"}</div>
                <div style="font-size: 0.8rem; opacity: 0.9; margin-top: 5px;">Heghe: 190 mΩ-190 | 16s backout style infinite</div>
            </div>
            <div style="position: absolute; width: 200%; height: 100px; background: rgba(255,255,255,0.2); bottom: 0; border-radius: 40%; animation: wave-anim 8s linear infinite;"></div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # End card wrapper

    # --- LOGIC MATRIX OUTPUT ---
    st.markdown("<br><h2 style='text-align: center; color: white; text-shadow: 2px 2px 0px #ff69b4; font-size: 2.5rem;'>⊹ ˖ Digital Logic Matrix ♡⸝⸝</h2>", unsafe_allow_html=True)
    
    st.markdown('<div class="logic-grid">', unsafe_allow_html=True)
    
    gates_to_show = ["AND", "OR", "XOR", "NAND", "NOR", "XNOR", "IMP", "BUFFER"]
    for gate in gates_to_show:
        val = logic_results[gate]
        st.markdown(f'''
            <div class="metric-card-pro">
                <div class="metric-title">{gate}</div>
                <div class="metric-val">({val})</div>
            </div>
        ''', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

    # --- TRUTH TABLE MODULE ---
    with st.expander("📊 Detailed Truth Table & Analytical Data"):
        st.subheader("System State Analysis")
        tt_data = {
            "Input A": [0, 0, 1, 1],
            "Input B": [0, 1, 0, 1],
            "AND": [0, 0, 0, 1],
            "OR": [0, 1, 1, 1],
            "XOR": [0, 1, 1, 0]
        }
        df_tt = pd.DataFrame(tt_data)
        st.table(df_tt)
        
        # Download Simulation Data
        csv_buffer = io.StringIO()
        df_tt.to_csv(csv_buffer)
        st.download_button(
            label="Download Logic Report (CSV)",
            data=csv_buffer.getvalue(),
            file_name="strawberry_logic_report.csv",
            mime="text/csv"
        )

    # Footer Branding
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center; color: white; opacity: 0.6; padding-bottom: 50px;">
            st.mowkanel / python-logic-studio-pro<br>
            Build: {datetime.datetime.now().year}.1.06-STABLE | Framework: Streamlit 1.x<br>
            Session Uptime: {int(time.time() - st.session_state.uptime)} seconds
        </div>
    """, unsafe_allow_html=True)

# Main Entry Point
if __name__ == "__main__":
    render_app()

#kisses
