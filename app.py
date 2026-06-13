import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import contextlib

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
    [   "🏠 Home",
        "📂 Carga de Dataset",
        "📊 Análisis Exploratorio (EDA)" ])
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
            st.session_state["df"] = df

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

# =====================================================
# CLASE DATA ANALYZER
# =====================================================

class DataAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def dataset_info(self):

        buffer = StringIO()

        with contextlib.redirect_stdout(buffer):
            self.df.info()

        return buffer.getvalue()

    def tipos_datos(self):
        return self.df.dtypes

    def valores_nulos(self):
        return self.df.isnull().sum()

    def variables_numericas(self):
        return self.df.select_dtypes(include=np.number).columns.tolist()

    def variables_categoricas(self):
        return self.df.select_dtypes(exclude=np.number).columns.tolist()

    def estadisticas(self):
        return self.df.describe()

    def media(self):
        return self.df.select_dtypes(include=np.number).mean()

    def mediana(self):
        return self.df.select_dtypes(include=np.number).median()

    def moda(self):
        return self.df.mode().iloc[0]

# =====================================================
# EDA
# =====================================================

elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.title("📊 Análisis Exploratorio de Datos")

    if "df" not in st.session_state:

        st.warning("⚠️ Primero debe cargar el dataset.")

    else:

        df = st.session_state["df"]

        analyzer = DataAnalyzer(df)

        tabs = st.tabs([
            "Información General",
            "Clasificación Variables",
            "Estadísticas",
            "Valores Faltantes",
            "Distribuciones" ])
# =====================================================
# Ítem 1: Información general del dataset 
# =====================================================
with tabs[0]:

            st.header("Ítem 1: Información General")

            st.subheader("Info()")

            st.code(analyzer.dataset_info())

            st.subheader("Tipos de Datos")

            st.dataframe(analyzer.tipos_datos().reset_index())

            st.subheader("Valores Nulos")

            st.dataframe(analyzer.valores_nulos().reset_index())
# =====================================================
# Ítem 2: Clasificación de variables 
# =====================================================
    with tabs[1]:

            st.header("Ítem 2: Clasificación de Variables")

            numericas = analyzer.variables_numericas()
            categoricas = analyzer.variables_categoricas()

            col1, col2 = st.columns(2)

            with col1:

                st.success(f"Variables Numéricas ({len(numericas)})")

                st.write(numericas)

            with col2:

                st.info(f"Variables Categóricas ({len(categoricas)})")

                st.write(categoricas)

# =====================================================
# Ítem 3: Estadísticas descriptivas 
# =====================================================
 with tabs[2]:

            st.header("Ítem 3: Estadísticas Descriptivas")

            st.dataframe(analyzer.estadisticas())

            col1, col2, col3 = st.columns(3)

            with col1:

                st.subheader("Media")

                st.dataframe(analyzer.media())

            with col2:

                st.subheader("Mediana")

                st.dataframe( analyzer.mediana())

            with col3:

                st.subheader("Moda")

                st.dataframe(analyzer.moda())
# =====================================================
# Ítem 4: Análisis de valores faltantes
# =====================================================
  with tabs[3]:

            st.header("Ítem 4: Valores Faltantes")

            nulos = analyzer.valores_nulos()

            st.dataframe(nulos)

            fig, ax = plt.subplots(figsize=(10,4))

            nulos.plot(kind="bar",ax=ax)

            plt.xticks(rotation=90)

            st.pyplot(fig)

            st.info("El gráfico muestra la cantidad de valores faltantes por variable." )     
# =====================================================
# Ítem 5: Distribución de variables numéricas
# =====================================================
           with tabs[4]:

            st.header("Ítem 5: Distribución de Variables Numéricas")

            numericas = analyzer.variables_numericas()

            variable = st.selectbox(
                "Seleccione una variable",
                numericas
            )

            fig, ax = plt.subplots(figsize=(8,4))

            sns.histplot(
                df[variable],
                kde=True,
                ax=ax
            )

            st.pyplot(fig)

            st.success(
                f"Distribución observada para la variable {variable}"
            )
# =====================================================
# Ítem 6: Análisis de variables categóricas 
# =====================================================

# =====================================================
# Ítem 7: Análisis bivariado (numérico vs categórico)
# =====================================================

# =====================================================
# Ítem 8: Análisis bivariado (categórico vs categórico)
# =====================================================

# =====================================================
# Ítem 9: Análisis basado en parámetros seleccionados
# =====================================================

# =====================================================
# Ítem 10: Hallazgos clave 
# =====================================================
                

