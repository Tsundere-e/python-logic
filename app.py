import streamlit as st
import graphviz
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

    /* Main Application Canvas */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* Professional Glassmorphism Layers */
    .glass-panel {
        background: rgba(255, 255, 255, 0.88);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #ffb6c1;
        box-shadow: 0 12px 32px rgba(255, 182, 193, 0.2);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }

    /* High-Contrast Typography */
    .stMarkdown, p, span, label, h1, h2, h3 {
        color: #8b4367 !important;
        font-weight: 700 !important;
    }

    /* Metric Card Enhancements */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 20px !important;
        padding: 15px !important;
        box-shadow: 4px 4px 0px #ffb6c1 !important;
    }

    [data-testid="stMetricValue"] > div {
        color: #ff69b4 !important;
        font-size: 2rem !important;
    }

    /* Hardware Terminal Style */
    .terminal-box {
        background: #1e1e1e;
        color: #ffdae0;
        font-family: 'Fira Code', monospace;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #ff69b4;
        font-size: 0.8rem;
        line-height: 1.5;
        overflow-y: auto;
        height: 200px;
    }

    /* System Toggles */
    .st-emotion-cache-1dj0h35 { background-color: #ff69b4 !important; }
    
    /* Clean UI */
    header, footer { visibility: hidden; }
    .stButton>button {
        border-radius: 12px;
        background-color: #ffb6c1;
        color: white;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BACKEND LOGIC CORE ---
class LogicController:
    """Handles all boolean algebraic computations and system state"""
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
        results["NOT_A"] = int(not a)
        results["NOT_B"] = int(not b)
        return results

# --- 4. STATE AND DATA MANAGEMENT ---
def initialize_session():
    if 'system_logs' not in st.session_state:
        st.session_state.system_logs = [f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Kernel Initialized."]
    if 'history_db' not in st.session_state:
        st.session_state.history_db = pd.DataFrame(columns=['Timestamp', 'A', 'B', 'AND', 'OR', 'XOR'])
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

def log_event(msg):
    ts = datetime.datetime.now().strftime('%H:%M:%S')
    st.session_state.system_logs.append(f"[{ts}] {msg}")
    if len(st.session_state.system_logs) > 8:
        st.session_state.system_logs.pop(0)

# --- 5. MAIN APPLICATION INTERFACE ---
def main():
    initialize_session()
    logic_unit = LogicController()

    # --- TOP BRANDING SECTION ---
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    head1, head2 = st.columns([1, 4])
    with head1:
        st.image("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/Gemini_Generated_Image_pt31c1pt31c1pt31.jpg", width=140)
    with head2:
        st.title("🍓 Strawberry Logic Studio Ultimate")
        st.write("#### Professional Digital Integrated Circuit Simulator v4.0")
        st.caption(f"Hardware Status: Operational | System Time: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- WORKSPACE LAYOUT ---
    left_panel, right_panel = st.columns([2, 3])

    with left_panel:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("⊹ ˖ Signal Control ♡⸝⸝")
        
        col_sw1, col_sw2 = st.columns(2)
        with col_sw1:
            signal_a = st.toggle("Primary Bus A", value=False, help="Toggle Input A Signal")
        with col_sw2:
            signal_b = st.toggle("Primary Bus B", value=False, help="Toggle Input B Signal")
        
        bit_a, bit_b = int(signal_a), int(signal_b)
        
        st.divider()
        st.write("Advanced Parameters")
        voltage = st.slider("Simulated Voltage (V)", 1.8, 5.0, 3.3)
        frequency = st.select_slider("Clock Frequency", options=["1Hz", "10Hz", "100Hz", "1KHz"])
        
        if st.button("Clear System History"):
            st.session_state.history_db = st.session_state.history_db.iloc[0:0]
            log_event("History cleared by user.")
        st.markdown('</div>', unsafe_allow_html=True)

    with right_panel:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("🖥️ Hardware Execution Logs")
        
        # Log Logic
        current_state = f"SIGNAL_FLIP: A={bit_a}, B={bit_b} (V={voltage}V)"
        if not st.session_state.system_logs or st.session_state.system_logs[-1][11:] != current_state:
            log_event(current_state)
            
        logs_html = "<br>".join(st.session_state.system_logs)
        st.markdown(f'<div class="terminal-box">{logs_html}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Core Computation
    results = logic_unit.process_signals(bit_a, bit_b)
    
    # Save to History
    new_entry = pd.DataFrame([{
        'Timestamp': datetime.datetime.now().strftime('%H:%M:%S'),
        'A': bit_a, 'B': bit_b, 
        'AND': results['AND'], 'OR': results['OR'], 'XOR': results['XOR']
    }])
    st.session_state.history_db = pd.concat([st.session_state.history_db, new_entry]).tail(10)

    # --- SHOWCASE ROW: LOGIN & SCHEMATIC ---
    # Posicionado logo após o cálculo dos 'results'
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 1.2])

    with col_l:
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.7); padding: 25px; border-radius: 25px; border: 2px solid #ffb6c1; height: 450px;">
                <h3 style="text-align: center; margin-bottom: 20px;">⊹ ˖ Login Simulator ♡⸝⸝</h3>
        """, unsafe_allow_html=True)
        
        sim_mail = st.text_input("Email", placeholder="user@strawberry.com", key="sim_mail")
        sim_pass = st.text_input("Password", type="password", key="sim_pass")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Log In", use_container_width=True):
            if "@" not in sim_mail or "." not in sim_mail:
                st.error("Invalid email format! 🍓")
            else:
                st.warning("hey! its only for showcase, dont place your sensitive info on random websites!!")
        
        st.markdown("""
                <div style="margin-top: 60px; text-align: center;">
                    <p style="font-size: 0.8rem; opacity: 0.8;">Don't have an account? Register</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.7); padding: 20px; border-radius: 25px; border: 2px solid #ffb6c1; height: 450px; display: flex; flex-direction: column; align-items: center; overflow: hidden;">
                <h3 style="text-align: center; margin-bottom: 10px;">⊹ ˖ Schematic ♡⸝⸝</h3>
        """, unsafe_allow_html=True)
        
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', bgcolor='transparent', size='4,4!', ratio='fill')
        dot.attr('node', fontname='Quicksand')
    
    # --- PERFORMANCE METRICS ---
    st.subheader("⊹ ˖ Digital Output Matrix ♡⸝⸝")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("AND GATE", results["AND"])
    m_col2.metric("OR GATE", results["OR"])
    m_col3.metric("XOR GATE", results["XOR"])
    m_col4.metric("NOT A", results["NOT_A"])

    # Second Row of Metrics
    m2_col1, m2_col2, m2_col3, m2_col4 = st.columns(4)
    m2_col1.metric("NAND GATE", results["NAND"])
    m2_col2.metric("NOR GATE", results["NOR"])
    m2_col3.metric("XNOR GATE", results["XNOR"])
    m2_col4.metric("NOT B", results["NOT_B"])

    # --- DATA ANALYTICS SECTION ---
    st.divider()
    with st.expander("📊 View Signal History & Export Data"):
        st.dataframe(st.session_state.history_db, use_container_width=True)
        
        # Buffer for export
        csv = st.session_state.history_db.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Session Data (CSV)",
            data=csv,
            file_name="logic_studio_export.csv",
            mime='text/csv'
        )

    # Footer
    st.markdown("<p style='text-align: center; opacity: 0.6;'>Strawberry Logic Engine v4.0.0 Stable | Python 3.10 Runtime</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()






