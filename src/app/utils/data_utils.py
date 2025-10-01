"""
Utilidades de datos compartidas para cumplir DRY entre módulos de la app.
"""
from __future__ import annotations

from typing import Any, Iterable, List, Tuple, Dict, Optional
import os


def _is_number(x: Any) -> bool:
    # Considera int/float, pero excluye bool (subclase de int)
    return (isinstance(x, (int, float)) and not isinstance(x, bool))


def calcular_estadisticas_numericas(lista_numeros: Iterable[Any]) -> Optional[Dict[str, float]]:
    """
    Filtra valores numéricos y calcula estadísticas básicas.
    Retorna None si no hay valores numéricos.
    """
    nums = [float(x) for x in lista_numeros if _is_number(x)]
    if not nums:
        return None
    suma = float(sum(nums))
    contador = float(len(nums))
    promedio = suma / contador
    maximo = float(max(nums))
    minimo = float(min(nums))
    return {
        "suma": suma,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "contador": contador,
    }


def procesar_archivo_csv(nombre_archivo: str) -> List[float]:
    """
    Lee un archivo CSV sencillo y devuelve todos los números convertidos a float.
    Ignora valores no numéricos. Si el archivo no existe, retorna [].
    """
    if not os.path.exists(nombre_archivo):
        return []
    numeros: List[float] = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for line in f:
                for token in line.strip().split(","):
                    token = token.strip()
                    if not token:
                        continue
                    try:
                        numeros.append(float(token))
                    except ValueError:
                        # Ignorar tokens no numéricos
                        pass
    except OSError:
        # Ante cualquier problema de lectura, retornar lo acumulado hasta ahora
        return numeros
    return numeros


def validar_datos_entrada(datos: Any) -> Tuple[bool, List[str]]:
    """
    Valida que `datos` sea una lista no vacía de números (int/float, no bool).
    Devuelve (ok, errores).
    """
    errores: List[str] = []
    if datos is None:
        errores.append("El valor de entrada es None")
        return False, errores
    if not isinstance(datos, list):
        errores.append("La entrada debe ser una lista")
        return False, errores
    if len(datos) == 0:
        errores.append("La lista está vacía")
        return False, errores
    no_numericos = [x for x in datos if not _is_number(x)]
    if no_numericos:
        errores.append("Algún elemento no es un número")
        return False, errores
    return True, []


def convertir_temperaturas(temperaturas_celsius: Iterable[Any]) -> List[float]:
    """
    Convierte C->F para valores numéricos. Ignora entradas no numéricas.
    Fórmula: F = C * 9/5 + 32
    """
    out: List[float] = []
    for c in temperaturas_celsius:
        if _is_number(c):
            out.append(float(c) * 9.0 / 5.0 + 32.0)
    return out


def buscar_elemento_en_lista(lista: Iterable[Any], elemento: Any) -> int:
    """
    Devuelve el índice del elemento en la lista o -1 si no se encuentra.
    """
    # Convertir a lista para soportar cualquier Iterable
    seq = list(lista)
    try:
        return seq.index(elemento)
    except ValueError:
        return -1
