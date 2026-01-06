import streamlit as st
import datetime
import pandas as pd
import time

# --- 1. CONFIGURAÇÃO DE HARDWARE VIRTUAL ---
st.set_page_config(
    page_title="Strawberry Logic Studio | Pro",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. O MOTOR DE UI/UX (CSS INJECTION BLINDADO) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap');

    /* Reset Global e Fundo */
    .stApp {
        background: url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* Container Principal para os Cards */
    .main-flex-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        padding: 40px 10px;
        width: 100%;
    }

    /* Moldura Roxa (Outer Shell) - Baseado em unnamed (1).jpg */
    .outer-frame {
        background: #9d6d84;
        border-radius: 40px;
        padding: 25px;
        width: 100%;
        max-width: 480px;
        min-height: 600px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }

    .frame-header {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    /* Caixa Branca Interna (Onde os widgets DEVEM ficar) */
    .inner-content-box {
        background: #fff0f5;
        border-radius: 30px;
        padding: 30px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        border: 2px solid rgba(255,182,193,0.4);
        position: relative;
    }

    /* FIX CRÍTICO: Forçando o Streamlit a não vazar componentes */
    div[data-testid="stVerticalBlock"] > div:has(div.inner-content-box) {
        gap: 0 !important;
    }

    /* Estilização dos Inputs (Screenshot_57.png) */
    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 20px !important;
        height: 55px !important;
        padding-left: 20px !important;
        color: #8b4367 !important;
        font-size: 1rem !important;
    }

    /* Estilização do Botão Log In */
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
        transition: 0.2s;
    }

    .stButton > button:active {
        transform: translateY(4px);
        box-shadow: 0 2px 0px #ffb6c1 !important;
    }

    /* Visual da Wave (Strawberry Data Wave) */
    .wave-container {
        background: linear-gradient(180deg, #ff8da1 0%, #ffc0d0 100%);
        border-radius: 25px;
        height: 380px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border: 1px solid white;
    }

    .floating-berry {
        font-size: 100px;
        animation: floatBerry 5s ease-in-out infinite;
        z-index: 10;
        filter: drop-shadow(0 15px 20px rgba(0,0,0,0.2));
    }

    @keyframes floatBerry {
        0%, 100% { transform: translateY(0) rotate(-5deg); }
        50% { transform: translateY(-30px) rotate(5deg); }
    }

    /* Métricas Digitais (Screenshot_56.png) */
    .logic-matrix-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 25px;
        padding: 40px 20px;
    }

    .logic-metric-card {
        background: white;
        border: 6px solid #ffb6c1;
        border-radius: 40px;
        padding: 30px;
        text-align: center;
        box-shadow: 10px 10px 0px #ffb6c1;
    }

    .gate-label { font-size: 1.6rem; color: #8b4367; font-weight: 700; }
    .gate-value { font-size: 2.8rem; color: #ff69b4; font-weight: 700; }

    /* Esconder elementos padrão */
    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DO PROCESSADOR ---
class StrawberryKernel:
    def __init__(self):
        self.logs = []
    
    def compute_all(self, a, b):
        return {
            "AND": int(a and b),
            "OR": int(a or b),
            "XOR": int(a != b),
            "NAND": int(not (a and b)),
            "NOR": int(not (a or b)),
            "XNOR": int(a == b)
        }

# --- 4. CONTROLE DE SESSÃO ---
if 'kernel' not in st.session_state:
    st.session_state.kernel = StrawberryKernel()
if 'history_logs' not in st.session_state:
    st.session_state.history_logs = [f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Core Ready"]

def log_update(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.history_logs.append(f"[{ts}] {msg}")
    if len(st.session_state.history_logs) > 6: st.session_state.history_logs.pop(0)

# --- 5. RENDERIZAÇÃO DO APP ---
def main():
    # Header de Branding
    st.markdown("""
        <div style="background: rgba(255,255,255,0.7); padding: 20px; border-radius: 25px; border: 2px solid #ffb6c1; text-align: center; margin-bottom: 30px;">
            <h1 style="color: #8b4367; margin:0; font-size: 2.5rem;">🍓 Strawberry Logic Studio Pro</h1>
            <p style="color: #ff69b4; font-weight: 700; margin:0; letter-spacing: 1px;">SILICON SIMULATION INTERFACE v5.0.0</p>
        </div>
    """, unsafe_allow_html=True)

    # Painel de Controle Superior
    top_c1, top_c2 = st.columns([1, 1])
    with top_c1:
        st.markdown('<div style="background:white; padding:25px; border-radius:25px; border:1px solid #ffb6c1;">', unsafe_allow_html=True)
        st.subheader("⊹ ˖ Bus Logic Inputs ♡⸝⸝")
        b1, b2 = st.columns(2)
        val_a = b1.toggle("Bus A Signal", key="bus_a")
        val_b = b2.toggle("Bus B Signal", key="bus_b")
        v_rail = st.select_slider("Voltage Rail", options=[1.8, 3.3, 5.0], value=3.3)
        st.markdown('</div>', unsafe_allow_html=True)

    with top_c2:
        log_update(f"SIGNAL: A={int(val_a)} B={int(val_b)} @ {v_rail}V")
        log_content = "<br>".join(st.session_state.history_logs)
        st.markdown(f'<div style="background:#2d1b24; color:#ffb6c1; padding:20px; border-radius:20px; font-family:\'Fira Code\',monospace; font-size:0.9rem; height:155px; overflow-y:auto; border-left:8px solid #ff69b4;">{log_content}</div>', unsafe_allow_html=True)

    results = st.session_state.kernel.compute_all(val_a, val_b)

    # --- SEÇÃO DOS CARDS (SISTEMA FLEX RESPONSIVO) ---
    st.markdown('<div class="main-flex-container">', unsafe_allow_html=True)

    # CARD 1: LOGIN SIMULATOR
    st.markdown('<div class="outer-frame"><div class="frame-header">× × Secure Login 🍓 ♡⸝⸝</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="inner-content-box">', unsafe_allow_html=True)
        st.text_input("Access Email", value="user@strawberry.com", key="login_email")
        st.text_input("Auth Password", type="password", value="logic123", key="login_pass")
        st.markdown('<p style="text-align: right; font-size: 0.85rem; color: #ff69b4; margin-top: 5px; font-weight: 700;">Forget Password?</p>', unsafe_allow_html=True)
        if st.button("Log In"): 
            st.toast("Access Granted!", icon="🍓")
        st.markdown('<div style="flex-grow:1;"></div>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 0.85rem; color: #8b4367;">Don\'t have an account? <span style="color:#ff69b4; text-decoration:underline; font-weight:700;">Register</span></p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # CARD 2: STRAWBERRY WAVE
    st.markdown('<div class="outer-frame"><div class="frame-header">× × Strawberry Data Wave 🍓 ♡⸝⸝</div>', unsafe_allow_html=True)
    st.markdown('<div class="inner-content-box" style="padding: 10px; justify-content: center;">', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="wave-container">
            <div class="floating-berry">🍓</div>
            <div style="position: absolute; bottom: 25px; width: 100%; text-align: center; color: white; z-index: 15;">
                <div style="font-weight: 700; font-size: 1.4rem;">Pulse: {"HIGH" if val_a or val_b else "LOW"}</div>
                <div style="font-size: 0.8rem; opacity: 0.9; margin-top: 5px;">Heghe: 190 mΩ-190 | 16s backout style infinite</div>
            </div>
            <div style="position: absolute; width: 200%; height: 100px; background: rgba(255,255,255,0.2); bottom: 0; border-radius: 45%; animation: wave-move 10s linear infinite;"></div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Fim do container de cards

    # --- MATRIZ DE RESULTADOS (Screenshot_56.png) ---
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: 2px 2px #ff69b4; font-size: 2.5rem; margin-top: 30px;'>⊹ ˖ Digital Logic Matrix ♡⸝⸝</h2>", unsafe_allow_html=True)
    
    st.markdown('<div class="logic-matrix-grid">', unsafe_allow_html=True)
    for gate, val in results.items():
        st.markdown(f'''
            <div class="logic-metric-card">
                <div class="gate-label">{gate}</div>
                <div class="gate-value">({val})</div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Rodapé Final
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; opacity: 0.6; padding-bottom: 40px;'>st.mowkanel / python-logic-pro • Build 2026.1.06</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
