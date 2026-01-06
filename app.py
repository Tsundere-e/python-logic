import streamlit as st
import graphviz
import datetime
import time
import pandas as pd

# --- SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Strawberry Logic Studio",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED CSS ENGINE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');

    /* Global Aesthetic */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* Professional Glassmorphism */
    .glass-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 2.5rem;
        border-radius: 30px;
        border: 2px solid #ffb6c1;
        box-shadow: 0 12px 40px rgba(255, 182, 193, 0.25);
        margin-bottom: 2rem;
        transition: all 0.4s ease;
    }

    .glass-card:hover {
        border-color: #ff69b4;
        box-shadow: 0 15px 50px rgba(255, 105, 180, 0.3);
    }

    /* Metric Dashboard Styling */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.98) !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 22px !important;
        padding: 20px !important;
        box-shadow: 5px 5px 0px #ffb6c1 !important;
        transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    [data-testid="stMetric"]:hover {
        transform: scale(1.05) translateY(-5px);
        box-shadow: 8px 8px 0px #ff69b4 !important;
    }

    /* Typography Overrides */
    h1, h2, h3 {
        color: #d87093 !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 0px rgba(255, 255, 255, 0.9);
    }
    
    p, span, label, .stMarkdown {
        color: #8b4367 !important;
        font-weight: 700 !important;
    }

    /* Specialized Components */
    .st-emotion-cache-1dj0h35 {
        background-color: #ff69b4 !important;
    }

    .console-header {
        background: #ffb6c1;
        color: white;
        padding: 5px 15px;
        border-radius: 10px 10px 0 0;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }

    .console-box {
        background: #2b2b2b;
        color: #ffdae0;
        font-family: 'Courier New', monospace;
        padding: 15px;
        border-radius: 0 0 10px 10px;
        font-size: 0.8rem;
        line-height: 1.4;
        border-bottom: 4px solid #ff69b4;
    }

    /* Interface Cleanup */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- CORE LOGIC ARCHITECTURE ---
class LogicProcessor:
    @staticmethod
    def run_all(a, b):
        return {
            "AND": a & b,
            "OR": a | b,
            "XOR": a ^ b,
            "NAND": 0 if (a == 1 and b == 1) else 1,
            "NOR": 1 if (a == 0 and b == 0) else 0,
            "XNOR": 1 if a == b else 0,
            "NOT_A": 1 if a == 0 else 0,
            "NOT_B": 1 if b == 0 else 0
        }

# --- APPLICATION STATE MANAGEMENT ---
def initialize_state():
    if 'boot_time' not in st.session_state:
        st.session_state.boot_time = datetime.datetime.now()
    if 'logs' not in st.session_state:
        st.session_state.logs = []
    if 'history' not in st.session_state:
        st.session_state.history = []

def add_log(msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    st.session_state.logs.append(f"[{timestamp}] {msg}")
    if len(st.session_state.logs) > 6:
        st.session_state.logs.pop(0)

# --- MAIN APP INTERFACE ---
def main():
    initialize_state()
    processor = LogicProcessor()

    # --- BRANDING HEADER ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    head_left, head_right = st.columns([1, 5])
    with head_left:
        st.image("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/Gemini_Generated_Image_pt31c1pt31c1pt31.jpg", width=130)
    with head_right:
        st.title("🍓 Strawberry Logic Studio Pro")
        st.markdown("##### High-Performance Digital Logic Simulation & Circuit Analysis Engine")
        st.caption(f"System Online since {st.session_state.boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SIMULATION CONTROLS ---
    col_ctrl, col_log = st.columns([2, 3])

    with col_ctrl:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("⊹ ˖ Control Center ♡⸝⸝")
        
        signal_a = st.toggle("Primary Bus A (Input)", value=False)
        signal_b = st.toggle("Primary Bus B (Input)", value=False)
        
        val_a, val_b = (1 if signal_a else 0), (1 if signal_b else 0)
        
        st.divider()
        st.write("Simulation Parameters")
        gate_speed = st.select_slider("Gate Latency (ms)", options=[10, 50, 100, 200], value=50)
        
        if st.button("Force Global Reset", use_container_width=True):
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_log:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🖥️ Kernel Execution")
        
        current_status = f"SIG_CHANGE: A={val_a} B={val_b} | Latency={gate_speed}ms"
        add_log(current_status)
        
        st.markdown('<div class="console-header">System Backend Logs</div>', unsafe_allow_html=True)
        log_content = "\\n".join(st.session_state.logs)
        st.markdown(f'<div class="console-box">{log_content}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # PROCESS LOGIC
    results = processor.run_all(val_a, val_b)

    # --- VISUALIZATION ENGINE ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("⚡ Live Schematic Visualization")
    
    # Custom Graphviz with High-Contrast Theming
    schematic = graphviz.Digraph()
    schematic.attr(rankdir='LR', bgcolor='transparent', splines='ortho')
    schematic.attr('node', fontname='Quicksand', style='filled,rounded', 
                  fontcolor='#5a3e5a', fontsize='12', fontweight='bold', 
                  color='#ff69b4', penwidth='3')
    schematic.attr('edge', color='#ffb6c1', penwidth='2', arrowhead='vee')

    # Input Clusters
    schematic.node('A', f'BUS A\\n[{val_a}]', shape='circle', 
                  fillcolor='#ff69b4' if signal_a else '#ffd1dc')
    schematic.node('B', f'BUS B\\n[{val_b}]', shape='circle', 
                  fillcolor='#ff69b4' if signal_b else '#ffd1dc')

    # Gate Architectures
    with schematic.subgraph(name='cluster_processing') as cpu:
        cpu.attr(label='Processing Unit', fontcolor='#d87093', color='#ffb6c1', style='dashed')
        active_gates = ["AND", "OR", "XOR", "NAND", "NOR"]
        for g in active_gates:
            is_active = results[g] == 1
            cpu.node(g, f'{g} GATE\\n({results[g]})', shape='rect', 
                    fillcolor='#ffc0cb' if is_active else '#ffffff')
            schematic.edge('A', g)
            schematic.edge('B', g)

    st.graphviz_chart(schematic, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- RESULTS MATRIX ---
    st.subheader("⊹ ˖ Output Matrix Analysis ♡⸝⸝")
    
    # Primary Metrics
    m_row1_1, m_row1_2, m_row1_3, m_row1_4 = st.columns(4)
    m_row1_1.metric("AND Operation", results["AND"], help="Logic High only if A and B are High")
    m_row1_2.metric("OR Operation", results["OR"], help="Logic High if any Input is High")
    m_row1_3.metric("XOR Operation", results["XOR"], help="Logic High if Inputs differ")
    m_row1_4.metric("NOT A (Inv)", results["NOT_A"], delta_color="inverse")

    # Secondary Metrics
    st.markdown(" ")
    m_row2_1, m_row2_2, m_row2_3, m_row2_4 = st.columns(4)
    m_row2_1.metric("NAND Gate", results["NAND"])
    m_row2_2.metric("NOR Gate", results["NOR"])
    m_row2_3.metric("XNOR Gate", results["XNOR"])
    m_row2_4.metric("NOT B (Inv)", results["NOT_B"], delta_color="inverse")

    # --- SYSTEM FOOTER ---
    st.divider()
    foot_l, foot_r = st.columns(2)
    with foot_l:
        st.caption("© 2026 Strawberry Logic Studio | Developed with Python & Love 🍓")
    with foot_r:
        st.markdown("<p style='text-align: right; opacity: 0.5;'>v4.2.1-STABLE-RELEASE</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
