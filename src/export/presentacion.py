"""
Generación de PDF del proyecto IT Operations Intelligence.
"""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import pandas as pd
from src.core.conclusiones import TEXTOS_CONCLUSIONES

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas


# Colores corporativos
AZUL_OSCURO  = HexColor("#0D1B2A")
AZUL_MEDIO   = HexColor("#1B3A5C")
AZUL_CLARO   = HexColor("#2E86C1")
CELESTE      = HexColor("#00D4FF")
BLANCO       = HexColor("#FFFFFF")
GRIS         = HexColor("#6C757D")
GRIS_CLARO   = HexColor("#D0D7DE")
VERDE        = HexColor("#00FF88")
ROJO         = HexColor("#FF3355")
NARANJA      = HexColor("#F39C12")

PAGE_W, PAGE_H = landscape(letter)  # 11 x 8.5 in
MARGIN = 0.8 * inch
CONTENT_W = PAGE_W - 2 * MARGIN


def _draw_bg(c, color=AZUL_OSCURO):
    c.setFillColor(color)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def _draw_accent_bar(c, y, color=CELESTE):
    c.setFillColor(color)
    c.rect(MARGIN, y, CONTENT_W, 4, fill=1, stroke=0)


def _draw_title(c, text, y, size=28, color=BLANCO):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", size)
    c.drawString(MARGIN, y, text)
    _draw_accent_bar(c, y - 12, AZUL_CLARO)


def _draw_text(c, text, x, y, size=16, color=BLANCO, bold=False, max_width=None, leading=None):
    if not text:
        return y
    c.setFillColor(color)
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    if max_width:
        words = text.split(" ")
        line = ""
        line_y = y
        lh = leading or (size * 1.4)
        for w in words:
            test = f"{line} {w}".strip()
            if c.stringWidth(test, "Helvetica-Bold" if bold else "Helvetica", size) > max_width:
                c.drawString(x, line_y, line)
                line_y -= lh
                line = w
            else:
                line = test
        if line:
            c.drawString(x, line_y, line)
        return line_y - lh
    else:
        c.drawString(x, y, text)
        return y


def _draw_bullets(c, items, x, y, size=14, color=BLANCO, max_width=None):
    c.setFillColor(color)
    c.setFont("Helvetica", size)
    lh = size * 1.5
    cy = y
    for item in items:
        text = f"\u2022 {item}"
        if max_width and c.stringWidth(text, "Helvetica", size) > max_width:
            cy = _draw_text(c, text, x, cy, size, color, max_width=max_width, leading=lh)
            cy -= lh
        else:
            c.drawString(x, cy, text)
            cy -= lh
    return cy


def _draw_table(c, data, x, y, col_widths=None):
    rows, cols = len(data), len(data[0])
    if col_widths is None:
        col_widths = [CONTENT_W / cols] * cols
    row_height = 24
    table_w = sum(col_widths)
    table_h = rows * row_height

    # Header row
    c.setFillColor(AZUL_CLARO)
    c.setStrokeColor(GRIS_CLARO)
    c.setLineWidth(0.5)
    c.rect(x, y - row_height, table_w, row_height, fill=1, stroke=1)
    for j, val in enumerate(data[0]):
        cx = x + sum(col_widths[:j])
        c.setFillColor(BLANCO)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(cx + 4, y - row_height + 7, str(val))

    # Data rows
    for i in range(1, rows):
        ry = y - (i + 1) * row_height
        c.setFillColor(BLANCO)
        c.rect(x, ry, table_w, row_height, fill=1, stroke=0)
        c.setStrokeColor(GRIS_CLARO)
        c.setLineWidth(0.5)
        c.rect(x, ry, table_w, row_height, fill=0, stroke=1)
        for j, val in enumerate(data[i]):
            cx = x + sum(col_widths[:j])
            c.setFillColor(AZUL_OSCURO)
            c.setFont("Helvetica", 11)
            c.drawString(cx + 4, ry + 7, str(val))

    return y - rows * row_height


# === DECORACIONES IT ===

