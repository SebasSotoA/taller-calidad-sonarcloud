import pytest
from src.app.utilidades_matematicas import funcion_grande, division_riesgosa

def test_funcion_grande():
    datos = [1, 2, 3]
    resultado = funcion_grande(datos)
    assert isinstance(resultado, (int, float))

def test_division_riesgosa():
    # --- Coverage: Esta función está probada pero puede fallar por Reliability
    resultado = division_riesgosa(10, 2)
    assert resultado == 5.0

# --- Coverage: Solo probamos algunas funciones, otras quedan sin cobertura
# Esto hará que SonarCloud reporte baja cobertura de pruebas
