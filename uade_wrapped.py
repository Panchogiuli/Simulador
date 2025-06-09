import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# Datos de ejemplo (reemplazar por datos reales o entrada de usuario)
nombre_alumno = "Francisco Giuli"
aplazos = 3
materias_aprobadas = 5
total_materias = 8
faltas = 23
examen_final = "Marketing"

# Título y subtítulo
st.title("\U0001F4CA UADE Wrapped – Resumen del Cuatrimestre")
st.subheader(f"Alumno: {nombre_alumno}")

# Aplazos
st.markdown(f"### \U0001F534 Aplazos: {aplazos}")

# Gráfico circular de materias aprobadas
fig, ax = plt.subplots()
ax.pie([materias_aprobadas, total_materias - materias_aprobadas],
       labels=["Aprobadas", "Restantes"],
       colors=["#23c9c7", "#004265"],
       startangle=90,
       autopct='%1.0f%%')
st.pyplot(fig)

# Faltas
st.markdown(f"### \U0001F7E1 Faltas acumuladas: {faltas}")

# Alerta de examen final
if examen_final:
    st.warning(f"\u26A0\uFE0F Examen final requerido en {examen_final}")

# Logo UADE
try:
    img = Image.open("uade_logo.png")
    st.image(img, width=120)
except FileNotFoundError:
    st.info("Logo UADE no encontrado")
