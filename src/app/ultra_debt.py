"""
ultra_debt.py
-------------
Refactorizado para eliminar duplicación, reducir complejidad y mejorar mantenibilidad.
Mantiene las firmas públicas y evita malas prácticas (variables locales masivas,
cascadas de returns, try/except innecesarios, números/strings mágicos).
"""

from __future__ import annotations

from .utils import nested_loops

# =========================
# Constantes (evitan “magic numbers”)
# =========================
MAX_LOCAL_VARS: int = 200
RETURN_MAX_CASE: int = 100
RANGE_LIMIT: int = 20
DEFAULT_NESTED_DEPTH: int = 15
TRY_LEVELS: int = 30


def funcion_con_variables_locales_masivas() -> int:
    """
    Reemplaza 200 variables locales por una construcción declarativa.
    SRP: una única responsabilidad clara (sumar una secuencia definida).

    Returns:
        int: Suma de 1..MAX_LOCAL_VARS.
    """
    # Evita 200 asignaciones locales: usa una secuencia generada.
    return sum(range(1, MAX_LOCAL_VARS + 1))


def funcion_con_return_statements_masivos() -> str:
    """
    Reemplaza ~100 'return' encadenados por una regla simple y clara (OCP-friendly).
    Si el valor está en 1..RETURN_MAX_CASE, devuelve "caso {valor}", de lo contrario
    "caso por defecto".

    Returns:
        str: Texto del caso evaluado.
    """
    valor = 5  # Mantiene el comportamiento observable original
    if 1 <= valor <= RETURN_MAX_CASE:
        return f"caso {valor}"
    return "caso por defecto"


def funcion_con_complejidad_ciclamatica_masiva() -> int:
    """
    Cálculo compacto y legible que evita anidamientos artificiales.

    Returns:
        int: Suma de i*(i+1) para i en [0, RANGE_LIMIT).
    """
    return sum(i * (i + 1) for i in range(RANGE_LIMIT))


def funcion_con_bucles_anidados_masivos() -> int:
    """
    Simula bucles anidados usando un helper reutilizable (evita complejidad profunda).

    Returns:
        int: Acumulado simulado dependiente de DEFAULT_NESTED_DEPTH.
    """
    return nested_loops(DEFAULT_NESTED_DEPTH)


def funcion_con_try_except_masivos() -> int:
    """
    Evita try/except anidados e innecesarios. Implementa la intención de forma
    determinística y clara.

    Returns:
        int: Suma de (n + 1) para n en [0, TRY_LEVELS).
    """
    # El comportamiento original acumulaba n+1 en un bucle con try/except que nunca fallaba.
    # Se expresa de manera explícita, sin capturas redundantes.
    return sum(n + 1 for n in range(TRY_LEVELS))