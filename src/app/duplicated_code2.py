"""
Archivo con código duplicado para probar detección de duplicación en SonarCloud.
Este archivo contiene funciones idénticas a duplicated_code1.py
"""

from typing import Any, Iterable, List, Tuple, Dict, Optional

from src.app.utils.data_utils import (
    calcular_estadisticas_numericas as _calc_stats,
    procesar_archivo_csv as _proc_csv,
    validar_datos_entrada as _validar,
    convertir_temperaturas as _conv_temp,
    buscar_elemento_en_lista as _buscar,
)


def calcular_estadisticas_numericas(lista_numeros: Iterable[Any]) -> Optional[Dict[str, float]]:
    """Calcula estadísticas delegando en utilidades compartidas (SRP/DRY)."""
    return _calc_stats(lista_numeros)


def procesar_archivo_csv(nombre_archivo: str) -> List[float]:
    """Procesa un CSV delegando en utilidades; sin prints, retorna lista de floats."""
    return _proc_csv(nombre_archivo)


def validar_datos_entrada(datos: Any) -> Tuple[bool, List[str]]:
    """Valida datos delegando en utilidades compartidas."""
    return _validar(datos)


def convertir_temperaturas(temperaturas_celsius: Iterable[Any]) -> List[float]:
    """Convierte temperaturas delegando en utilidades compartidas."""
    return _conv_temp(temperaturas_celsius)


def buscar_elemento_en_lista(lista: Iterable[Any], elemento: Any) -> int:
    """Busca un elemento delegando en utilidades compartidas."""
    return _buscar(lista, elemento)
