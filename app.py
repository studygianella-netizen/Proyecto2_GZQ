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

 st.subheader("👨‍💻 Datos del Autor")

        st.write("**Elaborado por:** Gianella Zorrilla Quispe")
        st.write("**Curso:**  Especialización en Python potenciado con IA - Edición - 58")
        st.write("**Institución:** DMC Institute")
        st.write("**Año:** 2026")

st.image("fondo.png")


st.sidebar.title("📌 Menú Principal")
opcion = st.sidebar.radio(
    "Navegación",
    ["🏠 Home"])
# =====================================================
# HOME
# =====================================================

if opcion == "🏠 Home":

    st.title("📊 Análisis Exploratorio de Datos - Bank Marketing")

    st.markdown("""
    ### Objetivo del Proyecto
    Este proyecto tiene como finalidad realizar un Análisis Exploratorio de Datos (EDA)
    sobre el dataset **Bank Marketing**, identificando patrones, tendencias y relaciones
    entre las variables que influyen en la aceptación de campañas de marketing bancario.

    La aplicación ha sido desarrollada utilizando Python y Streamlit como parte de la
    Especialización en Python for Analytics.
    """)

    st.divider()
    
    st.subheader("📁 Información del Dataset")
    st.markdown ("""
        El dataset Bank Marketing contiene información de campañas de marketing
        realizadas por una institución financiera.

        Su objetivo es analizar las características de los clientes y determinar
        qué factores están asociados a la aceptación de una campaña comercial.
        """)

    st.divider()

    st.subheader("🛠️ Tecnologías Utilizadas")

    tecnologia1, tecnologia2, tecnologia3, tecnologia4 = st.columns(4)

    with tecnologia1:
        st.info("🐍 Python")

    with tecnologia2:
        st.info("📊 Pandas")

    with tecnologia3:
        st.info("📈 Matplotlib & Seaborn")

    with tecnologia4:
        st.info("🚀 Streamlit")

    st.divider()

    st.subheader("🎯 Alcance del Proyecto")

    st.success("""
    Este aplicativo permitirá explorar el dataset mediante estadísticas descriptivas,
    visualizaciones interactivas y análisis de variables numéricas y categóricas,
    facilitando la identificación de hallazgos relevantes para la toma de decisiones.
    """)
