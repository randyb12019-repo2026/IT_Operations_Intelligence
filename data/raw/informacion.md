# Data Raw

## Descripción

Esta carpeta contiene los datos originales utilizados en el proyecto **IT Operations Intelligence**.

Los archivos aquí almacenados corresponden exactamente a la versión original del dataset, sin modificaciones, transformaciones ni procesos de limpieza previos.

## Fuente de Datos

El dataset utilizado puede descargarse desde Kaggle:

https://www.kaggle.com/datasets/shamiulislamshifat/it-incident-log

## Archivo Esperado

Una vez descargado, el archivo original debe almacenarse en esta carpeta para permitir la correcta ejecución de los notebooks y scripts del proyecto:

- `incident_event_log.csv` — Registro de incidencias IT con 36 variables y más de 141 mil registros

## Consideraciones

- No modificar los archivos almacenados en esta carpeta.
- Mantener una copia íntegra de los datos originales para garantizar la trazabilidad del análisis.
- Todas las transformaciones y procesos de limpieza deben realizarse sobre copias de trabajo en `data/processed`.

## Objetivo

Preservar la fuente de datos original utilizada durante el desarrollo del proyecto, garantizando la reproducibilidad y transparencia del flujo analítico.
