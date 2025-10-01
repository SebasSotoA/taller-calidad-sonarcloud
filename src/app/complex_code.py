"""
Archivo adicional con problemas de mantenibilidad para aumentar Technical Debt Ratio.
"""

from typing import Dict, Iterable, List, Tuple

# Constantes para evitar números y cadenas mágicas
MIN_EDAD: int = 18
MAX_EDAD: int = 65
ROLES_VALIDOS: Tuple[str, ...] = (
    "admin",
    "user",
    "guest",
    "root",
    "superuser",
    "moderator",
    "editor",
    "viewer",
    "anonymous",
    "public",
)


def _construir_usuarios(n: int = 100) -> List[Dict]:
    return [
        {
            "id": i,
            "nombre": f"Usuario {i}",
            "email": f"usuario{i}@ejemplo.com",
            "edad": 20 + (i % 50),
            "activo": i % 2 == 0,
        }
        for i in range(n)
    ]


def _es_email_valido(email: str) -> bool:
    return "@" in email and "." in email


def _validar_usuarios(usuarios: Iterable[Dict]) -> List[Dict]:
    validos: List[Dict] = []
    for u in usuarios:
        if MIN_EDAD <= u.get("edad", 0) <= MAX_EDAD and _es_email_valido(u.get("email", "")) and len(u.get("nombre", "")) >= 2:
            validos.append(u)
    return validos


def _estadisticas_usuarios(usuarios: List[Dict]) -> Dict:
    total = len(usuarios)
    if total == 0:
        return {
            "total_usuarios": 0,
            "usuarios_validos": 0,
            "usuarios_activos": 0,
            "edad_promedio": 0.0,
            "edad_minima": 0,
            "edad_maxima": 0,
            "porcentaje_activos": 0.0,
        }
    activos = sum(1 for u in usuarios if u.get("activo"))
    edades = [u.get("edad", 0) for u in usuarios]
    return {
        "total_usuarios": total,
        "usuarios_activos": activos,
        "edad_promedio": sum(edades) / total,
        "edad_minima": min(edades),
        "edad_maxima": max(edades),
        "porcentaje_activos": (activos / total) * 100,
    }

def funcion_muy_larga_con_muchas_responsabilidades() -> Dict:
    """Orquesta pasos específicos delegando en helpers (SRP)."""
    usuarios = _construir_usuarios(100)
    usuarios_validos = _validar_usuarios(usuarios)
    reporte = _estadisticas_usuarios(usuarios)
    # Podríamos notificar/guardar mediante servicios inyectables; omitido para mantener pureza
    reporte["usuarios_validos"] = len(usuarios_validos)
    return reporte


def funcion_con_muchos_parametros_y_logica_compleja(
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
):
    """Reduce complejidad: suma únicamente parámetros positivos.

    Nota: Se conserva la firma para compatibilidad, aunque es preferible
    aceptar una lista/iterable en diseño real.
    """
    params = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    return sum(p for p in params if isinstance(p, (int, float)) and p > 0)


def funcion_con_muchas_variables_y_operaciones() -> float:
    """Calcula de forma compacta sin variables intermedias innecesarias."""
    base = sum(range(1, 31))  # 1..30
    # Secuencia de transformaciones clara y encadenada
    resultado = base
    for op in (
        ("mul", 2),
        ("div", 3),
        ("add", 100),
        ("sub", 50),
        ("mul", 1.5),
        ("div", 2.5),
        ("add", 200),
        ("sub", 75),
        ("mul", 2.2),
        ("div", 1.8),
        ("add", 300),
        ("sub", 100),
        ("mul", 1.7),
        ("div", 2.3),
        ("add", 400),
        ("sub", 125),
        ("mul", 1.9),
        ("div", 2.1),
        ("add", 500),
        ("sub", 150),
    ):
        op_type, value = op
        if op_type == "mul":
            resultado *= value
        elif op_type == "div":
            resultado /= value
        elif op_type == "add":
            resultado += value
        elif op_type == "sub":
            resultado -= value
    return resultado


def funcion_con_muchos_comentarios_redundantes() -> int:
    """Suma pares y resta impares en 1..9 sin logs ni comentarios redundantes."""
    resultado = 0
    for i in range(10):
        if i == 0:
            continue
        resultado += i if i % 2 == 0 else -i
    return resultado


def funcion_con_muchos_imports_no_usados() -> int:
    """Evita imports innecesarios y retorna un valor determinista."""
    return 42


def funcion_con_muchos_strings_magicos(role_checks: Iterable[str] = ROLES_VALIDOS) -> str:
    """Valida que todos los roles recibidos pertenezcan al conjunto permitido."""
    for role in role_checks:
        if role not in ROLES_VALIDOS:
            return "error"
    return "success"


def funcion_con_muchos_numeros_magicos() -> int:
    """Evita cascadas de if con números duros; retorna el máximo de una secuencia."""
    numeros = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    return max(numeros)
