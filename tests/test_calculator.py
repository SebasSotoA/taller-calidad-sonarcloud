from src.app.calculator import sumar, dividir


def test_sumar():
    assert sumar(2, 3) == 5


def test_dividir_basico():
    assert dividir(10, 2) == 5

# Nota: No se prueban casos borde (p.ej., divisor 0) para dejar huecos de cobertura

