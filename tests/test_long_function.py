import math
import pytest

from src.app import long_function as lf


def test_procesar_datos_complejos_basico():
    datos = [1, "2", 3.0, [4, "5"], "x", None]
    r = lf.procesar_datos_complejos(datos)
    assert r["datos_procesados"] == [1.0, 2.0, 3.0, 4.0, 5.0]
    assert r["suma_total"] == 15.0
    assert r["contador"] == 5
    assert r["promedio"] == 3.0
    assert r["maximo"] == 5.0
    assert r["minimo"] == 1.0


def test_validar_formulario_usuario_ok():
    ok, errores = lf.validar_formulario_usuario(
        nombre="Juan Perez",
        email="juan@example.com",
        edad=25,
        telefono="+57 300-1234567",
        direccion="Calle 123 #45-67",
        ciudad="Bogota",
        pais="Colombia",
        codigo_postal="110111",
    )
    assert ok is True
    assert errores == []


def test_validar_formulario_usuario_errores_minimos():
    ok, errores = lf.validar_formulario_usuario(
        nombre="J",
        email="mal",
        edad=15,
        telefono="abc",
        direccion="",
        ciudad="1",
        pais="2",
        codigo_postal="a-1",
    )
    assert ok is False
    # Verificamos que se recojan múltiples errores representativos
    assert any("nombre" in e for e in errores)
    assert any("email" in e for e in errores)
    assert any("mayor de edad" in e or "edad" in e for e in errores)


def test_funcion_con_muchos_parametros():
    res = lf.funcion_con_muchos_parametros(1, 2, "x", None, 3.5, -1, 0, 4, 5, 6, 7, 8, 9, 10, "11", 12, 13, 14, 15, 16)
    # Suma de solo numéricos
    assert math.isclose(res, 1 + 2 + 3.5 + -1 + 0 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 12 + 13 + 14 + 15 + 16, rel_tol=1e-9)


def test_strings_y_numeros_magicos():
    assert lf.funcion_con_strings_magicos("admin") == "success"
    assert lf.funcion_con_strings_magicos("nope") == "denied"
    assert lf.funcion_con_numeros_magicos() == 1400


def test_context_managers(tmp_path):
    # Crear 3 archivos y dejar otros faltantes para verificar tolerancia a errores
    files = []
    contenidos = ["hola", "mundo", "!\nlinea2"]
    for idx, text in enumerate(contenidos, start=1):
        p = tmp_path / f"archivo{idx}.txt"
        p.write_text(text, encoding="utf-8")
        files.append(str(p))
    # Agregar rutas inexistentes también
    files += [str(tmp_path / "archivoX.txt"), str(tmp_path / "archivoY.txt")]

    total = lf.funcion_con_muchos_context_managers(files)
    assert total == sum(len(t) for t in contenidos)
