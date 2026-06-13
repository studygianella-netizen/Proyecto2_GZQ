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
    [
        "🏠 Home",
        "📂 Carga de Dataset"
    ]
)
# =====================================================
# HOME
# =====================================================

if opcion == "🏠 Home":

    st.title("📊 Análisis Exploratorio de Datos - Bank Marketing")

    st.markdown("""
    ### Objetivo del Proyecto
    Este proyecto tiene como finalidad realizar un Análisis Exploratorio de Datos (EDA)
    sobre el dataset **Bank Marketing**, identificando patrones, tendencias y relaciones
    entre las variables que influyen en la aceptación de campañas de marketing bancario.""")

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

# =====================================================
# CARGA DEL DATASET
# =====================================================

elif opcion == "📂 Carga de Dataset":

    st.title("📂 Carga del Dataset")

    st.markdown("""
    En esta sección se cargará el archivo CSV que será utilizado
    para el Análisis Exploratorio de Datos (EDA).
    """)

    archivo = st.file_uploader(
        "Seleccione el archivo BankMarketing.csv",
        type=["csv"]
    )

    if archivo is not None:

        try:
            import pandas as pd

            df = pd.read_csv(archivo)

            st.success("✅ Archivo cargado correctamente")

            st.subheader("Vista previa del Dataset")

            st.dataframe(df.head())

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Filas", df.shape[0])

            with col2:
                st.metric("Columnas", df.shape[1])

            st.subheader("Información General")

            st.write(f"El dataset contiene **{df.shape[0]} filas** y **{df.shape[1]} columnas**.")

        except Exception as e:
            st.error(f"Error al cargar el archivo: {e}")

    else:
        st.warning("⚠️ Debe cargar un archivo CSV para continuar.")
