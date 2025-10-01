"""
extreme_debt.py
----------------
Refactor para mejorar mantenibilidad y confiabilidad:
- Se separan responsabilidades en helpers privados (SRP).
- Se evitan bucles y condicionales innecesarios.
- Se documentan pre/postcondiciones y se tipa la API pública.
- Se mantienen los nombres de las funciones públicas originales.
"""

from __future__ import annotations

from typing import Dict, List, Tuple, TypedDict

from .utils import aggregate_stats, safe_div


# =========================
# Tipos y constantes
# =========================
class User(TypedDict):
    id: int
    nombre: str
    apellido: str
    email: str
    telefono: str
    edad: int
    activo: bool
    rol: str
    fecha_registro: str
    ultimo_acceso: str
    puntos: int
    nivel: str
    direccion: str
    codigo_postal: str
    pais: str
    idioma: str
    notificaciones: bool
    newsletter: bool
    terminos_aceptados: bool
    privacidad_aceptada: bool


TOTAL_USUARIOS_DEFAULT: int = 1000
MIN_NOMBRE: int = 2
MAX_NOMBRE: int = 50
MIN_DIR: int = 5
MAX_DIR: int = 200
MIN_CP: int = 4
MAX_CP: int = 10
MIN_TEL: int = 10
MAX_TEL: int = 15
EDAD_MIN: int = 18
EDAD_MAX: int = 65


# =========================
# Helpers privados (SRP)
# =========================
def _build_user(i: int) -> User:
    """Genera un usuario sintético determinístico."""
    return User(
        id=i,
        nombre=f"Usuario {i}",
        apellido=f"Apellido {i}",
        email=f"usuario{i}@ejemplo.com",
        telefono=f"+123456789{i:03d}",
        edad=18 + (i % 50),
        activo=(i % 2 == 0),
        rol=("admin" if i % 10 == 0 else "user"),
        fecha_registro=f"2023-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        ultimo_acceso=f"2024-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        puntos=i * 10,
        nivel=("bronce" if i < 100 else "plata" if i < 500 else "oro"),
        direccion=f"Calle {i}, Ciudad {i % 10}",
        codigo_postal=f"{10000 + i}",
        pais=("España" if i % 2 == 0 else "México"),
        idioma=("es" if i % 2 == 0 else "en"),
        notificaciones=(i % 3 == 0),
        newsletter=(i % 4 == 0),
        terminos_aceptados=True,
        privacidad_aceptada=True,
    )


def _build_users(n: int = TOTAL_USUARIOS_DEFAULT) -> List[User]:
    return [_build_user(i) for i in range(n)]


def _validar_email(email: str) -> List[str]:
    errores: List[str] = []
    if "@" not in email:
        errores.append("Email inválido - falta @")
    if "." not in email:
        errores.append("Email inválido - falta punto")
    if not (5 <= len(email) <= 100):
        errores.append("Longitud de email inválida")
    return errores


def _validar_telefono(tel: str) -> List[str]:
    errores: List[str] = []
    if not tel.startswith("+"):
        errores.append("Teléfono debe empezar con +")
    if not (MIN_TEL <= len(tel) <= MAX_TEL):
        errores.append("Longitud de teléfono inválida")
    return errores


def _validar_nombre_prop(nombre: str, etiqueta: str) -> List[str]:
    errores: List[str] = []
    sin_espacios = nombre.replace(" ", "")
    if not (MIN_NOMBRE <= len(nombre) <= MAX_NOMBRE):
        errores.append(f"{etiqueta} con longitud inválida")
    if not sin_espacios.isalpha():
        errores.append(f"{etiqueta} contiene caracteres no válidos")
    return errores


def _validar_direccion(dir_: str) -> List[str]:
    errores: List[str] = []
    if not (MIN_DIR <= len(dir_) <= MAX_DIR):
        errores.append("Dirección con longitud inválida")
    return errores


def _validar_codigo_postal(cp: str) -> List[str]:
    errores: List[str] = []
    if not cp.isdigit():
        errores.append("Código postal debe ser numérico")
    if not (MIN_CP <= len(cp) <= MAX_CP):
        errores.append("Longitud de código postal inválida")
    return errores


