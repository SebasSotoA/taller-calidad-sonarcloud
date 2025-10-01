from src.app.extreme_debt import (
    funcion_extremadamente_larga_con_muchas_responsabilidades,
    funcion_con_muchos_parametros_extremos,
    funcion_con_muchas_variables_locales_extremas,
    funcion_con_muchos_return_statements_extremos,
)

def test_funcion_extremadamente_larga_con_muchas_responsabilidades_shape():
    rep = funcion_extremadamente_larga_con_muchas_responsabilidades()
    for key in [
        "resumen",
        "estadisticas_edad",
        "estadisticas_puntos",
        "distribucion_niveles",
        "distribucion_idiomas",
        "distribucion_paises",
        "preferencias",
        "porcentajes",
    ]:
        assert key in rep

    resumen = rep["resumen"]
    assert resumen["total_usuarios"] == 1000
    assert resumen["usuarios_validos"] + resumen["usuarios_invalidos"] == 1000
    for v in rep["porcentajes"].values():
        assert 0.0 <= v <= 100.0

def test_funcion_con_muchos_parametros_extremos_suma_positivos():
    # 52 argumentos con mezcla de tipos
    args = [1, -2, 3.5, 0, "no-num", 2, -1, 4, 5, -6]  # 10
    args += [1] * 42  # hasta 52
    res = funcion_con_muchos_parametros_extremos(*args)
    expected = float(sum(x for x in args if isinstance(x, (int, float)) and x > 0))
    assert res == expected

def test_funcion_con_muchas_variables_locales_extremas():
    # suma 1..100 = 5050
    assert funcion_con_muchas_variables_locales_extremas() == 5050

def test_funcion_con_muchos_return_statements_extremos():
    assert funcion_con_muchos_return_statements_extremos() == "caso 5"