def _draw_shield(c, cx, cy, size=60, color=CELESTE):
    s = size
    c.setStrokeColor(color)
    c.setLineWidth(2)
    p = c.beginPath()
    p.moveTo(cx, cy + s)
    p.lineTo(cx - s, cy + s * 0.3)
    p.lineTo(cx - s * 0.7, cy - s * 0.5)
    p.lineTo(cx, cy - s * 0.8)
    p.lineTo(cx + s * 0.7, cy - s * 0.5)
    p.lineTo(cx + s, cy + s * 0.3)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    # Checkmark
    c.setStrokeColor(VERDE)
    c.setLineWidth(3)
    c.line(cx - s * 0.3, cy - s * 0.1, cx - s * 0.1, cy + s * 0.2)
    c.line(cx - s * 0.1, cy + s * 0.2, cx + s * 0.4, cy - s * 0.3)


def _draw_circuit_lines(c, x, y, count=3, spacing=20, color=CELESTE):
    c.setStrokeColor(color)
    c.setLineWidth(1)
    for i in range(count):
        cy = y - i * spacing
        c.line(x, cy, x + 30, cy)
        c.line(x + 30, cy, x + 30, cy - spacing // 2)
        c.circle(x + 30, cy - spacing // 2, 2, fill=1, stroke=0)


def _draw_footer(c, text="IT Operations Intelligence"):
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, 0.3 * inch, text)
    c.drawRightString(PAGE_W - MARGIN, 0.3 *inch, "Confidencial")


# ============================================================
# SLIDE DRAWERS
# ============================================================

def _slide_01_portada(c):
    _draw_bg(c)
    _draw_circuit_lines(c, MARGIN, PAGE_H - 1.3 * inch, 4, 25, CELESTE)
    _draw_circuit_lines(c, PAGE_W - MARGIN - 30, PAGE_H - 1.3 * inch, 4, 25, CELESTE)
    _draw_shield(c, PAGE_W / 2, PAGE_H - 2.2 * inch, 80, CELESTE)
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 3.5 * inch,
                        "IT Operations Intelligence")
    c.setFillColor(CELESTE)
    c.setFont("Helvetica", 18)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 4.2 * inch,
                        "Predicción de incumplimiento de SLA en tickets")
    c.drawCentredString(PAGE_W / 2, PAGE_H - 4.6 * inch,
                        "de soporte tecnológico mediante Machine Learning")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 5.5 * inch,
                        "Análisis  .  Transformación  .  Modelado Predictivo")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 12)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 6.3 * inch,
                        "Autor: Ing. Randy Bonucci Martin")
    _draw_footer(c)


def _slide_02_problema(c):
    _draw_bg(c)
    _draw_title(c, "Problema y Objetivo del Proyecto", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Los equipos de soporte IT gestionan miles de tickets de incidencias con",
        "plazos de respuesta estrictos definidos en Acuerdos de Nivel de Servicio (SLA)",
        "Actualmente reaccionan cuando el SLA ya se ha incumplido, generando",
        "multas, insatisfacción del cliente y deterioro de la calidad del servicio",
        "No existe una herramienta que permita identificar proactivamente los",
        "tickets con alto riesgo de incumplimiento antes de que ocurra",
    ], MARGIN, PAGE_H - 2.0 * inch, 14, BLANCO, CONTENT_W)
    _draw_text(c, "Objetivo General:", MARGIN, PAGE_H - 4.4 * inch,
               18, CELESTE, True)
    _draw_text(c, "Desarrollar modelos predictivos que permitan la detección temprana"
                  " de tickets con riesgo de incumplimiento de SLA a partir de datos"
                  " históricos de incidencias, facilitando la gestión proactiva del"
                  " soporte tecnológico y la reducción de violaciones de servicio.",
               MARGIN, PAGE_H - 4.9 * inch, 14, BLANCO, max_width=CONTENT_W)
    _draw_footer(c)


