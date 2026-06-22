# Módulo que genera la cabecera del dashboard con el título, descripción y reloj del sistema
import streamlit as st
from datetime import datetime

def cabecera():
    st.markdown("""
    <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem;">
        <div style="font-size:2.5rem;">🖥️</div>
        <div>
            <h1 style="margin:0; font-size:1.8rem;">IT Operations Intelligence</h1>
            <p style="margin:0; color:#6b7280; font-size:0.85rem;">
                Sistema de Análisis de Incidencias y Tickets de Soporte Tecnológico
            </p>
        </div>
        <div style="margin-left:auto; text-align:right;">
            <div style="font-family:'Share Tech Mono',monospace; color:#00ff88; font-size:0.8rem;">
                MONITOR: ACTIVE
            </div>
            <div style="font-family:'Share Tech Mono',monospace; color:#6b7280; font-size:0.7rem;">
                """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
