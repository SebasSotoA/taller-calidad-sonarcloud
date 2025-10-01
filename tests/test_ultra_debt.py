from src.app.ultra_debt import (
    funcion_con_variables_locales_masivas,
    funcion_con_return_statements_masivos,
    funcion_con_complejidad_ciclamatica_masiva,
    funcion_con_bucles_anidados_masivos,
    funcion_con_try_except_masivos,
)

def test_funcion_con_variables_locales_masivas():
    # suma 1..200 = 200*201/2 = 20100
    assert funcion_con_variables_locales_masivas() == 20100

def test_funcion_con_return_statements_masivos():
    assert funcion_con_return_statements_masivos() == "caso 5"

def test_funcion_con_complejidad_ciclamatica_masiva():
    # sum i*(i+1) for i in 0..19 = 2660
    assert funcion_con_complejidad_ciclamatica_masiva() == 2660

def test_funcion_con_bucles_anidados_masivos():
    # nested_loops(15) = 2**15 - 1 = 32767
    assert funcion_con_bucles_anidados_masivos() == (1 << 15) - 1

def test_funcion_con_try_except_masivos():
    # sum 1..30 = 465
    assert funcion_con_try_except_masivos() == 465