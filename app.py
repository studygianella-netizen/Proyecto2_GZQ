import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import contextlib

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Bank Marketing Analytics",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# CLASE POO
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
        
    def histograma(self, variable):

        fig, ax = plt.subplots(figsize=(8,4))

        sns.histplot(
            self.df[variable],
            kde=True,
            ax=ax
        )

        return fig

# =====================================================
# SIDEBAR
# =====================================================

try:
    st.sidebar.image("python.png")
except:
    pass

st.sidebar.title("📌 Menú Principal")

opcion = st.sidebar.radio(
    "Navegación",
    [
        "🏠 Home",
        "📂 Carga de Dataset",
        "📊 Análisis Exploratorio (EDA)",
        "📌 Conclusiones"
    ]
)

# =====================================================
# HOME
# =====================================================

if opcion == "🏠 Home":

    st.title("📊 Análisis Exploratorio de Datos - Bank Marketing")

    try:
        st.image("fondo.png")
    except:
        pass

    st.subheader("👨‍💻 Datos del Autor")

    st.write("**Elaborado por:** Gianella Zorrilla Quispe")
    st.write("**Curso:** Especialización en Python potenciado con IA - Edición 58")
    st.write("**Institución:** DMC Institute")
    st.write("**Año:** 2026")

    st.divider()

    st.markdown("""
    ### Objetivo del Proyecto

    Este proyecto tiene como finalidad realizar un Análisis Exploratorio de Datos (EDA)
    sobre el dataset Bank Marketing, identificando patrones, tendencias y relaciones
    entre las variables que influyen en la aceptación de campañas de marketing bancario.
    """)

    st.divider()

    st.subheader("📁 Información del Dataset")

    st.markdown("""
    El dataset Bank Marketing contiene información de campañas de marketing
    realizadas por una institución financiera.

    Su objetivo es analizar las características de los clientes y determinar
    qué factores están asociados a la aceptación de una campaña comercial.
    """)

    st.divider()

    st.subheader("🛠️ Tecnologías Utilizadas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("🐍 Python")

    with col2:
        st.info("📊 Pandas")

    with col3:
        st.info("📈 Matplotlib")

    with col4:
        st.info("🚀 Streamlit")

# =====================================================
# CARGA DATASET
# =====================================================

elif opcion == "📂 Carga de Dataset":

    st.title("📂 Carga del Dataset")

    archivo = st.file_uploader(
        "Seleccione el archivo BankMarketing.csv",
        type=["csv"]
    )

    if archivo is not None:

        try:

            df = pd.read_csv(archivo, sep=";")

            st.session_state["df"] = df

            st.success("✅ Archivo cargado correctamente")

            st.subheader("Vista previa")

            st.dataframe(df.head())

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Filas", df.shape[0])

            with col2:
                st.metric("Columnas", df.shape[1])

        except Exception as e:

            st.error(f"Error: {e}")

    else:

        st.warning("⚠️ Debe cargar un archivo CSV.")


# =====================================================
# EDA
# =====================================================
elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.title("📊 Análisis Exploratorio de Datos")

    if "df" not in st.session_state:

        st.warning("⚠️ Primero debe cargar el dataset en el módulo 'Carga de Dataset'.")

    else:

        df = st.session_state["df"]

        analyzer = DataAnalyzer(df)

        tabs = st.tabs([
            "Información General",
            "Clasificación Variables",
            "Estadísticas",
            "Valores Faltantes",
            "Distribuciones",
            "Variables Categóricas",
            "Numérico vs Categórico",
            "Categórico vs Categórico",
            "Análisis Dinámico",
            "Hallazgos"
        ])

        # =================================================
        # ITEM 1
        # =================================================

        with tabs[0]:

            st.header("Ítem 1: Información General")

            st.subheader("Info()")

            st.code(analyzer.dataset_info())

            st.subheader("Tipos de Datos")

            tipos_df = pd.DataFrame({
                "Variable": analyzer.tipos_datos().index,
                "Tipo": analyzer.tipos_datos().values
            })

            st.dataframe(tipos_df)

            st.subheader("Valores Nulos")

            nulos_df = pd.DataFrame({
                "Variable": analyzer.valores_nulos().index,
                "Nulos": analyzer.valores_nulos().values
            })

            st.dataframe(nulos_df)

        # =================================================
        # ITEM 2
        # =================================================

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

        # =================================================
        # ITEM 3
        # =================================================

        with tabs[2]:

            st.header("Ítem 3: Estadísticas Descriptivas")

            st.dataframe(analyzer.estadisticas())

            col1, col2, col3 = st.columns(3)

            with col1:

                st.subheader("Media")

                st.dataframe(
                    analyzer.media().reset_index().rename(
                        columns={"index": "Variable", 0: "Media"}
                    )
                )

            with col2:

                st.subheader("Mediana")

                st.dataframe(
                    analyzer.mediana().reset_index().rename(
                        columns={"index": "Variable", 0: "Mediana"}
                    )
                )

            with col3:

                st.subheader("Moda")

                moda_df = analyzer.moda()

                st.dataframe(moda_df)

        # =================================================
        # ITEM 4
        # =================================================

        with tabs[3]:

            st.header("Ítem 4: Valores Faltantes")

            nulos = analyzer.valores_nulos()

            st.dataframe(nulos)

            fig, ax = plt.subplots(figsize=(10, 4))

            nulos.plot(
                kind="bar",
                ax=ax
            )

            plt.xticks(rotation=90)

            st.pyplot(fig)

            st.info(
                "Visualización de valores faltantes por variable."
            )

        # =================================================
        # ITEM 5
        # =================================================

        with tabs[4]:

            st.header("Ítem 5: Distribución de Variables Numéricas")

            numericas = analyzer.variables_numericas()

            variable = st.selectbox(
                "Seleccione una variable numérica",
                numericas
            )

            fig, ax = plt.subplots(figsize=(8, 4))

            sns.histplot(
                data=df,
                x=variable,
                kde=True,
                ax=ax)

            st.pyplot( analyzer.histograma(variable))

            st.success(
                f"Distribución observada para la variable: {variable}"
            )
        # =================================================
        # ITEM 6
        # =================================================
        with tabs[5]:
            st.header("Ítem 6: Análisis de Variables Categóricas")
            categoricas = analyzer.variables_categoricas()
            variable_cat = st.selectbox(
                            "Seleccione una variable categórica",
                             categoricas )

            conteo = df[variable_cat].value_counts()

            st.subheader("Conteos")
            st.dataframe(conteo)

            st.subheader("Proporciones (%)")
            st.dataframe(
                round(df[variable_cat].value_counts(normalize=True)*100,2)
                )

            fig, ax = plt.subplots(figsize=(10,5))

            sns.countplot(
            data=df,
            x=variable_cat,
            order=conteo.index,
            ax=ax )

            plt.xticks(rotation=45)

            st.pyplot(fig)
        # =================================================
        # ITEM 7
        # =================================================
        with tabs[6]:

            st.header("Ítem 7: Análisis Bivariado (Numérico vs Categórico)")

            numericas = analyzer.variables_numericas()

            variable_num = st.selectbox(
                "Variable numérica",
                numericas,
                key="num_bivariado")

            if "y" in df.columns:

                fig, ax = plt.subplots(figsize=(8,5))

                sns.boxplot(
                    data=df,
                    x="y",
                    y=variable_num,
                    ax=ax)

                st.pyplot(fig)

                st.info(
                    f"Comparación de {variable_num} respecto a la aceptación de la campaña." )
        # =================================================
        # ITEM 8
        # =================================================

        with tabs[7]:

            st.header("Ítem 8: Análisis Bivariado (Categórico vs Categórico)")

            categoricas = analyzer.variables_categoricas()

            variable_cat = st.selectbox(
                "Seleccione variable categórica",
                categoricas,
                key="cat_bivariado")

            if "y" in df.columns:

                tabla = pd.crosstab(
                df[variable_cat],
                df["y"] )

            st.dataframe(tabla)

            fig, ax = plt.subplots(figsize=(10,5))

            tabla.plot(
                kind="bar",
                ax=ax)

            st.pyplot(fig)
        # =================================================
        # ITEM 9
        # =================================================
        with tabs[8]:

            st.header("Ítem 9: Análisis Basado en Parámetros")

            columnas = st.multiselect(
                "Seleccione columnas",
                df.columns.tolist(),
                default=df.columns[:3])

            if columnas:

                st.dataframe(df[columnas].head())

            filas = st.slider(
                "Cantidad de filas a visualizar",
                5,
                50,
                10)

            st.dataframe(df.head(filas))

            mostrar_estadisticas = st.checkbox(
                "Mostrar estadísticas descriptivas")

            if mostrar_estadisticas:

                st.dataframe(
                df.select_dtypes(include=np.number).describe()
                )

        # =================================================
        # ITEM 10
        # =================================================
        with tabs[9]:

            st.header("Ítem 10: Hallazgos Clave")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Registros",
                    df.shape[0])

            with col2:
                st.metric(
                "Variables",
                df.shape[1])

            with col3:

                if "y" in df.columns:

                    aceptacion = round(
                        (df["y"] == "yes").mean() * 100,
                        2
                        )

                    st.metric(
                        "Aceptación",
                        f"{aceptacion}%"
                        )

            st.divider()

            st.subheader("Indicadores Estadísticos")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Edad Promedio",
                    round(df["age"].mean(),2)
                    )

                st.metric(
                    "Edad Mediana",
                    round(df["age"].median(),2)
                    )

            with c2:

                st.metric(
                    "Duración Promedio",
                    round(df["duration"].mean(),2)
                    )

            st.metric(
                "Duración Mediana",
                round(df["duration"].median(),2)
                )

            st.divider()

            st.success("""
            Hallazgos principales:

            • La edad presenta una distribución amplia entre los clientes.

            • La duración del contacto es una de las variables más relevantes del dataset.

            • Existen diferencias entre los grupos que aceptan y no aceptan la campaña.

            • Algunas categorías muestran comportamientos distintos frente a la aceptación.

            • El análisis exploratorio permite identificar segmentos de clientes con mayor potencial para futuras campañas.
            """)

