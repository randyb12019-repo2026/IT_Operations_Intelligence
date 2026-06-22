# Módulo que renderiza la página de Predicciones de Incidencias
import streamlit as st
import pandas as pd

def predicciones(seccion, predicciones, col_pred):
    if seccion != "Predicciones":
        return

    st.header("Predicciones de Incidencias")

    if predicciones is None:
        st.warning("No hay datos de predicciones disponibles.")
        return

    if col_pred not in predicciones.columns:
        st.warning("No se encontró la columna de predicciones.")
        return

    riesgo = predicciones[predicciones[col_pred] == 1]
    cumplen = predicciones[predicciones[col_pred] == 0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tickets", len(predicciones))
    with col2:
        st.metric("Cumplen SLA", len(cumplen))
    with col3:
        st.metric("Riesgo Incumplimiento", len(riesgo))

    def mostrar_tabla(df, titulo):
        if len(df) == 0:
            st.info("No hay tickets en esta categoría.")
            return
        df_vista = df.head(100).copy()
        df_vista.insert(0, "Estado", df_vista[col_pred].map({0: "✅ Cumple SLA", 1: "🚨 En Riesgo"}))
        st.markdown(f"**{titulo}**")
        st.dataframe(df_vista)
        if len(df) > 100:
            st.markdown(f"*Mostrando 100 de {len(df)} registros*")

    st.subheader("Tickets con Riesgo de Incumplimiento de SLA")
    if len(riesgo) > 0:
        mostrar_tabla(riesgo, "🔴 Tickets en Riesgo")
    else:
        st.info("No se detectaron tickets en riesgo de incumplimiento de SLA.")

    st.subheader("Todas las Predicciones")
    mostrar_tabla(predicciones, "📋 Vista General")
