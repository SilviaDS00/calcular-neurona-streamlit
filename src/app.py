import streamlit as st

st.title("¡Hola, Neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas"])
with tab1:
    w0 = st.slider("Peso", 0.0, 5.0, 1.3, key="w0_tab1")

    x0 = st.number_input("Introduzca un valor de la entrada", key="x0_tab1")
    
    y = x0 * w0
    
    if st.button("Calcular la salida",key="b0"):
        st.write(f"La salida de la neurona es {y}")

        
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, 1.3, key="w0_tab2")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, 1.3, key="w1_tab2")

    col1, col2 = st.columns(2)
    with col1:
        x0 = st.number_input("Entrada x0", key="x0_tab2")
    with col2:
        x1 = st.number_input("Entrada x1", key="x1_tab2")
    
    y = x0 * w0 + x1 * w1
    
    if st.button("Calcular la salida", key="b1"):
        st.write(f"La salida de la neurona es {y}")
        
with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, 1.3, key="w0_col1_tab3")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, 1.3, key="w1_col2_tab3")
    with col3:
        w2 = st.slider("Peso w2", 0.0, 5.0, 1.3, key="w2_col3_tab3")

    col1, col2, col3 = st.columns(3)
    with col1:
        x0 = st.number_input("Entrada x0", key="x0_col1_tab3")
    with col2:
        x1 = st.number_input("Entrada x1", key="x1_col2_tab3")
    with col3:
        x2 = st.number_input("Entrada x2", key="x2_col3_tab3")
    
    s = st.number_input("Introduce el valor del sesgo", key="s_tab3")
    
    y = x0 * w0 + x1 * w1 + x2 * w2
    
    y = y + s

    if st.button("Calcular la salida", key="b2"):
        st.write(f"La salida de la neurona es {y}")