elif opcion == "📌 Conclusiones":

    st.title("📌 Conclusiones Finales")

    st.subheader("📌 Conclusiones Finales")

    st.markdown("""
        ### 1. Influencia de la duración del contacto
        Se observó que los clientes con mayor duración de contacto tienden a presentar una mayor tasa de aceptación de la campaña. Esto sugiere que la calidad y profundidad de la interacción comercial puede influir significativamente en los resultados obtenidos.

        ### 2. Diferencias entre segmentos de clientes
        El análisis de variables demográficas y socioeconómicas mostró diferencias en el comportamiento de aceptación entre distintos grupos de clientes. Esto permite identificar segmentos con mayor potencial para futuras campañas.

        ### 3. Importancia de los canales de comunicación
        Los resultados evidencian que algunos canales de contacto presentan mejores niveles de respuesta que otros. Optimizar el uso de los canales más efectivos podría mejorar la eficiencia de las campañas de marketing.

        ### 4. Valor del análisis exploratorio para la toma de decisiones
        La exploración de datos permitió identificar patrones, distribuciones y relaciones entre variables que facilitan una mejor comprensión del comportamiento de los clientes y apoyan la toma de decisiones basada en datos.

        ### 5. Oportunidades de optimización comercial
        La información obtenida permite orientar mejor los recursos comerciales, enfocando esfuerzos en los perfiles de clientes y estrategias de contacto que muestran mayores probabilidades de generar resultados positivos.
        """)
             