def _slide_03_dataset(c):
    _draw_bg(c)
    _draw_title(c, "El Dataset", PAGE_H - 1.0 * inch)
    _draw_text(c, "IT Incident Event Log",
               MARGIN, PAGE_H - 1.8 * inch, 16, CELESTE, True)
    _draw_table(c, [
        ["Característica", "Valor"],
        ["Registros", "141,712"],
        ["Variables originales", "36"],
        ["Variables tras feature engineering", "48"],
        ["Valores nulos significativos", "No"],
        ["Registros duplicados", "0"],
        ["Variable objetivo", "made_sla (Cumple SLA = True/False)"],
    ], MARGIN, PAGE_H - 2.2 * inch, [2.8 * inch, 3.0 * inch])
    _draw_text(c, "Distribución de la variable objetivo:",
               MARGIN, PAGE_H - 5.2 * inch, 16, CELESTE, True)
    _draw_text(c, "Cumple SLA (True)   :  132,497 registros (93.5 %)",
               MARGIN, PAGE_H - 5.6 * inch, 14, VERDE)
    _draw_text(c, "No Cumple SLA (False):    9,215 registros  (6.5 %)",
               MARGIN, PAGE_H - 6.0 * inch, 14, ROJO)
    _draw_text(c, "ATENCIÓN: Fuerte desbalance de clases",
               MARGIN + 4.5 * inch, PAGE_H - 5.2 * inch, 14, NARANJA, True)
    _draw_text(c, "- Comportamiento realista en entornos IT",
               MARGIN + 4.5 * inch, PAGE_H - 5.6 * inch, 12, NARANJA)
    _draw_text(c, "  (el incumplimiento es un evento minoritario)",
               MARGIN + 4.5 * inch, PAGE_H - 5.9 * inch, 12, NARANJA)
    _draw_footer(c)


def _slide_04_eda(c):
    _draw_bg(c)
    _draw_title(c, "Hallazgos del Análisis Exploratorio", PAGE_H - 1.0 * inch)
    _draw_text(c, "Correlación con el cumplimiento de SLA (made_sla_num):",
               MARGIN, PAGE_H - 1.8 * inch, 16, CELESTE, True)
    _draw_table(c, [
        ["Variable", "Correlación"],
        ["sys_mod_count", "-0.24"],
        ["reassignment_count", "-0.09"],
        ["resolution_time_hours", "-0.07"],
        ["problematic_ticket", "-0.06"],
        ["reopen_count", "-0.04"],
        ["criticality_score", "0.02"],
    ], MARGIN, PAGE_H - 2.5 * inch, [3.0 * inch, 2.0 * inch])
    _draw_bullets(c, [
        "sys_mod_count es la variable con mayor correlación negativa",
        "A más modificaciones, reasignaciones o tiempo de resolución,",
        "  menor probabilidad de cumplir el SLA",
        "Las variables temporales (hora, día, mes) tienen correlación débil",
    ], MARGIN, PAGE_H - 5.2 * inch, 14, BLANCO, CONTENT_W)
    _draw_footer(c)


def _slide_05_insights(c):
    _draw_bg(c)
    _draw_title(c, "Insights Clave del Análisis", PAGE_H - 1.0 * inch)
    y = PAGE_H - 1.8 * inch
    for titulo, texto in [
        ("1. Prioridad vs Cumplimiento de SLA",
         "Los tickets de prioridad crítica (1 - Critical) tienen la mayor tasa de"
         " incumplimiento relativa. La prioridad es un factor relevante aunque no"
         " determinante por sí solo."),
        ("2. Reasignaciones y Reaperturas",
         "El 14.8% de los tickets son problemáticos (>2 reasignaciones o alguna"
         " reapertura). Estos concentran la mayoría de los incumplimientos de SLA."),
        ("3. Tiempo de Resolución",
         "El tiempo promedio de resolución es de ~270 horas con alta variabilidad"
         " (desviación estándar de 651 h). Tickets con resolución prolongada tienen"
         " mayor probabilidad de incumplir el SLA."),
        ("4. Categorías de Incidentes",
         "Varias categorías tienen tasa de incumplimiento del 100%, lo que sugiere"
         " que ciertos tipos de incidentes requieren procesos especializados."),
    ]:
        _draw_text(c, titulo, MARGIN, y, 16, CELESTE, True)
        y = _draw_text(c, texto, MARGIN, y - 22, 13, BLANCO, max_width=CONTENT_W, leading=18)
        y -= 16
    _draw_footer(c)


