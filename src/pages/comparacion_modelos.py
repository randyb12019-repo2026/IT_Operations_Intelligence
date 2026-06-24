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

    st.markdown("""
    <div style="font-size:0.85rem; color:#c8d6e5; background:#1a2d44; border-left:3px solid #2e86c1; padding:0.75rem 1rem; border-radius:0 4px 4px 0; margin-bottom:1rem;">
    La tabla muestra las métricas de rendimiento de cada modelo evaluado sobre
    los datos de prueba. <b style="color:#00d4ff;">Accuracy</b> mide el porcentaje global de aciertos,
    <b style="color:#00d4ff;">Precision</b> la proporción de positivos correctos sobre el total de
    predicciones positivas, <b style="color:#00d4ff;">Recall</b> la capacidad de detectar los casos
    positivos reales, y <b style="color:#00d4ff;">F1-Score</b> el balance armónico entre Precision y
    Recall. Dado el desbalance de clases (6.5% de incumplimientos), el F1-Score
    es la métrica más representativa.
    </div>
    """, unsafe_allow_html=True)

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
