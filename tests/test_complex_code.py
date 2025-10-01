import math
import pytest

from src.app import complex_code as cc


def test_funcion_muy_larga_con_muchas_responsabilidades():
    reporte = cc.funcion_muy_larga_con_muchas_responsabilidades()
    assert set(reporte.keys()) == {
        "total_usuarios",
        "usuarios_activos",
        "edad_promedio",
        "edad_minima",
        "edad_maxima",
        "porcentaje_activos",
        "usuarios_validos",
    }
    assert reporte["total_usuarios"] == 100
    assert reporte["usuarios_validos"] == 100
    assert reporte["usuarios_activos"] == 50
    assert math.isclose(reporte["edad_promedio"], 44.5, rel_tol=1e-9, abs_tol=1e-9)
    assert reporte["edad_minima"] == 20
    assert reporte["edad_maxima"] == 69
    assert math.isclose(reporte["porcentaje_activos"], 50.0, rel_tol=1e-9, abs_tol=1e-9)


def test_funcion_con_muchos_parametros_y_logica_compleja():
    resultado = cc.funcion_con_muchos_parametros_y_logica_compleja(
        -1, 2, 3, 0, 5, -6, 7, -8, 9, 10, 0, 0, -4, 2, 1, -3, 8, -2, 0, 6, 4, -5, 3, 2, -1, 100
    )
    # Suma de positivos: 2+3+5+7+9+10+2+1+8+6+4+3+2+100 = 152
    assert resultado == 152


def test_funcion_con_muchos_parametros_excluye_diez_en_suma():
    # Cubre la lógica específica: excluir el 10 de la suma de positivos
    assert cc.funcion_con_muchos_parametros_y_logica_compleja(
        10, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ) == 0


def _expected_operaciones() -> float:
    base = sum(range(1, 31))
    resultado = base
    ops = (
        ("mul", 2),
        ("div", 3),
        ("add", 100),
        ("sub", 50),
        ("mul", 1.5),
        ("div", 2.5),
        ("add", 200),
        ("sub", 75),
        ("mul", 2.2),
        ("div", 1.8),
        ("add", 300),
        ("sub", 100),
        ("mul", 1.7),
        ("div", 2.3),
        ("add", 400),
        ("sub", 125),
        ("mul", 1.9),
        ("div", 2.1),
        ("add", 500),
        ("sub", 150),
    )
    for op_type, value in ops:
        if op_type == "mul":
            resultado *= value
        elif op_type == "div":
            resultado /= value
        elif op_type == "add":
            resultado += value
        elif op_type == "sub":
            resultado -= value
    return resultado


def test_funcion_con_muchas_variables_y_operaciones():
    esperado = _expected_operaciones()
    real = cc.funcion_con_muchas_variables_y_operaciones()
    assert math.isclose(real, esperado, rel_tol=1e-12, abs_tol=1e-12)


def test_funcion_con_muchos_comentarios_redundantes():
    assert cc.funcion_con_muchos_comentarios_redundantes() == -5


def test_funcion_con_muchos_imports_no_usados():
    assert cc.funcion_con_muchos_imports_no_usados() == 42


def test_funcion_con_muchos_strings_magicos_success():
    assert cc.funcion_con_muchos_strings_magicos() == "success"


def test_funcion_con_muchos_strings_magicos_error():
    assert cc.funcion_con_muchos_strings_magicos(["admin", "invalid"]) == "error"


def test_funcion_con_muchos_numeros_magicos():
    assert cc.funcion_con_muchos_numeros_magicos() == 1000