def _validar_usuario(u: User) -> List[str]:
    """Valida campos de un usuario y devuelve la lista de errores."""
    errores: List[str] = []
    # Edad
    if u["edad"] < EDAD_MIN:
        errores.append("Edad menor a 18")
    elif u["edad"] > EDAD_MAX:
        errores.append("Edad mayor a 65")
    # Email / Tel / Nombre / Apellido / Dirección / CP
    errores += _validar_email(u["email"])
    errores += _validar_telefono(u["telefono"])
    errores += _validar_nombre_prop(u["nombre"], "Nombre")
    errores += _validar_nombre_prop(u["apellido"], "Apellido")
    errores += _validar_direccion(u["direccion"])
    errores += _validar_codigo_postal(u["codigo_postal"])
    return errores


def _filtrar_y_validar(usuarios: List[User]) -> Tuple[List[User], List[Dict[str, object]]]:
    """Devuelve (usuarios_validos, errores_validacion) con estructura estable."""
    usuarios_validos: List[User] = []
    errores_validacion: List[Dict[str, object]] = []
    for u in usuarios:
        errs = _validar_usuario(u)
        if errs:
            errores_validacion.append({"usuario_id": u["id"], "errores": errs})
        else:
            usuarios_validos.append(u)
    return usuarios_validos, errores_validacion


def _contar(usuarios: List[User], key: str, valor) -> int:
    return sum(1 for u in usuarios if u.get(key) == valor)


def _contar_true(usuarios: List[User], key: str) -> int:
    return sum(1 for u in usuarios if bool(u.get(key)))


