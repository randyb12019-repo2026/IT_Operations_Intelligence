# Módulo que genera la barra lateral con navegación y filtros de datos
import streamlit as st
import pandas as pd

def sidebar(datos_incidencias):
    seccion = st.sidebar.radio(
        "Navegación",
        [
            "Resumen Ejecutivo",
            "Estado del Servicio",
            "Comparación de Modelos",
            "Predicciones",
            "Conclusiones"
        ]
    )

    filtro_col = None
    filtro_val = None

    if datos_incidencias is not None:
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Filtros")
        st.sidebar.markdown("""
        <div style="font-size:0.7rem; color:#6b7280; margin-bottom:0.5rem;">
        Aplica a: Resumen Ejecutivo, Estado del Servicio
        </div>
        """, unsafe_allow_html=True)

        cols_disponibles = ["category", "priority", "impact", "urgency", "incident_state", "assignment_group"]
        cols_existentes = [c for c in cols_disponibles if c in datos_incidencias.columns]

        if cols_existentes:
            col_elegida = st.sidebar.selectbox("Variable de filtro", [""] + cols_existentes)
            if col_elegida:
                valores = datos_incidencias[col_elegida].dropna().unique().tolist()
                if valores:
                    val_elegido = st.sidebar.selectbox("Valor", sorted(valores))
                    filtro_col = col_elegida
                    filtro_val = val_elegido

    if filtro_col and filtro_val:
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        <div style="font-size:0.75rem; color:#00d4ff; font-family:'Share Tech Mono',monospace; border:1px solid #00d4ff33; padding:0.5rem; border-radius:4px;">
        <b>FILTRO ACTIVO:</b> {} = {}<br>
        <span style="color:#6b7280;">Aplica a: Resumen Ejecutivo, Estado del Servicio</span>
        </div>
        """.format(filtro_col, filtro_val), unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="font-size:0.75rem; color:#6b7280;">
    <b>IT Operations Intelligence</b><br>
    Análisis predictivo de incidencias<br>
    y cumplimiento de SLA
    </div>
    """, unsafe_allow_html=True)

    return seccion, filtro_col, filtro_val
