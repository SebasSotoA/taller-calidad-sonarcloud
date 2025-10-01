# app/utils/debt_utils.py
"""
Helpers reutilizables para refactorización y reducción de duplicación en módulos de deuda técnica.
Proveen operaciones seguras (safe_div, validate_index), normalización y utilidades
para despachar estrategias y simular bucles anidados sin complejidad artificial.
Incluye validadores y utilidades de conteo/porcentaje y armado de usuarios base.
"""

from __future__ import annotations

from typing import Callable, Iterable, Sequence, TypeVar, Optional, Mapping, Any, Dict, List

T = TypeVar("T")

# ---------------------------
# Constantes de validación
# ---------------------------
NAME_BOUNDS = (2, 50)
ADDRESS_BOUNDS = (5, 200)
POSTAL_BOUNDS = (4, 10)
PHONE_BOUNDS = (10, 15)
AGE_BOUNDS = (18, 65)


def safe_div(a: float, b: float) -> float:
    """Divide a entre b validando que b no sea cero."""
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b


def dispatch_by_key(
    key: str,
    table: Mapping[str, Callable[[], T]],
    default: Optional[Callable[[], T]] = None,
) -> T:
    """Despacha por clave a una función sin argumentos."""
    fn = table.get(key)
    if fn is not None:
        return fn()
    if default is not None:
        return default()
    raise KeyError(f"Clave '{key}' no encontrada en tabla de despacho.")


def nested_loops(depth: int) -> int:
    """
    Simula bucles anidados de profundidad dada de forma O(1).
    Retorna 2**depth - 1 para depth>=1.
    """
    if depth < 1:
        raise ValueError("La profundidad debe ser al menos 1.")
    return (1 << depth) - 1  # 2**depth - 1


def normalize_numbers(valores: Iterable[float]) -> list[float]:
    """Normaliza una lista de números al rango [0, 1]."""
    xs = list(valores)
    if not xs:
        raise ValueError("La lista de valores está vacía.")
    mn, mx = min(xs), max(xs)
    if mn == mx:
        raise ValueError("Todos los valores son iguales; no se puede normalizar.")
    span = mx - mn
    return [(v - mn) / span for v in xs]


def aggregate_stats(valores: Iterable[float]) -> dict[str, float]:
    """Devuelve min, max, mean, var para una lista de números."""
    xs = list(valores)
    if not xs:
        raise ValueError("La lista de valores está vacía.")
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return {"min": min(xs), "max": max(xs), "mean": mean, "var": var}


def validate_index(seq: Sequence[T], idx: int) -> T:
    """Acceso seguro a índice de una secuencia."""
    if idx < 0 or idx >= len(seq):
        raise IndexError(f"Índice {idx} fuera de rango para secuencia de tamaño {len(seq)}.")
    return seq[idx]


# ---------------------------
# Validadores comunes
# ---------------------------
def validate_email(email: str) -> List[str]:
    errs: List[str] = []
    if "@" not in email:
        errs.append("Email inválido - falta @")
    if "." not in email:
        errs.append("Email inválido - falta punto")
    if not (5 <= len(email) <= 100):
        errs.append("Longitud de email inválida")
    return errs


def validate_phone(tel: str) -> List[str]:
    errs: List[str] = []
    min_tel, max_tel = PHONE_BOUNDS
    if not tel.startswith("+"):
        errs.append("Teléfono debe empezar con +")
    if not (min_tel <= len(tel) <= max_tel):
        errs.append("Longitud de teléfono inválida")
    return errs


def validate_name(nombre: str, etiqueta: str = "Nombre") -> List[str]:
    errs: List[str] = []
    min_n, max_n = NAME_BOUNDS
    sin_espacios = nombre.replace(" ", "")
    if not (min_n <= len(nombre) <= max_n):
        errs.append(f"{etiqueta} con longitud inválida")
    if not sin_espacios.isalpha():
        errs.append(f"{etiqueta} contiene caracteres no válidos")
    return errs


def validate_address(dir_: str) -> List[str]:
    errs: List[str] = []
    min_d, max_d = ADDRESS_BOUNDS
    if not (min_d <= len(dir_) <= max_d):
        errs.append("Dirección con longitud inválida")
    return errs


def validate_postal_code(cp: str) -> List[str]:
    errs: List[str] = []
    min_cp, max_cp = POSTAL_BOUNDS
    if not cp.isdigit():
        errs.append("Código postal debe ser numérico")
    if not (min_cp <= len(cp) <= max_cp):
        errs.append("Longitud de código postal inválida")
    return errs