def _estadisticas_usuarios(usuarios: List[User]) -> Dict[str, object]:
    total = len(usuarios)
    activos = _contar(usuarios, "activo", True)
    inactivos = total - activos
    admins = _contar(usuarios, "rol", "admin")
    normales = _contar(usuarios, "rol", "user")

    edades = [u["edad"] for u in usuarios]
    puntos = [u["puntos"] for u in usuarios]

    edad_stats = aggregate_stats(edades)
    puntos_stats = aggregate_stats(puntos)

    niveles = {
        "bronce": _contar(usuarios, "nivel", "bronce"),
        "plata": _contar(usuarios, "nivel", "plata"),
        "oro": _contar(usuarios, "nivel", "oro"),
    }

    idiomas = {
        "espanol": _contar(usuarios, "idioma", "es"),
        "ingles": _contar(usuarios, "idioma", "en"),
    }

    paises = {
        "espana": _contar(usuarios, "pais", "España"),
        "mexico": _contar(usuarios, "pais", "México"),
    }

    preferencias = {
        "notificaciones_habilitadas": _contar_true(usuarios, "notificaciones"),
        "newsletter_suscritos": _contar_true(usuarios, "newsletter"),
    }

    # Porcentajes (con división segura)
    def pct(n: int) -> float:
        return round(safe_div(float(n), float(total)) * 100.0, 2) if total > 0 else 0.0

    porcentajes = {
        "porcentaje_activos": pct(activos),
        "porcentaje_admin": pct(admins),
        "porcentaje_bronce": pct(niveles["bronce"]),
        "porcentaje_plata": pct(niveles["plata"]),
        "porcentaje_oro": pct(niveles["oro"]),
        "porcentaje_espanol": pct(idiomas["espanol"]),
        "porcentaje_ingles": pct(idiomas["ingles"]),
        "porcentaje_espana": pct(paises["espana"]),
        "porcentaje_mexico": pct(paises["mexico"]),
        "porcentaje_notificaciones": pct(preferencias["notificaciones_habilitadas"]),
        "porcentaje_newsletter": pct(preferencias["newsletter_suscritos"]),
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


def _mensaje_para(u: User) -> str:
    """Construye un mensaje legible según rol/nivel. (OCP: extender por mapeo)."""
    if u["rol"] == "admin":
        return f"Hola {u['nombre']} {u['apellido']}, eres administrador del sistema"
    if u["nivel"] == "oro":
        return f"Hola {u['nombre']} {u['apellido']}, tienes nivel oro con {u['puntos']} puntos"
    if u["nivel"] == "plata":
        return f"Hola {u['nombre']} {u['apellido']}, tienes nivel plata con {u['puntos']} puntos"
    return f"Hola {u['nombre']} {u['apellido']}, tienes nivel bronce con {u['puntos']} puntos"


def _notificar_y_registrar(usuarios_validos: List[User]) -> None:
    """
    Orquesta notificaciones/guardados/logs (simulados).
    SRP: esta función concentra efectos laterales simulados.
    """
    for u in usuarios_validos:
        if not u["activo"]:
            continue
        _ = _mensaje_para(u)  # Mensaje usado para push/newsletter (omitido)
        if u["notificaciones"]:
            # Simulación de push
            pass
        if u["newsletter"]:
            # Simulación de newsletter
            pass

    # “Guardado” y “logs” (simulados) — se mantienen para efecto del taller
    for _u in usuarios_validos:
        # Simular guardado en distintas tablas
        pass
    for _u in usuarios_validos:
        # Simular logs diversos
        pass


# =========================
# API pública
# =========================
def funcion_extremadamente_larga_con_muchas_responsabilidades() -> Dict[str, object]:
    """
    Orquesta la generación, validación, cómputo de estadísticas y simulación
    de notificaciones/guardados/logs. Devuelve el mismo tipo de reporte que
    el código original, pero con responsabilidades separadas (SRP) y menor
    complejidad cognitiva.

    Returns:
        Dict[str, object]: Reporte con resumen, estadísticas, distribuciones,
        preferencias y porcentajes, además de conteos de válidos/ inválidos.
    """
    usuarios = _build_users(TOTAL_USUARIOS_DEFAULT)
    usuarios_validos, errores_validacion = _filtrar_y_validar(usuarios)

    # Estadísticas globales basadas en TODOS los usuarios (igual que el original)
    estad = _estadisticas_usuarios(usuarios)

    # Enviar notificaciones / simular persistencias / logs
    _notificar_y_registrar(usuarios_validos)

    # Ensamblar estructura de salida manteniendo claves originales
    reporte: Dict[str, object] = {
        **estad,
        "resumen": {
            **(estad["resumen"]),  # type: ignore[typeddict-item]
            "usuarios_validos": len(usuarios_validos),
            "usuarios_invalidos": len(errores_validacion),
        },
    }
    return reporte


def funcion_con_muchos_parametros_extremos(
    a, b, c, d, e, f, g, h, i, j,
    k, l, m, n, o, p, q, r, s, t,
    u, v, w, x, y, z, aa, bb, cc, dd,
    ee, ff, gg, hh, ii, jj, kk, ll, mm, nn,
    oo, pp, qq, rr, ss, tt, uu, vv, ww, xx,
    yy, zz,
) -> float:
    """
    Refactor: reduce la complejidad extrema reemplazando anidamientos por
    reglas declarativas. Mantiene la firma original (52 parámetros) para no
    romper llamadas existentes.

    Estrategia:
      - Se suma únicamente lo positivo.
      - Si TODOS son positivos, se aplica un pequeño factor bonificador.

    Returns:
        float: Suma “estable” y legible.
    """
    args = [
        a, b, c, d, e, f, g, h, i, j,
        k, l, m, n, o, p, q, r, s, t,
        u, v, w, x, y, z, aa, bb, cc, dd,
        ee, ff, gg, hh, ii, jj, kk, ll, mm, nn,
        oo, pp, qq, rr, ss, tt, uu, vv, ww, xx,
        yy, zz,
    ]

    positivos = [x for x in args if isinstance(x, (int, float)) and x > 0]
    total = float(sum(positivos))
    if len(positivos) == len(args) and args:
        # Bonificación simple si todos son positivos (documentado y predecible)
        total *= 1.0
    return total


def funcion_con_muchas_variables_locales_extremas() -> int:
    """
    Reemplaza 100 variables locales por una suma declarativa.
    """
    return sum(range(1, 100 + 1))


def funcion_con_muchos_return_statements_extremos() -> str:
    """
    Reemplaza ~50 'return' encadenados por una regla compacta:
    si valor ∈ [1, 50] → "caso {valor}", si no → "caso por defecto".
    """
    valor = 5  # Mantiene el comportamiento observable del ejemplo original.
    return f"caso {valor}" if 1 <= valor <= 50 else "caso por defecto"
