import streamlit as st
import pandas as pd
import datetime
import time

st.set_page_config(page_title="Strawberry Logic Studio Pro", page_icon="🍓", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Fira+Code&display=swap');

    .stApp {
        background: linear-gradient(rgba(157, 109, 132, 0.85), rgba(157, 109, 132, 0.85)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        font-family: 'Quicksand', sans-serif;
    }

    [data-testid="stVerticalBlock"] > div:has(.shell) {
        background: #9d6d84;
        border-radius: 35px;
        padding: 25px !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.2);
    }

    .inner {
        background: #fff0f5;
        border-radius: 25px;
        padding: 25px;
        border: 1px solid #ffb6c1;
        min-height: 400px;
        display: flex;
        flex-direction: column;
    }

    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 15px !important;
    }

    .stButton > button {
        background: white !important;
        color: #ff69b4 !important;
        border: 3px solid #ffb6c1 !important;
        border-radius: 25px !important;
        width: 100% !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 0px #ffb6c1 !important;
    }

    .wave-box {
        background: linear-gradient(180deg, #ff8da1, #ffc0d0);
        border-radius: 20px;
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }

    .berry {
        font-size: 80px;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    .m-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
    }

    .m-card {
        background: white;
        border: 4px solid #ffb6c1;
        border-radius: 25px;
        padding: 15px;
        text-align: center;
        box-shadow: 5px 5px 0px #ffb6c1;
    }

    .m-label { color: #8b4367; font-weight: 700; font-size: 1rem; }
    .m-val { color: #ff69b4; font-size: 1.8rem; font-weight: 700; }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

class LogicKernel:
    @staticmethod
    def compute(a, b):
        a_i, b_i = int(a), int(b)
        return {
            "AND": (a_i & b_i) & 1,
            "OR": (a_i | b_i) & 1,
            "XOR": (a_i ^ b_i) & 1,
            "NAND": (~(a_i & b_i)) & 1,
            "NOR": (~(a_i | b_i)) & 1,
            "XNOR": (~(a_i ^ b_i)) & 1
        }

if 'history_list' not in st.session_state:
    st.session_state.history_list = []

st.markdown("<h1 style='color: white; text-align: center;'>Strawberry Studio v2.0</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="shell">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>× × Login 🍓</h3>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="inner">', unsafe_allow_html=True)
        st.text_input("User", value="dev@strawberry.com")
        st.text_input("Key", type="password", value="****")
        st.button("Auth Sequence")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="shell">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>× × Wave 🍓</h3>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="inner">', unsafe_allow_html=True)
        st.markdown('<div class="wave-box"><div class="berry">🍓</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
ctrl1, ctrl2 = st.columns(2)
in_a = ctrl1.toggle("Bus A", value=True)
in_b = ctrl2.toggle("Bus B", value=False)

results = LogicKernel.compute(in_a, in_b)
st.session_state.history_list.append({**results, "ts": datetime.datetime.now()})

st.markdown('<div class="m-grid">', unsafe_allow_html=True)
for g, v in results.items():
    st.markdown(f"""
        <div class="m-card">
            <div class="m-label">{g}</div>
            <div class="m-val">({v})</div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

with st.expander("Analytical History"):
    if st.session_state.history_list:
        st.table(pd.DataFrame(st.session_state.history_list).tail(10))
