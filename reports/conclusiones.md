# Conclusiones Generales — IT Operations Intelligence

## Resumen del Proyecto

El objetivo de este proyecto fue analizar datos históricos de incidencias de soporte tecnológico y desarrollar un modelo predictivo capaz de identificar tickets con alto riesgo de incumplimiento de SLA (Service Level Agreement) antes de que la violación ocurra.

A través de un flujo completo de análisis de datos, preparación de variables, exploración estadística, ingeniería de características y modelado predictivo, se logró construir una solución capaz de detectar patrones asociados al incumplimiento de SLA dentro del entorno de operaciones IT.

---

## Principales Hallazgos

### Calidad de los Datos

- El dataset contenía **141,712 registros y 36 variables originales**, sin valores nulos significativos ni filas duplicadas.
- La transformación a formato datetime y la imputación de valores nulos con la mediana permitieron preparar los datos para el modelado de forma eficiente.
- Se descartaron variables identificativas (number, caller_id), fechas originales y metadatos no predictivos, reduciendo el espacio de características a **13 variables numéricas relevantes**.

### Desbalance de Clases

- **El 93.5% de los tickets cumplen con el SLA**, mientras que solo el **6.5% lo incumplen**.
- Este desbalance es inherente al dominio de soporte IT y requirió técnicas especializadas como **SMOTE** (Synthetic Minority Oversampling) y el uso de `class_weight='balanced'` para evitar que los modelos ignoren la clase minoritaria.
- Tras aplicar SMOTE, ambas clases quedaron equilibradas con **105,997 muestras cada una** en el conjunto de entrenamiento.

### Variables más Predictivas

Según el análisis de importancia del modelo Gradient Boosting:

| Variable | Importancia Relativa |
|---|---|
| `sys_mod_count` | **53.5%** |
| `resolution_time_hours` | **23.4%** |
| `reassignment_count` | **6.9%** |
| `problematic_ticket` | 4.2% |
| `priority_score` | 3.8% |
| `impact_score` | 2.9% |
| `urgency_score` | 2.5% |
| `criticality_score` | 1.8% |
| Otras | 1.0% |

**Conclusión clave:** El historial operativo del ticket (modificaciones, reasignaciones, tiempo de resolución) es significativamente más predictivo que sus metadatos estáticos (prioridad, impacto, urgencia).

### Feature Engineering

La creación de variables derivadas mejoró sustancialmente la capacidad predictiva:

- **Variables temporales:** `open_hour`, `open_dayofweek`, `open_month`, `open_year` — para capturar estacionalidad y patrones horarios.
- **Codificación ordinal:** `priority_score`, `impact_score`, `urgency_score` — preservando el orden intrínseco de cada variable.
- **Indicadores compuestos:** `criticality_score` (promedio de las tres puntuaciones ordinales) y `criticality_level` (Low/Medium/High).
- **Identificación de tickets problemáticos:** `problematic_ticket` = 1 si `reassignment_count > 2` o `reopen_count > 0`.
- **Métrica operacional:** `resolution_time_hours` calculada como la diferencia entre resolución y apertura.

### Rendimiento de Modelos

Se evaluaron **4 algoritmos de clasificación** con técnicas de balanceo y validación:

| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| Regresión Logística | 0.8028 | 0.9785 | 0.8068 | 0.8844 | 0.8526 |
| Random Forest | 0.8967 | 0.9502 | 0.9387 | 0.9444 | 0.8843 |
| **Gradient Boosting** | **0.9346** | **0.9369** | **0.9972** | **0.9661** | **0.9056** |
| Red Neuronal MLP | 0.9339 | 0.9382 | 0.9948 | 0.9657 | 0.8984 |

### Selección del Modelo Final

**Gradient Boosting** fue seleccionado como modelo final debido a:

- **Mejor F1-Score (0.9661):** El equilibrio más alto entre precisión y recall.
- **Mejor ROC-AUC (0.9056):** Excelente capacidad discriminativa entre clases.
- **Recall excepcional (99.72%):** Detecta casi la totalidad de los casos de cumplimiento de SLA.
- **Alta precisión (93.69%):** Baja tasa de falsos positivos.
- **Accuracy del 93.46%:** Rendimiento general sólido y consistente.

### Limitaciones Identificadas

A pesar del excelente rendimiento global, el modelo Gradient Boosting muestra limitaciones en la detección de la **clase minoritaria (incumplimiento de SLA)**, con un recall del 3% para esta clase. Esto significa que:

- La mayoría de los verdaderos incumplimientos no son detectados directamente.
- La **Regresión Logística** logró el mejor recall para la clase minoritaria (75%), aunque con menor precisión (21%).
- Se requieren estrategias complementarias como **optimización de umbrales de decisión** o **cost-sensitive learning** para mejorar la detección de incumplimientos sin sacrificar el rendimiento general.

---

## Conclusión Final

Los resultados obtenidos demuestran que los datos históricos de incidencias de soporte tecnológico contienen información suficiente para predecir el cumplimiento de SLA mediante técnicas de Machine Learning.

La utilización de modelos predictivos sobre indicadores operativos como el número de modificaciones del ticket, el tiempo de resolución y las reasignaciones puede servir como herramienta de apoyo para la **gestión proactiva de incidencias**, permitiendo:

- **Identificar tempranamente** tickets con alto riesgo de incumplimiento.
- **Priorizar recursos** de soporte hacia las incidencias más críticas.
- **Reducir tiempos de respuesta** mediante alertas automatizadas.
- **Mejorar la disponibilidad** y calidad de los servicios tecnológicos.

Este proyecto constituye una base sólida para futuros desarrollos orientados a sistemas de monitorización inteligente, mantenimiento predictivo y observabilidad de infraestructuras IT, con potencial de integración en plataformas de ticketing como ServiceNow o Jira.

---

## Trabajo Futuro

- Integración con sistemas de monitoreo en tiempo real para detección temprana de anomalías.
- Incorporación de análisis de texto (NLP) sobre descripciones de incidencias para extraer urgencia semántica.
- Desarrollo de un sistema de alertas automatizadas con umbrales configurables.
- Evaluación de técnicas avanzadas de deep learning para clasificación multilabel.
- Implementación de explicabilidad mediante SHAP/LIME para predicciones individuales.
- Dashboard interactivo con métricas de deriva del modelo (concept drift) y reentrenamiento automático.
