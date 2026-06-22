# Módulo que renderiza la página de Resumen Ejecutivo con métricas clave y gráficos
import streamlit as st
import pandas as pd
import plotly.express as px

def resumen_ejecutivo(seccion, datos_filt, comparacion, col_f1, col_modelo,
                      tickets_totales, sla_cumplimiento_pct, tickets_riesgo,
                      tiempo_medio_resolucion):
    if seccion != "Resumen Ejecutivo":
        return

    st.header("Resumen Ejecutivo")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Tickets", f"{tickets_totales:,}" if tickets_totales else "N/D")
    with col2:
        st.metric("SLA Cumplimiento", f"{sla_cumplimiento_pct}%" if sla_cumplimiento_pct else "N/D")
    with col3:
        st.metric("Tickets en Riesgo", f"{tickets_riesgo:,}" if tickets_riesgo is not None else "N/D")
    with col4:
        st.metric("Tiempo Medio Resolución", tiempo_medio_resolucion if tiempo_medio_resolucion else "N/D")

    if comparacion is not None and col_modelo and col_f1:
        st.subheader("Rendimiento de Modelos")
        mejor = comparacion.loc[comparacion[col_f1].idxmax()]
        st.markdown(f"""
        <div class="info-card">
        <h3>Mejor Modelo: {mejor[col_modelo]}</h3>
        <p>F1-Score: <b>{mejor[col_f1]:.4f}</b></p>
        </div>
        """, unsafe_allow_html=True)

        fig = px.bar(comparacion, x=col_modelo, y=col_f1,
                     title="Comparación de F1-Score por Modelo",
                     color=col_f1, color_continuous_scale="blues")
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#c8d6e5",
            xaxis_title="",
            yaxis_title="F1-Score"
        )
        st.plotly_chart(fig)

    if datos_filt is not None and "made_sla" in datos_filt.columns:
        st.subheader("Distribución de Cumplimiento de SLA")
        dist = datos_filt["made_sla"].value_counts().reset_index()
        dist.columns = ["Cumple SLA", "Cantidad"]
        dist["Cumple SLA"] = dist["Cumple SLA"].map({True: "Cumple SLA", False: "No Cumple SLA"})
        fig = px.pie(dist, values="Cantidad", names="Cumple SLA",
                      title="Cumplimiento de SLA (Datos Filtrados)",
                      color_discrete_sequence=["#00ff88", "#ff3355"])
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#c8d6e5"
        )
        st.plotly_chart(fig)
