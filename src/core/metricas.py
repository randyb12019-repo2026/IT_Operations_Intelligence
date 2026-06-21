# Módulo con funciones para calcular y obtener métricas a partir de los datos de incidencias
import pandas as pd

def obtener_media(df, posibles_columnas):
    for col in posibles_columnas:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            return round(df[col].mean(), 2), col
    return "N/D", None


def obtener_metricas(datos_incidencias, metricas_preferidas):
    metricas_disponibles = [col for col in metricas_preferidas if col in datos_incidencias.columns]
    if not metricas_disponibles:
        metricas_disponibles = datos_incidencias.select_dtypes(include="number").columns.tolist()
    return metricas_disponibles
