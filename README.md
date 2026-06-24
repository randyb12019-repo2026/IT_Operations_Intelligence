# IT Operations Intelligence

## Sistema de Análisis de Incidencias y Tickets de Soporte Tecnológico

Proyecto de análisis de datos y aprendizaje automático orientado al estudio de patrones de fallos, tiempos de resolución, categorías de incidencias y generación de recomendaciones para optimizar las operaciones y la gestión de servicios informáticos.

---

## Instalación

### Requisitos

- Python 3.10+
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/randyb12019-repo2026/IT_Operations_Intelligence.git
cd IT_Operations_Intelligence

# 2. Crear y activar entorno virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. (Opcional) Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# 5. Descargar el dataset desde Kaggle y colocarlo en:
#    data/raw/incident_event_log.csv
#    Fuente: https://www.kaggle.com/datasets/shamiulislamshifat/it-incident-log-dataset

# 6. Ejecutar los notebooks en orden:
#    notebooks/01_exploracion_y_limpieza_dataset.ipynb
#    notebooks/02_transformacion_y_feature_engineering.ipynb
#    notebooks/03_analisis_exploratorio_EDA.ipynb
#    notebooks/04_modelo_predictivo.ipynb
#    notebooks/05_exportacion_resultados.ipynb

# 7. Lanzar el dashboard
streamlit run app/streamlit_app.py

# 8. (Opcional) Ejecutar tests
.venv\Scripts\python.exe -m pytest tests/ -v
```

> **Nota:** GitHub rechaza archivos .pkl por seguridad, por lo que el modelo models/modelo_sla.pkl está excluido del repositorio (.gitignore). Debes generar este archivo ejecutando los notebooks localmente (paso 6). Sin este archivo, el dashboard mostrará un mensaje indicando que no se encontró el modelo, pero el resto de la aplicación funciona con normalidad.

### Con Docker

```bash
# 1. Construir la imagen
docker build -t it-operations-intelligence .

# 2. Ejecutar el contenedor
docker run -p 8501:8501 it-operations-intelligence
```

Luego abrir http://localhost:8501 en el navegador.

---

## Descripción del Proyecto

Los sistemas de ticketing y gestión de incidencias generan continuamente datos sobre el estado del servicio de soporte tecnológico. La capacidad de predecir qué tickets tienen mayor probabilidad de incumplir los SLAs permite a los equipos de operaciones IT tomar acciones proactivas para mejorar la calidad del servicio.

Este proyecto aplica técnicas de análisis de datos y Machine Learning para identificar variables relacionadas con el incumplimiento de SLA y desarrollar modelos predictivos capaces de anticipar posibles desviaciones en el servicio de soporte.

---

## Objetivo General

Analizar los registros históricos de incidencias de soporte tecnológico para identificar los factores asociados al incumplimiento de SLA y desarrollar modelos predictivos orientados a la gestión proactiva de incidencias.

---

## Problema de Negocio

Los equipos de soporte IT suelen reaccionar una vez que el SLA ya se ha incumplido.

La pregunta principal que intenta responder este proyecto es:

> ¿Es posible predecir qué tickets de soporte tecnológico tienen mayor probabilidad de incumplir el SLA, permitiendo una intervención temprana?

---

## Dataset

### Fuente

Dataset: **IT Incident Log Dataset**

Enlace: [https://www.kaggle.com/datasets/shamiulislamshifat/it-incident-log-dataset](https://www.kaggle.com/datasets/shamiulislamshifat/it-incident-log-dataset)

### Características

- 141.712 registros
- 36 variables originales
- Datos estructurados de sistema de ticketing ITSM
- Sin valores nulos significativos
- Variables temporales, categóricas y numéricas

### Variables Principales

| Variable | Descripción |
|---|---|
| number | Número de incidencia |
| incident_state | Estado actual de la incidencia |
| category | Categoría de la incidencia |
| subcategory | Subcategoría de la incidencia |
| priority | Prioridad (1-Critical a 4-Low) |
| impact | Impacto (1-High a 3-Low) |
| urgency | Urgencia (1-High a 3-Low) |
| assignment_group | Grupo asignado |
| reassignment_count | Número de reasignaciones |
| reopen_count | Número de reaperturas |
| made_sla | Indicador de cumplimiento de SLA |
| opened_at | Fecha de apertura |
| resolved_at | Fecha de resolución |
| closed_at | Fecha de cierre |

---

## Arquitectura del Proyecto

```
Dataset Original (IT Incident Log)
         |
         ▼
