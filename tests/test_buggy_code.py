import os
import builtins
import pytest

from src.app import buggy_code as bc


def test_dividir_numeros_ok():
    assert bc.dividir_numeros(10, 2) == 5.0


def test_dividir_numeros_zero_division():
    with pytest.raises(ValueError):
        bc.dividir_numeros(10, 0)


def test_usar_variable_no_definida():
    assert bc.usar_variable_no_definida() == 10


def test_manejo_excepciones_vacio():
    assert bc.manejo_excepciones_vacio() == 5.0


def test_usar_eval_peligroso_ok():
    assert bc.usar_eval_peligroso("2+2") == 4.0
    assert bc.usar_eval_peligroso("10/5") == 2.0


def test_usar_eval_peligroso_division_por_cero():
    with pytest.raises(ValueError):
        bc.usar_eval_peligroso("1/0")


def test_abrir_archivo_sin_cerrar_no_existe(tmp_path):
    # Cambiar cwd temporalmente al tmp_path para no tocar el repo
    filename = tmp_path / "archivo.txt"
    # No creamos el archivo: debe devolver cadena vacía
    from os import getcwd, chdir
    cwd = getcwd()
    try:
        chdir(tmp_path)
        assert bc.abrir_archivo_sin_cerrar(str(filename.name)) == ""
    finally:
        chdir(cwd)


def test_procesar_lista_nula_ok():
    assert bc.procesar_lista_nula([1, 2, 3]) == 3


def test_procesar_lista_nula_none():
    with pytest.raises(ValueError):
        bc.procesar_lista_nula(None)


def test_comparar_string_con_int():
    assert bc.comparar_string_con_int(42, "42") is True
    assert bc.comparar_string_con_int(42, "abc") is False


def test_acceso_indice_fuera_rango():
    assert bc.acceso_indice_fuera_rango(1) == 2
    assert bc.acceso_indice_fuera_rango(10) is None


def test_usar_atributo_inexistente():
    assert bc.usar_atributo_inexistente() == "valor"


def test_comparaciones_tipos_incompatibles():
    r1, r2, r3, r4, r5 = bc.comparaciones_tipos_incompatibles()
    assert r1 is True
    assert r2 is True
    assert r3 is True
    assert r4 is True
    assert r5 is True


def test_comparaciones_imposibles():
    r1, r2, r3, r4 = bc.comparaciones_imposibles()
    assert r1 == "mayor"
    assert r2 == "no_ejecuta"
    assert r3 is True
    assert r4 is True


def test_operaciones_imposibles():
    r1, r2, r3, r4 = bc.operaciones_imposibles()
    assert r1 == 5.0
    assert r2 == 1
    assert r3 == 3
    assert r4 is None


def test_uso_recursos_no_cerrados(tmp_path):
    # Ejecuta en un dir temporal para evitar basura en el repo
    from os import getcwd, chdir
    cwd = getcwd()
    try:
        chdir(tmp_path)
        content = bc.uso_recursos_no_cerrados()
        # Como archivo1.txt no existe, debe retornar ""
        assert content == ""
        # Y se habrán creado archivo2.txt y archivo3.txt
        assert os.path.exists("archivo2.txt")
        assert os.path.exists("archivo3.txt")
    finally:
        chdir(cwd)


def test_variables_no_inicializadas():
    r1, r2 = bc.variables_no_inicializadas()
    assert r1 == 52
    assert r2 == 0


def test_excepciones_no_manejadas():
    div, entero, idx = bc.excepciones_no_manejadas()
    assert div is None
    assert entero == 123
    assert idx is None


def test_comparaciones_strings_peligrosas():
    r1, r2, r3 = bc.comparaciones_strings_peligrosas()
    assert r1 == "string vacío"
    assert r2 == "valor es None"
    assert r3 == "iguales"


def test_operaciones_lista_peligrosas():
    r1, r2, r3, r4 = bc.operaciones_lista_peligrosas()
    assert r1 == 1
    assert r2 is None
    assert r3 is None
    assert r4 is None
