import os
import pytest

from src.app import buggy_code as bc


def test_usar_eval_peligroso_none_raises():
    with pytest.raises(ValueError):
        bc.usar_eval_peligroso(None)  # type: ignore[arg-type]


def test_usar_eval_peligroso_pow_mod_unary():
    assert bc.usar_eval_peligroso("2**3") == 8.0
    assert bc.usar_eval_peligroso("-5") == -5.0
    assert bc.usar_eval_peligroso("10%3") == 1.0


def test_abrir_archivo_sin_cerrar_exists(tmp_path):
    p = tmp_path / "archivo.txt"
    p.write_text("contenido", encoding="utf-8")
    # Cambiar cwd temporalmente al tmp_path para no tocar el repo
    from os import getcwd, chdir
    cwd = getcwd()
    try:
        chdir(tmp_path)
        assert bc.abrir_archivo_sin_cerrar("archivo.txt") == "contenido"
    finally:
        chdir(cwd)


def test_acceso_indice_fuera_rango_bordes():
    assert bc.acceso_indice_fuera_rango(0) == 1
    assert bc.acceso_indice_fuera_rango(2) == 3
    assert bc.acceso_indice_fuera_rango(-1) is None
    assert bc.acceso_indice_fuera_rango(3) is None
