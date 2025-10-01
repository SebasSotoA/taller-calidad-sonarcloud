import pytest

from src.app.massive_debt import (
    funcion_con_complejidad_ciclamatica_extrema,
    funcion_con_muchos_bucles_anidados_extremos,
    funcion_con_muchos_try_except_anidados_extremos,
    funcion_con_muchos_operadores_logicos_extremos,
    funcion_con_muchos_strings_magicos_extremos,
    funcion_con_muchos_numeros_magicos_extremos,
)

def test_funcion_con_complejidad_ciclamatica_extrema_tipo_y_rango():
    res = funcion_con_complejidad_ciclamatica_extrema()
    assert isinstance(res, (int, float))
    assert res >= 0

def test_funcion_con_muchos_bucles_anidados_extremos_valor():
    res = funcion_con_muchos_bucles_anidados_extremos()
    assert isinstance(res, int)
    assert res >= 0

def test_funcion_con_muchos_try_except_anidados_extremos_determinista():
    r1 = funcion_con_muchos_try_except_anidados_extremos()
    r2 = funcion_con_muchos_try_except_anidados_extremos()
    assert isinstance(r1, (int, float))
    assert r1 == r2  # determinista

def test_funcion_con_muchos_operadores_logicos_extremos():
    assert isinstance(funcion_con_muchos_operadores_logicos_extremos(), bool)

def test_funcion_con_muchos_strings_magicos_extremos():
    s = funcion_con_muchos_strings_magicos_extremos()
    assert isinstance(s, str)
    assert len(s) > 0

def test_funcion_con_muchos_numeros_magicos_extremos():
    v = funcion_con_muchos_numeros_magicos_extremos()
    assert isinstance(v, (int, float))