def _slide_06_feature_eng(c):
    _draw_bg(c)
    _draw_title(c, "Feature Engineering", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Temporales: open_hour, open_dayofweek, open_month, open_year",
        "Codificación ordinal de prioridad, impacto y urgencia",
        "Criticality Score = promedio de priority, impact, urgency scores",
        "Resolution Time = diff(resolved_at - opened_at) en horas",
        "Problematic Ticket = reassignment > 2 OR reopen > 0",
    ], MARGIN, PAGE_H - 2.0 * inch, 13, BLANCO, 5.0 * inch)
    _draw_text(c, "Antes vs Después:", MARGIN + 5.5 * inch, PAGE_H - 2.0 * inch,
               16, CELESTE, True)
    _draw_table(c, [
        ["", "Original", "Transformado"],
        ["Variables", "36", "48"],
        ["Registros", "141,712", "141,712"],
    ], MARGIN + 5.5 * inch, PAGE_H - 2.6 * inch, [1.5 * inch, 1.2 * inch, 1.5 * inch])
    _draw_text(c, "Variables más importantes según modelo:",
               MARGIN + 5.5 * inch, PAGE_H - 4.0 * inch, 13, CELESTE, True)
    _draw_text(c, "sys_mod_count       53.5%",
               MARGIN + 5.5 * inch, PAGE_H - 4.4 * inch, 12, BLANCO)
    _draw_text(c, "resolution_time_h   23.4%",
               MARGIN + 5.5 * inch, PAGE_H - 4.7 * inch, 12, BLANCO)
    _draw_text(c, "reassignment_count   6.9%",
               MARGIN + 5.5 * inch, PAGE_H - 5.0 * inch, 12, BLANCO)
    _draw_text(c, "problematic_ticket   4.2%",
               MARGIN + 5.5 * inch, PAGE_H - 5.3 * inch, 12, BLANCO)
    _draw_text(c, "priority_score       3.8%",
               MARGIN + 5.5 * inch, PAGE_H - 5.6 * inch, 12, BLANCO)
    _draw_text(c, "Otras variables      8.2%",
               MARGIN + 5.5 * inch, PAGE_H - 5.9 * inch, 12, BLANCO)
    _draw_footer(c)


def _slide_07_modelos(c):
    _draw_bg(c)
    _draw_title(c, "Modelos Predictivos Evaluados", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Regresión Logística  -> modelo base, interpretable, 1000 iteraciones",
        "Random Forest        -> 200 árboles, class_weight='balanced'",
        "Gradient Boosting    -> 200 estimadores, max_depth=5",
        "Red Neuronal MLP     -> 3 capas (64-32-16), relu, adam, 500 epochs",
    ], MARGIN, PAGE_H - 2.0 * inch, 14, BLANCO, CONTENT_W)
    _draw_text(c, "Métricas de evaluación:",
               MARGIN, PAGE_H - 3.5 * inch, 16, CELESTE, True)
    csv_path = PROJECT_ROOT / "data" / "final" / "comparacion_modelos.csv"
    if csv_path.exists():
        df_comp = pd.read_csv(csv_path)
        cols = ["Modelo", "Accuracy", "Precision", "Recall", "F1-Score"]
        cols_existentes = [c for c in cols if c in df_comp.columns]
        filas = []
        for _, row in df_comp.iterrows():
            filas.append([str(row[c]) if not isinstance(row[c], (int, float)) else f"{row[c]:.4f}" for c in cols_existentes])
        tabla = [cols_existentes] + filas
    else:
        tabla = [["Modelo", "Accuracy", "Precision", "Recall", "F1-Score"]]
    _draw_table(c, tabla, MARGIN, PAGE_H - 4.2 * inch, [2.2 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch])
    _draw_footer(c)


def _slide_08_resultados(c):
    _draw_bg(c)
    _draw_title(c, "Resultados - Gradient Boosting (Modelo Seleccionado)",
                PAGE_H - 1.0 * inch, 24)
    _draw_text(c, "Métricas del modelo seleccionado:",
               MARGIN, PAGE_H - 1.8 * inch, 16, CELESTE, True)
    _draw_table(c, [
        ("Métrica", "Valor"),
        ("Accuracy", "93.46 %"),
        ("Precision", "93.69 %"),
        ("Recall", "99.72 %"),
        ("F1-Score", "0.9661"),
        ("ROC-AUC", "0.9056"),
    ], MARGIN, PAGE_H - 2.2 * inch,
               [1.8 * inch, 1.5 * inch])
    _draw_text(c, "Interpretación:", MARGIN + 4.0 * inch, PAGE_H - 1.8 * inch,
                16, CELESTE, True)
    _draw_bullets(c, [
        "Mejor F1-Score (0.9661) de todos los modelos",
        "ROC-AUC de 0.9056: excelente discriminación",
        "Recall del 99.72% en clase mayoritaria",
        "Alta precision (93.69%): baja tasa de falsos positivos",
    ], MARGIN + 4.0 * inch, PAGE_H - 2.5 * inch, 14, BLANCO, 4.5 * inch)
    _draw_text(c, "Variables más influyentes:",
               MARGIN, PAGE_H - 5.3 * inch, 16, CELESTE, True)
    _draw_text(c, "sys_mod_count (53.5%)  ->  resolution_time_hours (23.4%)  ->  reassignment_count (6.9%)",
               MARGIN, PAGE_H - 5.7 * inch, 13, BLANCO)
    _draw_footer(c)


