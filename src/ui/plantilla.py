# Módulo con la configuración inicial de la página del dashboard Streamlit
import streamlit as st

def configurar_pagina():
    st.set_page_config(
        page_title="IT Operations Intelligence",
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
