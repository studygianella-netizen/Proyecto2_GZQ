import streamlit as st

# =====================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =====================================================
st.set_page_config(
    page_title="Bank Marketing Analytics",
    page_icon="📊",
    layout="wide")

st.sidebar.image("python.png")

st.title("PROYECTO 2")

st.write("Elaborado por: Gianella Zorrilla Quispe")
st.write("Carrera: Administración de empresas")
st.write ("Curso: Especialización en Python potenciado con IA - Edición - 58")
st.write ("Año: 2026")
st.image("fondo.png")


st.sidebar.title("📌 Menú Principal")
opcion = st.sidebar.radio(
    "Navegación",
    ["🏠 Home"])
# =====================================================
# HOME
# =====================================================


