# Módulo que renderiza la página de Estado del Servicio con análisis detallado de incidencias
import streamlit as st
import pandas as pd
import plotly.express as px

def estado_infraestructura(seccion, datos_incidencias):
    if seccion != "Estado del Servicio":
        return

    st.header("Estado del Servicio de Soporte")

    if datos_incidencias is None:
        st.warning("No hay datos disponibles.")
        return

    col1, col2 = st.columns(2)

    with col1:
        if "priority" in datos_incidencias.columns:
            st.subheader("Distribución por Prioridad")
            priority_order = ["1 - Critical", "2 - High", "3 - Moderate", "4 - Low"]
            prio_data = datos_incidencias["priority"].value_counts().reindex(
                [p for p in priority_order if p in datos_incidencias["priority"].value_counts().index]
            ).reset_index()
            prio_data.columns = ["Prioridad", "Cantidad"]
            colors = {"1 - Critical": "#ff3355", "2 - High": "#ffaa00",
                      "3 - Moderate": "#00d4ff", "4 - Low": "#00ff88"}
            fig = px.bar(prio_data, x="Prioridad", y="Cantidad",
                         color="Prioridad",
                         color_discrete_map=colors,
                         title="Tickets por Prioridad")
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                            font_color="#c8d6e5", showlegend=False)
            st.plotly_chart(fig)

    with col2:
        if "incident_state" in datos_incidencias.columns:
            st.subheader("Estado de Incidencias")
            state_data = datos_incidencias["incident_state"].value_counts().reset_index()
            state_data.columns = ["Estado", "Cantidad"]
            state_data = state_data.sort_values("Cantidad", ascending=False).head(8)
            state_colors = {"New": "#00d4ff", "Active": "#ffaa00", "Resolved": "#00ff88",
                           "Closed": "#6b7280", "Awaiting User Info": "#ff7733",
                           "Awaiting Vendor": "#cc66ff", "Awaiting Problem": "#ff3355",
                           "Awaiting Evidence": "#ffcc00"}
            fig = px.bar(state_data, x="Estado", y="Cantidad",
                         color="Estado",
                         color_discrete_map=state_colors,
                         title="Distribución por Estado")
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                            font_color="#c8d6e5", showlegend=False)
            st.plotly_chart(fig)

    if "category" in datos_incidencias.columns:
        st.subheader("Top 10 Categorías de Incidencias")
        cat_data = datos_incidencias["category"].value_counts().head(10).reset_index()
        cat_data.columns = ["Categoría", "Cantidad"]
        fig = px.bar(cat_data, x="Cantidad", y="Categoría", orientation="h",
                     title="Incidencias por Categoría",
                     color="Cantidad", color_continuous_scale="blues")
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                         font_color="#c8d6e5", yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig)

    if all(c in datos_incidencias.columns for c in ["impact", "urgency"]):
        st.subheader("Matriz Impacto vs Urgencia")
        matrix = pd.crosstab(datos_incidencias["impact"], datos_incidencias["urgency"])
        fig = px.imshow(matrix, text_auto=True, aspect="auto",
                        title="Impacto vs Urgencia",
                        color_continuous_scale="blues")
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                         font_color="#c8d6e5")
        st.plotly_chart(fig)

    if "assignment_group" in datos_incidencias.columns:
        st.subheader("Grupos de Asignación (Top 10)")
        group_data = datos_incidencias["assignment_group"].value_counts().head(10).reset_index()
        group_data.columns = ["Grupo", "Cantidad"]
        fig = px.bar(group_data, x="Cantidad", y="Grupo", orientation="h",
                     title="Tickets por Grupo de Asignación",
                     color="Cantidad", color_continuous_scale="greens")
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                         font_color="#c8d6e5", yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig)
