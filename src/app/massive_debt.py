"""
massive_debt.py
---------------
Versión refactorizada para mejorar mantenibilidad, confiabilidad y reducir complejidad.
Aplica principios SOLID, elimina números/strings mágicos y reutiliza helpers comunes.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List

from .utils import (  # type: ignore
    aggregate_stats,
    dispatch_by_key,
    nested_loops,
    normalize_numbers,
    safe_div,
    validate_index,
)

# =========================
# Constantes (evitar “magic numbers/strings”)
# =========================
DEFAULT_DEPTH: int = 12
DEFAULT_TRIES: int = 8
DEFAULT_KEY: str = "alpha"

NUM_SAMPLE: List[float] = [3.0, 6.0, 9.0, 12.0, 15.0]
ALTERNATE_NUM_SAMPLE: List[float] = [10.0, 5.0, 0.0, -5.0, 20.0]

LABELS: Dict[str, str] = {
    "alpha": "ALPHA",
    "beta": "BETA",
    "gamma": "GAMMA",
}

TAX_RATE: float = 0.19
DISCOUNT_RATE: float = 0.07
SURCHARGE_RATE: float = 0.03
SPLIT_DIVISOR: float = 2.0


# =========================
# Funciones públicas (API)
# =========================
def funcion_con_complejidad_ciclamatica_extrema() -> float:
    """
    Calcula un valor compuesto sobre un arreglo normalizado aplicando un
    despacho por clave. Reemplaza cascadas de if/elif por una tabla (OCP).

    Returns:
        float: resultado del cálculo compuesto.

    Raises:
        ValueError: si la clave de estrategia no existe o si ocurre división
                    por cero en la operación configurada.
    """
    values = normalize_numbers(NUM_SAMPLE)
    stats = aggregate_stats(values)

    strategies: Dict[str, Callable[[], float]] = {
        "alpha": lambda: _alpha_score(stats["mean"], stats["max"]),
        "beta": lambda: _beta_score(stats["mean"], stats["min"], TAX_RATE),
        "gamma": lambda: _gamma_score(values),
    }

    # OCP: agregar una estrategia solo requiere extender "strategies".
    return dispatch_by_key(DEFAULT_KEY, strategies)


def funcion_con_muchos_bucles_anidados_extremos() -> int:
    """
    Simula trabajo intensivo reemplazando bucles anidados profundos por
    un helper que controla la profundidad (evita complejidad artificial).

    Returns:
        int: acumulado “simulado” dependiente de la profundidad.
    """
    return nested_loops(DEFAULT_DEPTH)


def funcion_con_muchos_try_except_anidados_extremos() -> float:
    """
    Realiza un conjunto de operaciones controladas con manejo de errores
    específico, evitando try/except anidados y genéricos.

    Returns:
        float: resultado agregado de operaciones seguras.

    Raises:
        ValueError: si una operación segura detecta entrada inválida.
        IndexError: si se accede a un índice fuera del rango permitido.
    """
    result = 0.0
    pool = normalize_numbers(ALTERNATE_NUM_SAMPLE)

    # Evita anidamientos: usa bucle lineal con manejo de casos concreto.
    for i in range(min(DEFAULT_TRIES, len(pool))):
        # Acceso seguro a índice (puede lanzar IndexError con mensaje claro).
        value = validate_index(pool, i)

        # División segura (puede lanzar ValueError si divisor == 0).
        quotient = safe_div(value, SPLIT_DIVISOR)

        result += quotient

    return result


def funcion_con_muchos_operadores_logicos_extremos() -> bool:
    """
    Evalúa condiciones compuestas usando expresiones declarativas (any/all)
    en lugar de secuencias complejas de 'and/or' anidados.

    Returns:
        bool: True si pasa los umbrales definidos; de lo contrario False.
    """
    values = normalize_numbers(NUM_SAMPLE)

    # Reglas declarativas (fácil de extender):
    all_non_negative = all(v >= 0 for v in values)
    any_large = any(v > 10 for v in values)
    mean_ok = aggregate_stats(values)["mean"] >= 5

    # Condición compuesta, clara y lineal:
    return (all_non_negative and mean_ok) or any_large


def funcion_con_muchos_strings_magicos_extremos() -> str:
    """
    Genera una etiqueta de salida a partir de una clave conocida y
    plantillas de cadena definidas en constantes.

    Returns:
        str: etiqueta generada.
    """
    label = LABELS.get(DEFAULT_KEY)
    if label is None:
        # Manejo explícito: señaliza configuración inválida.
        raise ValueError(f"DEFAULT_KEY inválida: {DEFAULT_KEY!r}")

    # Plantilla con f-string (claro y eficiente).
    return f"[{label}] valores procesados: {len(NUM_SAMPLE)}"


def funcion_con_muchos_numeros_magicos_extremos() -> float:
    """
    Calcula un valor financiero simple evitando números mágicos en línea.
    Aplica tasas configurables y rutas de error predecibles.

    Returns:
        float: valor neto luego de descuentos/impuestos/recargos.

    Raises:
        ValueError: si ocurre división por cero al calcular prorrateos.
    """
    subtotal = sum(normalize_numbers(NUM_SAMPLE))
    tax = subtotal * TAX_RATE
    discount = subtotal * DISCOUNT_RATE
    surcharge = subtotal * SURCHARGE_RATE

    gross = subtotal + tax + surcharge - discount

    # Ejemplo de operación segura que antes podía fallar por divisor=0.
    per_unit = safe_div(gross, float(len(NUM_SAMPLE)))
    return round(per_unit, 4)


# =========================
# Helpers privados (SRP)
# =========================
def _alpha_score(mean_value: float, max_value: float) -> float:
    """
    Combina media y máximo de forma segura.

    Args:
        mean_value: promedio de la serie.
        max_value: valor máximo de la serie.

    Returns:
        float: puntuación compuesta.
    """
    # safe_div protege ante división por cero.
    ratio = safe_div(max_value, mean_value if mean_value != 0 else 1.0)
    return round(mean_value + ratio, 4)


def _beta_score(mean_value: float, min_value: float, tax_rate: float) -> float:
    """
    Aplica una transformación paramétrica (inyecta la tasa como dependencia).

    Args:
        mean_value: promedio de la serie.
        min_value: valor mínimo de la serie.
        tax_rate: tasa a aplicar (DIP: dependencia inyectada).

    Returns:
        float: puntuación resultante.
    """
    base = mean_value - min_value
    return round(base * (1 + tax_rate), 4)


def _gamma_score(values: List[float]) -> float:
    """
    Puntuación basada en dispersión (SRP: cálculo aislado).

    Args:
        values: lista de valores numéricos.

    Returns:
        float: métrica ad-hoc basada en rango/longitud.
    """
    if not values:
        raise ValueError("La lista de valores no puede estar vacía.")

    stats = aggregate_stats(values)
    spread = stats["max"] - stats["min"]
    factor = safe_div(spread, float(len(values)))
    return round(stats["mean"] + factor, 4)