Exploración y Limpieza (Notebook 01)
         |
         ▼
Transformación y Feature Engineering (Notebook 02)
         |
         ▼
Análisis Exploratorio de Datos - EDA (Notebook 03)
         |
         ▼
Modelado Predictivo (Notebook 04)
         |
         ▼
Exportación de Resultados y Conclusiones (Notebook 05)
```

---

## Ciclo de Vida del Proyecto

```
Comprensión del Negocio
         |
         ▼
Comprensión de los Datos
         |
         ▼
Limpieza de Datos
         |
         ▼
Transformación de Datos
         |
         ▼
Ingeniería de Características
         |
         ▼
Análisis Exploratorio
         |
         ▼
Modelado Predictivo
         |
         ▼
Evaluación
         |
         ▼
Insights
         |
         ▼
Conclusiones
```

---

## Fases del Proyecto

### Fase 1. Comprensión del Negocio

**Actividades:**
- Definición del problema a resolver
- Objetivos del proyecto
- Alcance del proyecto

### Fase 2. Comprensión de los Datos

**Actividades:**
- Carga del dataset IT Incident Log
- Validación de la estructura general
- Verificación de calidad de datos
- Validación de tipos de datos

### Fase 3. Limpieza de Datos

**Actividades:**
- Verificación de valores nulos
- Detección de duplicados
- Validación de integridad

### Fase 4. Transformación de Datos

**Actividades:**
- Conversión de fechas a formato datetime
- Extracción de características temporales (hora, día, mes)
- Cálculo de tiempo de resolución
- Codificación de variables ordinales (prioridad, impacto, urgencia)

### Fase 5. Ingeniería de Características

**Nuevas variables:**
- priority_score, impact_score, urgency_score (codificación numérica)
- criticality_score (indicador compuesto de criticidad)
- resolution_time_hours (tiempo de resolución en horas)
- problematic_ticket (indicador de ticket problemático)

### Fase 6. Análisis Exploratorio de Datos (EDA)

**Análisis realizados:**
- Univariante: histogramas, distribuciones, boxplots
- Bivariante: prioridad vs SLA, reasignaciones vs SLA
- Correlaciones: identificación de variables más relacionadas con SLA
- Análisis temporal: incumplimiento por hora del día

### Fase 7. Preparación para Machine Learning

**Actividades:**
- Definición de variable objetivo (made_sla)
- Selección de características
- División Train/Test (80/20)
- Escalado de variables (StandardScaler)
- Balanceo de clases (SMOTE)

### Fase 8. Modelado Predictivo

**Modelos evaluados:**

- **Regresión Logística**: Modelo base para clasificación binaria con balanceo de clases
- **Random Forest**: Modelo basado en árboles de decisión con 200 estimadores
- **Gradient Boosting**: Modelo de boosting con 200 estimadores y profundidad 5
- **Red Neuronal MLP**: Red neuronal multicapa con 3 capas ocultas (64, 32, 16)

### Fase 9. Evaluación de Modelos

**Métricas:**
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

### Fase 10. Interpretación de Resultados

**Aspectos analizados:**
- Variables más influyentes
- Comportamiento de los incidentes
- Capacidad predictiva del modelo

### Fase 11. Insights de Negocio

**Hallazgo 1:** La prioridad del ticket es el factor más determinante en el cumplimiento de SLA.

**Hallazgo 2:** El número de reasignaciones está fuertemente correlacionado con el incumplimiento de SLA.

**Hallazgo 3:** El tiempo de resolución es un indicador clave del cumplimiento de SLA.

**Hallazgo 4:** La combinación de impacto, urgencia y prioridad (criticality_score) ofrece mejor capacidad predictiva.

### Fase 12. Conclusiones y Recomendaciones

**Conclusiones:**
- Los datos históricos de incidencias contienen información valiosa para predecir SLA
- Los modelos predictivos permiten identificar tickets con riesgo de incumplimiento
- La ingeniería de características mejora significativamente la capacidad predictiva

**Recomendaciones:**
- Implementar alertas tempranas para tickets con alta probabilidad de incumplimiento
- Revisar procesos de asignación para reducir reasignaciones
- Monitorear categorías con mayor tasa de incumplimiento
- Integrar el modelo predictivo con el sistema de ticketing

---

## Tecnologías Utilizadas

### Lenguaje
- Python

### Análisis de Datos
- Pandas
- NumPy

### Visualización
- Matplotlib
- Seaborn
- Plotly

### Machine Learning
- Scikit-Learn
- Imbalanced-Learn (SMOTE)

### Dashboard
- Streamlit

### Testing
- pytest

## Estructura del Proyecto

```
IT_Operations_Intelligence/
│
├── app/
│   └── streamlit_app.py
│
├── dashboard/
│   ├── __init__.py
│   └── dashboard.py
│
├── data/
│   ├── raw/
│   │   └── incident_event_log.csv
│   ├── processed/
│   │   └── incident_event_log_transformado.csv
│   └── final/
│       ├── comparacion_modelos.csv
│       ├── predicciones_incidencias.csv
│       └── incidentes_riesgo_sla.csv
│
├── models/
│   └── modelo_sla.pkl
│
├── notebooks/
│   ├── 01_exploracion_y_limpieza_dataset.ipynb
│   ├── 02_transformacion_y_feature_engineering.ipynb
│   ├── 03_analisis_exploratorio_EDA.ipynb
│   ├── 04_modelo_predictivo.ipynb
│   └── 05_exportacion_resultados.ipynb
│
├── reports/
│   └── graphics/
│
├── src/
│   ├── core/
│   │   ├── datos.py
│   │   ├── detectores.py
│   │   ├── metricas.py
│   │   └── conclusiones.py
│   ├── ui/
│   │   ├── cabecera.py
│   │   ├── estilos.py
│   │   ├── plantilla.py
│   │   └── sidebar.py
│   ├── pages/
│   │   ├── resumen_ejecutivo.py
│   │   ├── estado_infraestructura.py
│   │   ├── comparacion_modelos.py
│   │   └── predicciones.py
│   └── export/
│       ├── presentacion.py
│       └── generar_presentacion.py
│
├── tests/
│
├── LICENCE.md
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── Dockerfile
```

---

## Correspondencia entre Fases y Notebooks

| Fase | Descripción | Notebook |
|---|---|---|
| Fase 1 | Comprensión del Negocio | 01_exploracion_y_limpieza_dataset.ipynb y README |
| Fase 2 | Comprensión de los Datos | 01_exploracion_y_limpieza_dataset.ipynb |
| Fase 3 | Exploración Inicial de los Datos | 01_exploracion_y_limpieza_dataset.ipynb |
| Fase 4 | Limpieza y Preparación de Datos | 01_exploracion_y_limpieza_dataset.ipynb |
| Fase 5 | Transformación y Feature Engineering | 02_transformacion_y_feature_engineering.ipynb |
| Fase 6 | Análisis Exploratorio de Datos (EDA) | 03_analisis_exploratorio_EDA.ipynb |
| Fase 7 | Preparación para Machine Learning | 04_modelo_predictivo.ipynb |
| Fase 8 | Modelado Predictivo | 04_modelo_predictivo.ipynb |
| Fase 9 | Comparación y Evaluación de Modelos | 04_modelo_predictivo.ipynb |
| Fase 10 | Interpretación de Resultados | 04_modelo_predictivo.ipynb |
| Fase 11 | Exportación y Validación de Resultados | 05_exportacion_resultados.ipynb |
| Fase 12 | Conclusiones y Recomendaciones | 05_exportacion_resultados.ipynb y README |

---

## Principales Beneficios

### Beneficios Operativos
- Identificación temprana de tickets con riesgo de incumplimiento de SLA
- Mejora en la priorización de incidencias
- Optimización de la asignación de recursos de soporte
- Reducción del tiempo de respuesta ante incidencias críticas

### Beneficios Estratégicos
- Toma de decisiones basada en datos históricos
- Incremento en la tasa de cumplimiento de SLA
- Mejora continua de procesos de soporte IT

---

## Competencias Aplicadas

- Análisis Exploratorio de Datos
- Limpieza y Transformación de Datos
- Ingeniería de Características
- Estadística Descriptiva
- Machine Learning Supervisado
- Evaluación de Modelos
- Interpretación de Resultados
- Comunicación de Insights

---

## Líneas Futuras

- Implementación de detección de anomalías en tiempo real
- Integración con sistemas SIEM y de ticketing (ServiceNow, Jira)
- Incorporación de análisis de texto descriptivo de incidencias (NLP)
- Desarrollo de sistema de alertas predictivas automatizadas
- Integración con herramientas de observabilidad (Datadog, Grafana)

---

## Autor

Proyecto desarrollado como trabajo final del Bootcamp de Data Analytics e Inteligencia Artificial.

**Autor:** Randy Bonucci Martín

**Especialización:** Data Analytics, Infraestructuras IT y Machine Learning.

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo LICENCE.md para más detalles.
