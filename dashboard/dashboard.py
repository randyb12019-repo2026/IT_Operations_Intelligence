# Módulo principal del dashboard que coordina la carga de datos, la navegación y el renderizado de páginas
import streamlit as st
from src.ui.estilos import estilos
from src.core.datos import carga_datos, validar_datos
from src.core.detectores import detectar_columna_prediccion, detectar_columna_modelo, detectar_columna_f1

from src.ui.sidebar import sidebar
from src.ui.cabecera import cabecera
from src.pages.resumen_ejecutivo import resumen_ejecutivo
from src.pages.estado_infraestructura import estado_infraestructura
from src.pages.comparacion_modelos import comparacion_modelos
from src.pages.predicciones import predicciones as mostrar_predicciones
from src.core.conclusiones import conclusiones

def mostrar_dashboard():
    estilos()
    comparacion, predicciones, datos_incidencias = carga_datos()
    validar_datos(comparacion, predicciones, datos_incidencias)

    col_pred = detectar_columna_prediccion(predicciones)
    col_modelo = detectar_columna_modelo(comparacion)
    col_f1 = detectar_columna_f1(comparacion)

    seccion, filtro_col, filtro_val = sidebar(datos_incidencias)

    if filtro_col and filtro_val:
        datos_filt = datos_incidencias[datos_incidencias[filtro_col] == filtro_val].copy()
        if filtro_col in predicciones.columns:
            predicciones_filt = predicciones[predicciones[filtro_col] == filtro_val].copy()
        else:
            predicciones_filt = predicciones
    else:
        datos_filt = datos_incidencias
        predicciones_filt = predicciones

    cabecera()

    # Métricas desde datos filtrados
    tickets_totales = len(datos_filt)

    sla_pct = None
    if "made_sla" in datos_filt.columns:
        sla_vals = datos_filt["made_sla"].value_counts(normalize=True)
        if True in sla_vals.index:
            sla_pct = round(sla_vals[True] * 100, 1)

    tickets_riesgo = None
    if "made_sla" in datos_filt.columns:
        tickets_riesgo = int((datos_filt["made_sla"] == False).sum())

    tiempo_medio = None
    if "resolution_time_hours" in datos_filt.columns:
        tiempo_medio = round(datos_filt["resolution_time_hours"].mean(), 1)
        tiempo_medio = f"{tiempo_medio}h"

    resumen_ejecutivo(seccion, datos_filt, comparacion, col_f1, col_modelo,
                      tickets_totales, sla_pct, tickets_riesgo, tiempo_medio)

    estado_infraestructura(seccion, datos_filt)
    comparacion_modelos(seccion, comparacion, col_modelo, col_f1)
    mostrar_predicciones(seccion, predicciones_filt, col_pred)
    conclusiones(seccion)

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; font-size:13px; color:#6b7280;' "
        "title='Este proyecto se distribuye bajo licencia MIT. Consulte el archivo LICENCE.md para más detalles.'>"
        "<b>IT Operations Intelligence</b> | "
        "Licencia MIT ⓘ | Desarrollado por Ing. Randy Bonucci Martin"
        "</div>",
        unsafe_allow_html=True,
    )

__all__ = ["mostrar_dashboard"]
