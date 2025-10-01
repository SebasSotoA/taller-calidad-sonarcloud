import math
import pytest

from src.app import long_function as lf


def test_funcion_con_complejidad_ciclamatica():
    val = lf.funcion_con_complejidad_ciclamatica()
    assert isinstance(val, int)
    assert val > 0


def test_funcion_con_muchas_variables_locales():
    assert lf.funcion_con_muchas_variables_locales() == 210


def test_funcion_con_muchos_return():
    assert lf.funcion_con_muchos_return() == 5


def test_funcion_con_imports_no_usados():
    assert lf.funcion_con_imports_no_usados() == 10


def test_funcion_con_muchos_if_anidados():
    val = lf.funcion_con_muchos_if_anidados()
    assert isinstance(val, int)
    assert val > 0


def test_funcion_con_muchos_elif():
    assert lf.funcion_con_muchos_elif(5) == "cinco"
    assert lf.funcion_con_muchos_elif(21) == "desconocido"


def test_funcion_con_muchos_bucles_anidados():
    assert lf.funcion_con_muchos_bucles_anidados() == 6250000


def test_funcion_con_muchas_condiciones_complejas():
    assert lf.funcion_con_muchas_condiciones_complejas() == 24


def test_funcion_con_muchos_try_except():
    assert lf.funcion_con_muchos_try_except() == 55


def test_funcion_con_muchos_while():
    assert lf.funcion_con_muchos_while() == 31250


def test_funcion_con_muchos_operadores_logicos():
    assert lf.funcion_con_muchos_operadores_logicos() == 14


def test_funcion_con_muchos_casos_switch():
    assert lf.funcion_con_muchos_casos_switch(5) == "caso 5"
    assert lf.funcion_con_muchos_casos_switch(31) == "caso por defecto"


def test_funcion_con_muchos_operadores_ternarios():
    nivel, letra = lf.funcion_con_muchos_operadores_ternarios(5)
    assert nivel == "bajo" and letra == "E"
    nivel0, letra0 = lf.funcion_con_muchos_operadores_ternarios(0)
    assert nivel0 == "cero" and letra0 == "desconocido"
    nivel_alto, letra_k = lf.funcion_con_muchos_operadores_ternarios(11)
    assert nivel_alto == "alto" and letra_k == "K"


def test_funcion_con_muchos_lambdas():
    val = lf.funcion_con_muchos_lambdas()
    assert isinstance(val, int)
    assert val > 0


def test_funcion_con_muchos_generadores():
    assert lf.funcion_con_muchos_generadores() == 31250


def test_funcion_con_muchos_decoradores():
    assert lf.funcion_con_muchos_decoradores() == 25


def test_funcion_con_duplicacion_interna():
    assert lf.funcion_con_duplicacion_interna() == 180
