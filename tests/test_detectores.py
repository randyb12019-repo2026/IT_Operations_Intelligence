import pandas as pd
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.core.detectores import detectar_columna_prediccion, detectar_columna_modelo, detectar_columna_f1


def test_detectar_prediccion():
    df = pd.DataFrame({"Prediccion": [0, 1], "otra": [1, 2]})
    assert detectar_columna_prediccion(df) == "Prediccion"


def test_detectar_modelo():
    df = pd.DataFrame({"Modelo": ["A", "B"], "F1": [0.9, 0.8]})
    assert detectar_columna_modelo(df) == "Modelo"


def test_detectar_f1():
    df = pd.DataFrame({"F1-Score": [0.9, 0.8]})
    assert detectar_columna_f1(df) == "F1-Score"
