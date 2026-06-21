import pandas as pd
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.core.metricas import obtener_media, obtener_metricas


def test_obtener_media_con_columna_existente():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    resultado, col = obtener_media(df, ["a", "b"])
    assert resultado == 2.0


def test_obtener_media_sin_columna():
    df = pd.DataFrame({"x": [1, 2, 3]})
    resultado, col = obtener_media(df, ["no_existe"])
    assert resultado == "N/D"
    assert col is None


def test_obtener_metricas_con_columnas_preferidas():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": ["x", "y"]})
    resultado = obtener_metricas(df, ["a", "b", "d"])
    assert resultado == ["a", "b"]
