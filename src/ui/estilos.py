# Módulo que define los estilos CSS personalizados con temática oscura tipo terminal de monitoreo
import streamlit as st

def estilos():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Inter:wght@300;400;600;700&display=swap');

    * { font-family: 'Inter', sans-serif; }

    .stApp {
        background: #0a0e17;
        background-image:
            radial-gradient(ellipse at 10% 20%, rgba(0, 150, 255, 0.05) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 80%, rgba(0, 200, 100, 0.03) 0%, transparent 50%);
    }

    h1, h2, h3 {
        font-family: 'Share Tech Mono', monospace !important;
        color: #00d4ff !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }

    h1 { border-bottom: 1px solid #00d4ff33; padding-bottom: 0.5rem; }

    .stMetric {
        background: linear-gradient(135deg, #0d1520 0%, #141e2b 100%);
        border: 1px solid #1a3a5c;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.05);
    }
    .stMetric label {
        font-family: 'Share Tech Mono', monospace !important;
        color: #00d4ff !important;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #00ff88 !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 2rem !important;
    }

    .info-card {
        background: linear-gradient(135deg, #0d1520 0%, #141e2b 100%);
        border: 1px solid #1a3a5c;
        border-left: 3px solid #00d4ff;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 0.8rem 0;
    }
    .info-card h3 {
        margin-top: 0;
        color: #00d4ff;
        font-family: 'Share Tech Mono', monospace;
        font-size: 1rem;
    }
    .info-card p {
        color: #c8d6e5;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .stButton button {
        background: linear-gradient(135deg, #00d4ff 0%, #0088cc 100%);
        color: #0a0e17;
        font-weight: 600;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-family: 'Share Tech Mono', monospace;
        transition: all 0.3s;
    }
    .stButton button:hover {
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
        transform: translateY(-1px);
    }

    .stSelectbox, .stMultiselect {
        background-color: #0d1520;
        border-color: #1a3a5c;
        color: #c8d6e5;
    }

    .stDataFrame {
        border: 1px solid #1a3a5c !important;
        border-radius: 8px;
    }

    .status-indicator {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 6px;
    }
    .status-ok { background: #00ff88; box-shadow: 0 0 8px #00ff88; }
    .status-warning { background: #ffaa00; box-shadow: 0 0 8px #ffaa00; }
    .status-critical { background: #ff3355; box-shadow: 0 0 8px #ff3355; }

    footer { display: none; }
    </style>
    """, unsafe_allow_html=True)
