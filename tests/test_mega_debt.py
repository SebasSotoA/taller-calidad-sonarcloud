import pytest
import src.app.mega_debt as mega

def test_funcion_mega_larga_con_responsabilidades_masivas_monkeypatched(monkeypatch):
    # Acelera: baja a 200 usuarios para el test
    monkeypatch.setattr(mega, "TOTAL_USUARIOS_DEFAULT", 200)

    rep = mega.funcion_mega_larga_con_responsabilidades_masivas()
    for key in [
        "resumen",
        "estadisticas_edad",
        "estadisticas_puntos",
        "distribucion_niveles",
        "distribucion_idiomas",
        "distribucion_paises",
        "preferencias",
        "estadisticas_uso",
        "porcentajes",
    ]:
        assert key in rep

    resumen = rep["resumen"]
    assert resumen["total_usuarios"] == 200
    assert resumen["usuarios_validos"] + resumen["usuarios_invalidos"] == 200
    for v in rep["porcentajes"].values():
        assert 0.0 <= v <= 100.0

def test_funcion_con_parametros_masivos_suma_positivos():
    # 104 args: mezcla de tipos / signos
    base = [1, -1, 2.5, "x", 0] * 21  # 105 elementos
    args = base[:104]
    res = mega.funcion_con_parametros_masivos(*args)
    expected = float(sum(x for x in args if isinstance(x, (int, float)) and x > 0))
    assert res == expected