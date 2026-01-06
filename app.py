import streamlit as st
import graphviz

def main():
    st.set_page_config(page_title="Logic Gate Sim", layout="centered")
    
    st.title("⚡ Python Logic Gate Simulator")
    st.markdown("Interactive Boolean Algebra visualization.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input A")
        input_a = st.toggle("Activate Signal A", value=False)

    with col2:
        st.subheader("Input B")
        input_b = st.toggle("Activate Signal B", value=False)

    a_val = 1 if input_a else 0
    b_val = 1 if input_b else 0

    st.divider()

    # Logic Calculations
    res_and = a_val & b_val
    res_or = a_val | b_val
    res_xor = a_val ^ b_val
    res_not = 0 if a_val == 1 else 1

    # Visualization using Graphviz
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR')
    
    graph.node('A', 'Input A', shape='circle', style='filled', color='lightblue' if input_a else 'lightgrey')
    graph.node('B', 'Input B', shape='circle', style='filled', color='lightblue' if input_b else 'lightgrey')
    
    graph.node('AND', f'AND\n{res_and}', shape='box', style='filled', color='lightgreen' if res_and else 'white')
    graph.node('OR', f'OR\n{res_or}', shape='box', style='filled', color='lightgreen' if res_or else 'white')
    graph.node('XOR', f'XOR\n{res_xor}', shape='box', style='filled', color='lightgreen' if res_xor else 'white')
    
    graph.edge('A', 'AND')
    graph.edge('B', 'AND')
    graph.edge('A', 'OR')
    graph.edge('B', 'OR')
    graph.edge('A', 'XOR')
    graph.edge('B', 'XOR')

    st.graphviz_chart(graph)

    st.divider()

    # Metric Dashboard
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AND Gate", res_and, delta_color="normal")
    m2.metric("OR Gate", res_or, delta_color="normal")
    m3.metric("XOR Gate", res_xor, delta_color="normal")
    m4.metric("NOT A", res_not, delta_color="inverse")

if __name__ == "__main__":
    main()