# Data Final

## Descripción

Esta carpeta contiene los resultados finales generados durante la fase de modelado predictivo del proyecto **IT Operations Intelligence**.

## Contenido

- `comparacion_modelos.csv` — Métricas de rendimiento (Accuracy, Precision, Recall, F1-Score, ROC-AUC) de los 4 modelos evaluados.
- `predicciones_incidencias.csv` — Predicciones completas del modelo final sobre el conjunto de prueba, incluyendo probabilidades.
- `incidentes_riesgo_sla.csv` — Subconjunto de tickets clasificados como en riesgo de incumplimiento de SLA.

## Modelo Seleccionado

Tras la evaluación de diferentes algoritmos de clasificación, **Gradient Boosting** fue seleccionado como modelo final debido a su mejor F1-Score (0.9661) y ROC-AUC (0.9056), demostrando el mejor equilibrio entre precisión y capacidad predictiva para la detección de incumplimientos de SLA.

## Objetivo

Garantizar la disponibilidad de los resultados finales del proyecto para su revisión, presentación y posible reutilización en futuros análisis o procesos de mejora continua dentro de la gestión de servicios IT.
