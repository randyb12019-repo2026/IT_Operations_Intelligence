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

    st.markdown("""
    <div style="font-size:0.85rem; color:#c8d6e5; background:#1a2d44; border-left:3px solid #2e86c1; padding:0.75rem 1rem; border-radius:0 4px 4px 0; margin-bottom:1rem;">
    La columna <b style="color:#00d4ff;">Predicción</b> indica si el modelo clasifica el ticket como
    <b style="color:#00d4ff;">Cumple SLA</b> (0) o <b style="color:#ff3355;">En Riesgo</b> (1).
    La columna <b style="color:#00d4ff;">Probabilidad</b> muestra el nivel de confianza del modelo
    en su predicción (0 a 1). Los tickets marcados como En Riesgo requieren
    atención prioritaria para evitar incumplimientos de SLA.
    </div>
    """, unsafe_allow_html=True)

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
    st.markdown("""
    <div style="font-size:0.85rem; color:#c8d6e5; background:#1a2d44; border-left:3px solid #ff3355; padding:0.75rem 1rem; border-radius:0 4px 4px 0; margin-bottom:0.75rem;">
    Estos son los tickets que el modelo predice con mayor probabilidad de
    incumplir el SLA. Se recomienda revisarlos y tomar acciones preventivas
    como reasignación prioritaria, escalamiento o contacto proactivo.
    </div>
    """, unsafe_allow_html=True)
    if len(riesgo) > 0:
        mostrar_tabla(riesgo, "🔴 Tickets en Riesgo")
    else:
        st.info("No se detectaron tickets en riesgo de incumplimiento de SLA.")

    st.subheader("Todas las Predicciones")
    mostrar_tabla(predicciones, "📋 Vista General")
