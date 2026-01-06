import streamlit as st
import graphviz

# Page Configuration
st.set_page_config(
    page_title="Strawberry Logic Simulator",
    page_icon="🎀",
    layout="centered"
)

# Professional Kawaii CSS Injection
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

    /* Background with your Strawberry pattern */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/sua-conta/seu-repo/main/download%20(15).jpg");
        background-size: cover;
        background-repeat: repeat;
        font-family: 'Quicksand', sans-serif;
    }

    /* Metric Cards Styling - Semi-transparent white for contrast */
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 20px !important;
        padding: 15px !important;
        box-shadow: 5px 5px 15px rgba(216, 112, 147, 0.2) !important;
    }

    /* Text contrast adjustments */
    h1, h2, h3 {
        color: #d87093 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }
    
    p, span, label {
        color: #8b4367 !important;
        font-weight: 600 !important;
    }

    /* Pink Toggle Switches */
    .st-emotion-cache-1dj0h35 {
        background-color: #ff69b4 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🎀 Logic Gate Sim: Strawberry Edition 🍓")
    st.write("### Interactive Digital Logic Dashboard")
    
    st.divider()

    # Input Section with Toggles
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🍓 Input A")
        input_a = st.toggle("Signal A", value=False)
    with col2:
        st.subheader("🍓 Input B")
        input_b = st.toggle("Signal B", value=False)

    # Convert Boolean to Integer
    a_val = 1 if input_a else 0
    b_val = 1 if input_b else 0

    # Logic Calculation Engine
    results = {
        "AND": a_val & b_val,
        "OR": a_val | b_val,
        "XOR": a_val ^ b_val,
        "NOT_A": 1 if a_val == 0 else 0
    }

    st.divider()
    st.subheader("⊹ ˖ Live Circuit Diagram ♡⸝⸝")
    
    # Graphviz Diagram Creation
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', bgcolor='transparent')
    
    # Global Node Attributes (Dark font for visibility)
    dot.attr('node', fontname='Quicksand', style='filled', shape='circle', 
             fontcolor='#5a3e5a', fontsize='12', fontweight='bold')
    
    # Input Nodes Color Logic
    on_color = '#ff69b4'
    off_color = '#ffd1dc'
    
    dot.node('A', f'Input A\\n({a_val})', fillcolor=on_color if input_a else off_color, color='#d87093')
    dot.node('B', f'Input B\\n({b_val})', fillcolor=on_color if input_b else off_color, color='#d87093')
    
    # Gate Nodes Styling
    dot.attr('node', shape='rect', style='filled,rounded')
    
    for gate, res in results.items():
        if gate != "NOT_A":
            gate_fill = '#ffc0cb' if res else '#fdfcfc'
            dot.node(gate, f'{gate} Gate\\n({res})', 
                     fillcolor=gate_fill, 
                     color='#ff69b4', 
                     fontcolor='#8b4367')
            dot.edge('A', gate, color='#ff69b4')
            dot.edge('B', gate, color='#ff69b4')

    # Rendering the Graph in Streamlit
    st.graphviz_chart(dot)

    st.divider()

    # Final Results Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AND", results["AND"])
    m2.metric("OR", results["OR"])
    m3.metric("XOR", results["XOR"])
    m4.metric("NOT A", results["NOT_A"])

if __name__ == "__main__":
    main()
