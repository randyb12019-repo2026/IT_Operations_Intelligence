# Data Processed

## Descripción

Esta carpeta contiene los datos resultantes del proceso de limpieza, transformación y enriquecimiento realizado sobre los datos originales de incidencias IT.

## Transformaciones Realizadas

- Conversión de columnas de fecha a tipo datetime para extracción de componentes temporales.
- Creación de variables derivadas: `open_hour`, `open_dayofweek`, `open_month`, `open_year`.
- Cálculo de `resolution_time_hours` a partir de fechas de apertura y resolución.
- Codificación ordinal de `priority`, `impact` y `urgency` a valores numéricos.
- Generación de `criticality_score` como promedio de puntuaciones de impacto, urgencia y prioridad.
- Clasificación de `criticality_level` en categorías Low, Medium, High.
- Identificación de `problematic_ticket` basado en reasignaciones y reaperturas.
- Conversión de la variable objetivo `made_sla` a formato numérico (`made_sla_num`).

## Características

- 48 columnas (36 originales + 12 nuevas variables).
- 141,712 registros sin duplicados.
- Datos preparados para análisis exploratorio y modelado predictivo.

## Uso

Estos datos son utilizados durante las fases de análisis exploratorio, generación de insights y entrenamiento de modelos de Machine Learning para la predicción del cumplimiento de SLA.
