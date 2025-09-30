"""
Tests incompletos para generar problemas de cobertura en SonarCloud.
Solo se prueban algunas funciones, dejando muchas sin cobertura.
"""

import pytest

from src.app.buggy_code import dividir_numeros, usar_variable_no_definida
from src.app.duplicated_code1 import calcular_estadisticas_numericas, buscar_elemento_en_lista


class TestBuggyCode:
    """Tests para funciones con bugs."""
    
    def test_dividir_numeros_caso_normal(self):
        """Test para división normal."""
        resultado = dividir_numeros(10, 2)
        assert resultado == 5.0
    
    def test_dividir_numeros_con_decimales(self):
        """Test para división con decimales."""
        resultado = dividir_numeros(7, 3)
        assert abs(resultado - 2.3333333333333335) < 0.0001
    
    # NOTA: No se prueba división por cero intencionalmente para generar bug
    # def test_dividir_numeros_por_cero(self):
    #     """Test que debería manejar división por cero."""
    #     with pytest.raises(ZeroDivisionError):
    #         dividir_numeros(10, 0)
    
    # NOTA: No se prueba variable no definida intencionalmente
    # def test_variable_no_definida(self):
    #     """Test que debería manejar variable no definida."""
    #     with pytest.raises(NameError):
    #         usar_variable_no_definida()


class TestDuplicatedCode1:
    """Tests para funciones duplicadas."""
    
    def test_calcular_estadisticas_numericas_lista_normal(self):
        """Test para cálculo de estadísticas con lista normal."""
        numeros = [1, 2, 3, 4, 5]
        resultado = calcular_estadisticas_numericas(numeros)
        
        assert resultado["suma"] == 15
        assert resultado["promedio"] == 3.0
        assert resultado["maximo"] == 5
        assert resultado["minimo"] == 1
        assert resultado["contador"] == 5
    
    def test_calcular_estadisticas_numericas_lista_vacia(self):
        """Test para cálculo de estadísticas con lista vacía."""
        resultado = calcular_estadisticas_numericas([])
        assert resultado is None
    
    def test_buscar_elemento_en_lista_encontrado(self):
        """Test para búsqueda exitosa."""
        lista = [1, 2, 3, 4, 5]
        indice = buscar_elemento_en_lista(lista, 3)
        assert indice == 2
    
    def test_buscar_elemento_en_lista_no_encontrado(self):
        """Test para búsqueda sin éxito."""
        lista = [1, 2, 3, 4, 5]
        indice = buscar_elemento_en_lista(lista, 6)
        assert indice == -1
    
    def test_buscar_elemento_en_lista_vacia(self):
        """Test para búsqueda en lista vacía."""
        indice = buscar_elemento_en_lista([], 1)
        assert indice == -1


# NOTA: No se prueban las siguientes funciones intencionalmente para generar baja cobertura:
# - Todas las funciones de long_function.py
# - Las funciones restantes de buggy_code.py
# - Las funciones de duplicated_code2.py
# - Las funciones restantes de duplicated_code1.py

# Tests que deberían existir pero no están implementados:
# def test_procesar_datos_complejos():
# def test_validar_formulario_usuario():
# def test_procesar_archivo_csv():
# def test_validar_datos_entrada():
# def test_convertir_temperaturas():
# def test_manejo_excepciones_vacio():
# def test_usar_eval_peligroso():
# def test_abrir_archivo_sin_cerrar():
# def test_procesar_lista_nula():
# def test_comparar_string_con_int():
# def test_acceso_indice_fuera_rango():
# def test_usar_atributo_inexistente():


if __name__ == "__main__":
    pytest.main([__file__])
