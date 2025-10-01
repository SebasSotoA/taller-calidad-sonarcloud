"""
Helpers reutilizables para refactorización y reducción de duplicación en módulos de deuda técnica.
Proveen operaciones seguras (safe_div, validate_index), normalización y utilidades
para despachar estrategias y simular bucles anidados sin complejidad artificial.
"""

from __future__ import annotations

from typing import Callable, Iterable, Sequence, TypeVar, Optional, Dict, Mapping

T = TypeVar("T")


def safe_div(a: float, b: float) -> float:
    """
    Divide a entre b validando que b no sea cero.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        Resultado de la división.

    Raises:
        ValueError: Si b es cero.
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b


def dispatch_by_key(
    key: str,
    table: Mapping[str, Callable[[], T]],
    default: Optional[Callable[[], T]] = None,
) -> T:
    """
    Despacha la llamada a una función según el valor de key usando un diccionario.

    Args:
        key: Clave a despachar.
        table: Mapeo de funciones sin argumentos.
        default: Función por defecto si la clave no existe.

    Returns:
        Resultado de la función despachada.

    Raises:
        KeyError: Si la clave no existe y no se provee default.
    """
    fn = table.get(key)
    if fn is not None:
        return fn()
    if default is not None:
        return default()
    raise KeyError(f"Clave '{key}' no encontrada en tabla de despacho.")


def nested_loops(depth: int) -> int:
    """
    Simula el trabajo de bucles anidados de profundidad dada de forma O(1),
    evitando recursión o anidamientos reales.

    Semántica: produce el mismo resultado que la versión recursiva anterior,
    i.e., (2**depth) - 1 para depth >= 1.

    Args:
        depth: Profundidad de los bucles (>= 1).

    Returns:
        Suma acumulada simulada: 2**depth - 1.

    Raises:
        ValueError: Si depth < 1.
    """
    if depth < 1:
        raise ValueError("La profundidad debe ser al menos 1.")
    return (1 << depth) - 1  # equivalente a 2**depth - 1


def normalize_numbers(valores: Iterable[float]) -> list[float]:
    """
    Normaliza una lista de números a rango [0, 1].

    Args:
        valores: Números a normalizar.

    Returns:
        Lista normalizada.

    Raises:
        ValueError: Si la lista está vacía o todos los valores son iguales.
    """
    valores = list(valores)
    if not valores:
        raise ValueError("La lista de valores está vacía.")
    min_v, max_v = min(valores), max(valores)
    if min_v == max_v:
        raise ValueError("Todos los valores son iguales; no se puede normalizar.")
    span = max_v - min_v
    return [(v - min_v) / span for v in valores]


def aggregate_stats(valores: Iterable[float]) -> dict[str, float]:
    """
    Calcula estadísticas básicas (min, max, mean, var) de una lista de números.

    Args:
        valores: Números a analizar.

    Returns:
        Diccionario con 'min', 'max', 'mean', 'var'.

    Raises:
        ValueError: Si la lista está vacía.
    """
    xs = list(valores)
    if not xs:
        raise ValueError("La lista de valores está vacía.")
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return {
        "min": min(xs),
        "max": max(xs),
        "mean": mean,
        "var": var,
    }


def validate_index(seq: Sequence[T], idx: int) -> T:
    """
    Acceso seguro a un índice de una secuencia.

    Args:
        seq: Secuencia a indexar.
        idx: Índice solicitado.

    Returns:
        Elemento en la posición idx.

    Raises:
        IndexError: Si el índice está fuera de rango.
    """
    if idx < 0 or idx >= len(seq):
        raise IndexError(f"Índice {idx} fuera de rango para secuencia de tamaño {len(seq)}.")
    return seq[idx]