def _slide_09_conclusiones(c):
    _draw_bg(c)
    _draw_title(c, "Conclusiones", PAGE_H - 1.0 * inch)
    y = PAGE_H - 1.8 * inch
    for titulo, cuerpo in TEXTOS_CONCLUSIONES:
        _draw_text(c, titulo, MARGIN, y, 14, CELESTE, True)
        y -= 18
        y = _draw_text(c, cuerpo, MARGIN, y, 10, BLANCO, max_width=CONTENT_W, leading=13)
        y -= 14
    _draw_footer(c)


def _slide_10_recomendaciones(c):
    _draw_bg(c)
    _draw_title(c, "Recomendaciones", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Implementar alertas tempranas para tickets con probabilidad >70% de",
        "incumplimiento, activando intervenciones preventivas automáticas",
        "Reducir reasignaciones mediante enrutamiento inteligente basado en",
        "categoría del ticket, especialidad del agente y carga de trabajo",
        "Optimizar el umbral de decisión del modelo (<0.5) para mejorar la",
        "detección de incumplimientos reales aceptando más falsos positivos",
        "Monitorear la deriva del modelo (concept drift) con reentrenamiento",
        "automático cuando las métricas caigan por debajo de umbrales definidos",
        "Integrar el score de riesgo en el sistema de ticketing (ServiceNow, Jira)",
        "para priorizar la cola de trabajo según riesgo predictivo",
        "Implementar explicaciones SHAP para cada predicción y aumentar la",
        "confianza de los agentes en las recomendaciones del modelo",
        "Evaluar el impacto económico (ROI) de la detección temprana considerando",
        "multas, costos operativos y satisfacción del cliente",
    ], MARGIN, PAGE_H - 2.0 * inch, 13, BLANCO, CONTENT_W)
    _draw_footer(c)


def _slide_11_gracias(c):
    _draw_bg(c)
    _draw_circuit_lines(c, MARGIN, PAGE_H - 2.0 * inch, 5, 25, CELESTE)
    _draw_circuit_lines(c, PAGE_W - MARGIN - 30, PAGE_H - 2.0 * inch, 5, 25, CELESTE)
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 0.5 * inch, "Gracias")
    c.setFillColor(CELESTE)
    c.setFont("Helvetica", 20)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 0.2 * inch,
                        "IT Operations Intelligence")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 0.8 * inch, "\u00bfPreguntas?")
    _draw_footer(c)


# ============================================================
# MAIN
# ============================================================

SLIDE_DRAWERS = [
    _slide_01_portada,
    _slide_02_problema,
    _slide_03_dataset,
    _slide_04_eda,
    _slide_05_insights,
    _slide_06_feature_eng,
    _slide_07_modelos,
    _slide_08_resultados,
    _slide_09_conclusiones,
    _slide_10_recomendaciones,
    _slide_11_gracias,
]


def generar_presentacion(output_path=None):
    """
    Crea y guarda el PDF del proyecto.
    """
    if output_path is None:
        output_path = str(PROJECT_ROOT / "Presentacion_IT_Operations_Intelligence.pdf")
    c = canvas.Canvas(output_path, pagesize=(PAGE_W, PAGE_H))
    for i, drawer in enumerate(SLIDE_DRAWERS, 1):
        drawer(c)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 8)
        c.drawRightString(PAGE_W - MARGIN, 0.15 * inch, f"{i} / {len(SLIDE_DRAWERS)}")
        c.showPage()
    c.save()
    return os.path.abspath(output_path)


if __name__ == "__main__":
    ruta = generar_presentacion()
    print(f"PDF generado: {ruta}")
