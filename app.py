import streamlit as st
import graphviz

# Page Configuration
st.set_page_config(page_title="Strawberry Logic Sim", page_icon="🎀")

# Custom CSS for UI/UX Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

    .stApp {
        background-color: #fff0f5;
        font-family: 'Quicksand', sans-serif;
    }

    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.7);
        border: 2px solid #ffb6c1;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 3px 3px 10px rgba(216, 112, 147, 0.1);
    }

    h1, h2, h3 {
        color: #d87093 !important;
    }

    .st-emotion-cache-1dj0h35 {
        background-color: #ff69b4 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🎀 Logic Gate Sim: Strawberry Edition 🍓")
    st.write("### Interactive Digital Logic Simulation")
    
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🍓 Input A")
        input_a = st.toggle("Signal A", value=False)
    with col2:
        st.subheader("🍓 Input B")
        input_b = st.toggle("Signal B", value=False)

    a_val = 1 if input_a else 0
    b_val = 1 if input_b else 0

    results = {
        "AND": a_val & b_val,
        "OR": a_val | b_val,
        "XOR": a_val ^ b_val,
        "NOT_A": 1 if a_val == 0 else 0
    }

    st.divider()
    st.subheader("⊹ ˖ Circuit Diagram ♡⸝⸝")
    
    # Diagram Generation
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', bgcolor='transparent')
    dot.attr('node', fontname='Quicksand', style='filled', shape='circle', fontcolor='white')
    
    on_color = '#ff69b4'
    off_color = '#ffb6c1'
    
    dot.node('A', f'A\n({a_val})', fillcolor=on_color if input_a else off_color, color='#d87093')
    dot.node('B', f'B\n({b_val})', fillcolor=on_color if input_b else off_color, color='#d87093')
    
    dot.attr('node', shape='rect', style='filled,rounded')
    
    for gate, res in results.items():
        if gate != "NOT_A":
            dot.node(gate, f'{gate}\n({res})', fillcolor='#ffc0cb' if res else 'white', color='#ff69b4')
            dot.edge('A', gate, color='#ff69b4')
            dot.edge('B', gate, color='#ff69b4')

    st.graphviz_chart(dot)

    st.divider()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AND Gate", results["AND"])
    m2.metric("OR Gate", results["OR"])
    m3.metric("XOR Gate", results["XOR"])
    m4.metric("NOT A", results["NOT_A"])

if __name__ == "__main__":
    main()
