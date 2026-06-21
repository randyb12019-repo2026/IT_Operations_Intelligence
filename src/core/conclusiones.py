# Módulo que contiene los textos de conclusiones del proyecto y su función de visualización

TEXTOS_CONCLUSIONES = [
    ("1. Preparación y Transformación de los Datos",
     "Durante las fases iniciales del proyecto se realizó la exploración, validación y "
     "preparación del dataset de incidencias y tickets de soporte tecnológico. El conjunto de datos, "
     "con más de 141 mil registros y 36 variables, no presentó valores nulos significativos, "
     "lo que permitió centrar el trabajo en la transformación de variables temporales, "
     "codificación de variables categóricas e ingeniería de características orientadas a "
     "la predicción del cumplimiento de SLA (Service Level Agreement)."),
    ("2. Análisis Exploratorio de Datos",
     "El análisis exploratorio permitió comprender el comportamiento de las incidencias registradas "
     "en el sistema de ticketing, incluyendo su distribución por categoría, prioridad, impacto, "
     "urgencia, grupo de asignación y estado del ciclo de vida. Se identificó que el 93.5% de los "
     "tickets cumplieron con el SLA establecido, mientras que el 6.5% restante experimentaron "
     "incumplimientos. Las variables con mayor correlación con el incumplimiento de SLA fueron "
     "el nivel de prioridad, el número de reasignaciones y el estado final de la incidencia."),
    ("3. Modelo Predictivo",
     "Se entrenaron y evaluaron diferentes algoritmos de Machine Learning para predecir el "
     "incumplimiento de SLA en tickets de soporte tecnológico. La comparación de métricas "
     "permitió identificar al modelo con mejor rendimiento general para este problema de "
     "clasificación binaria, utilizando técnicas de balanceo de clases para manejar el "
     "desequilibrio entre tickets que cumplen y no cumplen el SLA."),
    ("4. Resultados Obtenidos",
     "El modelo seleccionado fue capaz de identificar tickets con alto riesgo de incumplimiento "
     "de SLA dentro del conjunto de datos analizado. Las métricas obtenidas durante la evaluación, "
     "junto con la matriz de confusión y el análisis de predicciones, permitieron validar el "
     "comportamiento del modelo y comprobar su capacidad para diferenciar entre tickets que "
     "cumplirían y no cumplirían el SLA establecido."),
    ("5. Aplicación Práctica",
     "El dashboard implementado permite visualizar indicadores operativos del servicio de soporte, "
     "revisar el comportamiento del modelo predictivo y consultar las incidencias con riesgo de "
     "incumplimiento de SLA, proporcionando una base sólida para la toma de decisiones en "
     "operaciones IT, gestión de servicios y optimización de procesos de soporte técnico."),
    ("6. Trabajo Futuro",
     "Como posibles líneas de mejora se plantea la incorporación de datos históricos adicionales, "
     "la integración con sistemas de monitoreo en tiempo real, la evaluación de técnicas avanzadas "
     "de deep learning para clasificación de textos descriptivos de incidencias, y el desarrollo "
     "de un sistema de alertas tempranas para la gestión proactiva de SLA.")
]

def conclusiones(seccion):
    if seccion != "Conclusiones":
        return
    import streamlit as st
    st.header("Conclusiones del Proyecto")
    textos = TEXTOS_CONCLUSIONES
    for titulo, cuerpo in textos:
        st.markdown(f"""
        <div class="info-card">
        <h3>{titulo}</h3>
        <p>{cuerpo}</p>
        </div>
        """, unsafe_allow_html=True)
