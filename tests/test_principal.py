import pytest
from src.app.utilidades_matematicas import funcion_grande

def test_funcion_grande():
    datos = [1, 2, 3]
    resultado = funcion_grande(datos)
    assert isinstance(resultado, (int, float))

# --- Coverage: NO probamos division_riesgosa() ni codigo_duplicado.py
# Esto hará que SonarCloud reporte baja cobertura de pruebas