def validate_user_basic(u: Mapping[str, Any]) -> List[str]:
    """Valida campos básicos de un usuario común a extreme/mega."""
    errs: List[str] = []
    min_age, max_age = AGE_BOUNDS
    edad = int(u.get("edad", 0))
    if edad < min_age:
        errs.append("Edad menor a 18")
    elif edad > max_age:
        errs.append("Edad mayor a 65")
    errs += validate_email(str(u.get("email", "")))
    errs += validate_phone(str(u.get("telefono", "")))
    errs += validate_name(str(u.get("nombre", "")), "Nombre")
    errs += validate_name(str(u.get("apellido", "")), "Apellido")
    errs += validate_address(str(u.get("direccion", "")))
    errs += validate_postal_code(str(u.get("codigo_postal", "")))
    return errs


# ---------------------------
# Conteos y porcentajes
# ---------------------------
def count_equals(items: Iterable[Mapping[str, Any]], key: str, value: Any) -> int:
    return sum(1 for it in items if it.get(key) == value)


def count_truthy(items: Iterable[Mapping[str, Any]], key: str) -> int:
    return sum(1 for it in items if bool(it.get(key)))


def pct(n: int, total: int) -> float:
    return round(safe_div(float(n), float(total)) * 100.0, 2) if total > 0 else 0.0


# ---------------------------
# Usuario base y estadísticas básicas
# ---------------------------
def build_user_basic(i: int) -> Dict[str, Any]:
    """Crea un usuario base con los campos compartidos por extreme/mega."""
    return {
        "id": i,
        "nombre": f"Usuario {i}",
        "apellido": f"Apellido {i}",
        "email": f"usuario{i}@ejemplo.com",
        "telefono": f"+123456789{i:03d}",
        "edad": 18 + (i % 50),
        "activo": (i % 2 == 0),
        "rol": ("admin" if i % 10 == 0 else "user"),
        "fecha_registro": f"2023-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        "ultimo_acceso": f"2024-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        "puntos": i * 10,
        "nivel": ("bronce" if i < 100 else "plata" if i < 500 else "oro"),
        "direccion": f"Calle {i}, Ciudad {i % 10}",
        "codigo_postal": f"{10000 + i}",
        "pais": ("España" if i % 2 == 0 else "México"),
        "idioma": ("es" if i % 2 == 0 else "en"),
        "notificaciones": (i % 3 == 0),
        "newsletter": (i % 4 == 0),
        "terminos_aceptados": True,
        "privacidad_aceptada": True,
    }


def compute_basic_stats(usuarios: List[Mapping[str, Any]]) -> Dict[str, Any]:
    """Estadísticas y distribuciones comunes para extreme/mega (parte básica)."""
    total = len(usuarios)
    activos = count_equals(usuarios, "activo", True)
    inactivos = total - activos
    admins = count_equals(usuarios, "rol", "admin")
    normales = count_equals(usuarios, "rol", "user")

    edad_stats = aggregate_stats([u["edad"] for u in usuarios])
    puntos_stats = aggregate_stats([u["puntos"] for u in usuarios])

    niveles = {
        "bronce": count_equals(usuarios, "nivel", "bronce"),
        "plata": count_equals(usuarios, "nivel", "plata"),
        "oro": count_equals(usuarios, "nivel", "oro"),
    }
    idiomas = {
        "espanol": count_equals(usuarios, "idioma", "es"),
        "ingles": count_equals(usuarios, "idioma", "en"),
    }
    paises = {
        "espana": count_equals(usuarios, "pais", "España"),
        "mexico": count_equals(usuarios, "pais", "México"),
    }
    preferencias = {
        "notificaciones_habilitadas": count_truthy(usuarios, "notificaciones"),
        "newsletter_suscritos": count_truthy(usuarios, "newsletter"),
    }

    porcentajes = {
        "porcentaje_activos": pct(activos, total),
        "porcentaje_admin": pct(admins, total),
        "porcentaje_bronce": pct(niveles["bronce"], total),
        "porcentaje_plata": pct(niveles["plata"], total),
        "porcentaje_oro": pct(niveles["oro"], total),
        "porcentaje_espanol": pct(idiomas["espanol"], total),
        "porcentaje_ingles": pct(idiomas["ingles"], total),
        "porcentaje_espana": pct(paises["espana"], total),
        "porcentaje_mexico": pct(paises["mexico"], total),
        "porcentaje_notificaciones": pct(preferencias["notificaciones_habilitadas"], total),
        "porcentaje_newsletter": pct(preferencias["newsletter_suscritos"], total),
    }

    return {
        "resumen": {
            "total_usuarios": total,
            "usuarios_activos": activos,
            "usuarios_inactivos": inactivos,
            "usuarios_admin": admins,
            "usuarios_normales": normales,
        },
        "estadisticas_edad": {
            "promedio": edad_stats["mean"],
            "minima": edad_stats["min"],
            "maxima": edad_stats["max"],
        },
        "estadisticas_puntos": {
            "promedio": puntos_stats["mean"],
            "minimos": puntos_stats["min"],
            "maximos": puntos_stats["max"],
        },
        "distribucion_niveles": niveles,
        "distribucion_idiomas": idiomas,
        "distribucion_paises": paises,
        "preferencias": preferencias,
        "porcentajes": porcentajes,
    }
