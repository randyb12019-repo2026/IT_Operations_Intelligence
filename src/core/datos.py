# Módulo para carga y validación de datos del proyecto IT Operations Intelligence
import streamlit as st
import pandas as pd
from pathlib import Path

def carga_datos():
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    FINAL_DIR = PROJECT_ROOT / "data" / "final"
    PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

    def cargar_csv(ruta):
        if ruta.exists():
            return pd.read_csv(ruta)
        return None

    comparacion = cargar_csv(FINAL_DIR / "comparacion_modelos.csv")
    predicciones = cargar_csv(FINAL_DIR / "predicciones_incidencias.csv")
    datos_incidencias = cargar_csv(PROCESSED_DIR / "incident_event_log_transformado.csv")

    return comparacion, predicciones, datos_incidencias


def validar_datos(comparacion, predicciones, datos_incidencias):
    errores = []
    if comparacion is None:
        errores.append("data/final/comparacion_modelos.csv")
    if predicciones is None:
        errores.append("data/final/predicciones_incidencias.csv")
    if datos_incidencias is None:
        errores.append("data/processed/incident_event_log_transformado.csv")

    if errores:
        st.error("No se encontraron los archivos necesarios.")
        st.markdown("Archivos faltantes:\n- " + "\n- ".join(errores))
        st.markdown("---")
        st.markdown("""
        **Solución local:** Ejecuta los notebooks en orden
        (`notebooks/01_` a `05_`) para generar los CSVs.

        **Solución Docker:** Asegúrate de que los CSVs existen en tu máquina
        y reconstruye la imagen con `docker build -t it-operations-intelligence .`.
        """)
        st.stop()

    if comparacion.empty:
        st.warning("comparacion_modelos.csv está vacío.")
    if predicciones.empty:
        st.warning("predicciones_incidencias.csv está vacío.")
    if datos_incidencias.empty:
        st.warning("incident_event_log_transformado.csv está vacío.")
