import os
from typing import Any

import pytest

from src.app import duplicated_code1 as dc1


@pytest.mark.parametrize("mod", [dc1])
class TestDuplicatedModules:
    def test_calcular_estadisticas_numericas_ok(self, mod):
        datos = [1, 2, 3, 4.0, "x", None]
        stats = mod.calcular_estadisticas_numericas(datos)
        assert stats is not None
        assert stats["suma"] == pytest.approx(10.0)
        assert stats["promedio"] == pytest.approx(10.0 / 4.0)
        assert stats["maximo"] == 4.0
        assert stats["minimo"] == 1.0
        assert stats["contador"] == 4.0

    def test_calcular_estadisticas_numericas_vacia(self, mod):
        assert mod.calcular_estadisticas_numericas([]) is None
        assert mod.calcular_estadisticas_numericas(["a", None]) is None

    def test_procesar_archivo_csv_ok(self, mod, tmp_path):
        p = tmp_path / "valores.csv"
        p.write_text("1,2,3\n4,5,abc\n7.5\n", encoding="utf-8")
        numeros = mod.procesar_archivo_csv(str(p))
        assert numeros == [1.0, 2.0, 3.0, 4.0, 5.0, 7.5]

    def test_procesar_archivo_csv_no_existe(self, mod, tmp_path):
        p = tmp_path / "no_existe.csv"
        assert mod.procesar_archivo_csv(str(p)) == []

    def test_validar_datos_entrada(self, mod):
        ok, errores = mod.validar_datos_entrada([1, 2.0, 3])
        assert ok is True and errores == []

        ok, errores = mod.validar_datos_entrada(None)
        assert ok is False and "None" in errores[0]

        ok, errores = mod.validar_datos_entrada("no lista")
        assert ok is False and "lista" in errores[0].lower()

        ok, errores = mod.validar_datos_entrada([])
        assert ok is False and "vacía" in errores[0]

        ok, errores = mod.validar_datos_entrada([1, "x", 3])
        assert ok is False and any("no es un número" in e for e in errores)

    def test_convertir_temperaturas(self, mod):
        out = mod.convertir_temperaturas([0, 100, -40, "x"])
        # 0C->32F, 100C->212F, -40C->-40F
        assert out == [32.0, 212.0, -40.0]

    def test_buscar_elemento_en_lista(self, mod):
        lista = ["a", "b", "c"]
        assert mod.buscar_elemento_en_lista(lista, "b") == 1
        assert mod.buscar_elemento_en_lista(lista, "z") == -1
        assert mod.buscar_elemento_en_lista([], "a") == -1
