"""
Helpers reutilizables para refactorización y reducción de duplicación en módulos de deuda técnica.
Proveen operaciones seguras (safe_div, validate_index), normalización y utilidades
para despachar estrategias y simular bucles anidados sin complejidad artificial.
"""

from __future__ import annotations

from typing import Callable, Iterable, Sequence, TypeVar, Optional, Dict, Mapping, Iterator

T = TypeVar("T")


# =========================
# Excepciones de dominio (mejor semántica que ValueError genérico)
# =========================
class ValidationError(ValueError):
    """Errores de validación de datos."""


# =========================
# Utilidades básicas y de despacho
# =========================
def safe_div(a: float, b: float) -> float:
    """
    Divide a entre b validando que b no sea cero.
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
    Despacha la llamada a una función según key usando un diccionario (sin args).
    """
    fn = table.get(key)
    if fn is not None:
        return fn()
    if default is not None:
        return default()
    raise KeyError(f"Clave '{key}' no encontrada en tabla de despacho.")


def dispatch_with_args(
    key: str,
    table: Mapping[str, Callable[..., T]],
    *args,
    default: Optional[Callable[..., T]] = None,
    **kwargs,
) -> T:
    """
    Variante de despacho que admite *args/**kwargs (OCP: fácil de extender).
    """
    fn = table.get(key)
    if fn is not None:
        return fn(*args, **kwargs)
    if default is not None:
        return default(*args, **kwargs)
    raise KeyError(f"Clave '{key}' no encontrada en tabla de despacho.")


def ensure(predicate: bool, message: str, exc: type[Exception] = ValidationError) -> None:
    """
    'Guard clause': si predicate es False, lanza la excepción indicada.
    Útil para evitar anidamientos y documentar precondiciones.
    """
    if not predicate:
        raise exc(message)


# =========================
# Números y colecciones
# =========================
def nested_loops(depth: int) -> int:
    """
    Simula el trabajo de bucles anidados de profundidad dada de forma O(1).
    Devuelve 2**depth - 1 para depth >= 1.
    """
    if depth < 1:
        raise ValueError("La profundidad debe ser al menos 1.")
    return (1 << depth) - 1  # 2**depth - 1


def normalize_numbers(valores: Iterable[float]) -> list[float]:
    """
    Normaliza una lista de números a rango [0, 1].
    """
    valores = list(valores)
    if not valores:
        raise ValidationError("La lista de valores está vacía.")
    min_v, max_v = min(valores), max(valores)
    if min_v == max_v:
        raise ValidationError("Todos los valores son iguales; no se puede normalizar.")
    span = max_v - min_v
    return [(v - min_v) / span for v in valores]


def aggregate_stats(valores: Iterable[float]) -> dict[str, float]:
    """
    Calcula min, max, mean, var sobre una lista de números.
    """
    xs = list(valores)
    if not xs:
        raise ValidationError("La lista de valores está vacía.")
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return {"min": min(xs), "max": max(xs), "mean": mean, "var": var}


def percentage(part: float, whole: float, *, decimals: int = 2, zero_when_empty: bool = True) -> float:
    """
    Calcula porcentaje de forma segura (evita división por cero).
    """
    if whole == 0:
        if zero_when_empty:
            return 0.0
        raise ValidationError("No se puede calcular porcentaje con total = 0.")
    return round((part / whole) * 100.0, decimals)


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Restringe un valor al rango [min_value, max_value].
    """
    if min_value > max_value:
        raise ValidationError("min_value no puede ser mayor que max_value.")
    return max(min_value, min(max_value, value))


def chunked(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """
    Divide un iterable en bloques de longitud 'size'. Útil para procesar lotes.
    """
    if size < 1:
        raise ValidationError("El tamaño de chunk debe ser >= 1.")
    buff: list[T] = []
    for item in iterable:
        buff.append(item)
        if len(buff) == size:
            yield buff
            buff = []
    if buff:
        yield buff


# =========================
# Validación genérica de texto / secuencias
# =========================
def validate_index(seq: Sequence[T], idx: int) -> T:
    """
    Acceso seguro a un índice de una secuencia.
    """
    if idx < 0 or idx >= len(seq):
        raise IndexError(f"Índice {idx} fuera de rango para secuencia de tamaño {len(seq)}.")
    return seq[idx]


def is_alpha_space(s: str) -> bool:
    """
    True si la cadena contiene solo letras y espacios (útil para nombres).
    """
    return s.replace(" ", "").isalpha()


def validate_length(s: str, *, min_len: int, max_len: int) -> None:
    """
    Valida longitud mínima y máxima de una cadena.
    """
    ensure(min_len >= 0, "min_len debe ser >= 0")
    ensure(max_len >= min_len, "max_len debe ser >= min_len")
    n = len(s)
    if n < min_len or n > max_len:
        raise ValidationError(f"Longitud inválida: {n} (esperado entre {min_len} y {max_len}).")
