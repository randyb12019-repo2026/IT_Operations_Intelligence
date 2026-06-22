# Módulo que renderiza la página de Comparación de Modelos Predictivos
import streamlit as st
import pandas as pd
import plotly.express as px

def comparacion_modelos(seccion, comparacion, col_modelo, col_f1):
    if seccion != "Comparación de Modelos":
        return

    st.header("Comparación de Modelos Predictivos")

    if comparacion is None:
        st.warning("No hay datos de comparación de modelos.")
        return

    st.dataframe(comparacion.round(4))

    metricas = [c for c in comparacion.columns if c.lower() not in ["modelo", "model"]]
    for metrica in metricas:
        fig = px.bar(comparacion, x=col_modelo, y=metrica,
                     title=f"Comparación de {metrica}",
                     color=metrica, color_continuous_scale="blues")
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#c8d6e5",
            xaxis_title="",
            yaxis_title=metrica
        )
        st.plotly_chart(fig)

    if col_f1 and col_modelo:
        mejor = comparacion.loc[comparacion[col_f1].idxmax()]
        st.markdown(f"""
        <div class="info-card">
        <h3>Modelo Recomendado: {mejor[col_modelo]}</h3>
        <p>F1-Score: <b>{mejor[col_f1]:.4f}</b></p>
        </div>
        """, unsafe_allow_html=True)
