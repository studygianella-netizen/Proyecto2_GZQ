import streamlit as st


st.set_page_config(page_title="Proyecto 1 Python", layout="wide")

st.sidebar.image("python.png")

st.title("PROYECTO 1")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Gianella Zorrilla Quispe")
st.write("Carrera: Administración de empresas")
st.write ("Curso: Especialización en Python potenciado con IA - Edición - 58")
st.write ("Año: 2026")
st.image("fondo.png")

menu = st.sidebar.selectbox("Seleccione una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

# =====================================================
# HOME
# =====================================================

if menu == "Home":
    st.write("Bienvenido a mi aplicación")
    st.write("Descripción del proyecto:")
    st.write("Aplicación interactiva desarrollada en Streamlit como proyecto aplicado del módulo de Fundamentos de Programación. El proyecto integra conceptos esenciales de Python como variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO), mediante una interfaz dinámica e intuitiva.")
    st.write("Tecnologías utilizadas:")
    st.write("""
    - Python
    - Streamlit
    - Pandas
    - NumPy
    """)

# =====================================================
# EJERCICIO 1
# =====================================================

elif menu == "Ejercicio 1":
    
# =====================================================
# EJERCICIO 2
# =====================================================

elif menu == "Ejercicio 2":
   

    
# =====================================================
# EJERCICIO 3
# =====================================================

elif menu == "Ejercicio 3":
   


# =====================================================
# EJERCICIO 3
# =====================================================
    
elif menu == "Ejercicio 4":
   
