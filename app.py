import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Strawberry Logic", page_icon="🍓", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(255, 182, 193, 0.4), rgba(255, 182, 193, 0.4)), 
                    url("https://raw.githubusercontent.com/Tsundere-e/python-logic/main/download%20(15).jpg");
        background-size: cover;
        font-family: 'Quicksand', sans-serif;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(157, 109, 132, 0.8) !important;
        border-radius: 30px !important;
        padding: 20px !important;
        border: none !important;
    }

    .inner-card {
        background: #fff0f5;
        border-radius: 25px;
        padding: 30px;
        min-height: 400px;
    }

    .stTextInput input {
        border-radius: 15px !important;
        border: 2px solid #ffb6c1 !important;
        height: 45px !important;
    }

    .stButton button {
        background: white !important;
        color: #ff69b4 !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 20px !important;
        width: 100% !important;
        font-weight: bold !important;
    }

    .wave-box {
        background: linear-gradient(180deg, #ff8da1 0%, #ffc0d0 100%);
        border-radius: 20px;
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
    }

    header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>⊹ ˖ Strawberry Studio ♡⸝⸝</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Secure Login 🍓</h3>", unsafe_allow_html=True)
        st.markdown('<div class="inner-card">', unsafe_allow_html=True)
        st.text_input("Email", value="user@strawberry.io")
        st.text_input("Password", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Log In")
        st.markdown("<p style='text-align: center; color: #ff69b4; font-size: 0.8rem;'>Don't have an account? Register</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown("<h3 style='color: white;'>× × Strawberry Data Wave 🍓</h3>", unsafe_allow_html=True)
        st.markdown('<div class="inner-card">', unsafe_allow_html=True)
        st.markdown("""
            <div class="wave-box">
                <div>
                    <span style="font-size: 80px;">🍓</span><br>
                    <b>Pulse: STREAMING</b><br>
                    <span style="font-size: 0.7rem;">Heghe: 190 mΩ | 16s backout infinite</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
v_rail = st.select_slider("System Voltage", options=[1.2, 1.8, 3.3, 5.0], value=3.3)
a = st.slider("Input A", 0.0, v_rail, v_rail)
b = st.slider("Input B", 0.0, v_rail, 0.0)

res = {"AND": int(a >= v_rail*0.7 and b >= v_rail*0.7), "OR": int(a >= v_rail*0.7 or b >= v_rail*0.7)}

st.write(pd.DataFrame([res]))

st.markdown("<p style='text-align: center; color: white; opacity: 0.6;'>st.mowkanel / python-logic</p>", unsafe_allow_html=True)
