"""
mega_debt.py
-------------
Refactor para mejorar mantenibilidad y confiabilidad:
- Se separan responsabilidades en helpers privados (SRP).
- Se usan utilidades comunes (aggregate_stats, safe_div).
- Se reducen bucles/condicionales repetidos y números mágicos.
- Se mantienen los nombres de las funciones públicas originales.
"""

from __future__ import annotations

from typing import Dict, List, Tuple, TypedDict, Any

from .utils import aggregate_stats, safe_div


# =========================
# Tipos y constantes
# =========================
class User(TypedDict, total=False):
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

    # Campos “masivos” adicionales
    preferencias: Dict[str, Any]
    configuracion: Dict[str, Any]
    estadisticas: Dict[str, int]
    historial: List[str]
    favoritos: List[str]
    seguidores: int
    siguiendo: int
    posts: int
    comentarios: int
    likes_recibidos: int
    likes_dados: int
    compartidos: int
    grupos: List[str]
    eventos: List[str]
    mensajes_enviados: int
    mensajes_recibidos: int
    archivos_subidos: int
    espacio_usado: int
    limite_espacio: int
    premium: bool
    fecha_premium: str | None
    metodos_pago: List[str]
    facturacion: Dict[str, bool]
    ultima_actividad: str
    dispositivos: List[str]
    sesiones_activas: int
    ip_ultima: str
    user_agent: str
    referrer: str
    utm_source: str
    utm_medium: str
    utm_campaign: str
    utm_term: str
    utm_content: str
    geolocalizacion: Dict[str, float]
    zona_horaria: str
    idioma_nativo: str
    moneda: str
    formato_fecha: str
    formato_hora: str
    unidades: str
    temperatura: str


TOTAL_USUARIOS_DEFAULT: int = 5000

# Reglas de validación (evitan “magic numbers”)
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
    """Genera un usuario sintético determinístico con campos “masivos”."""
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
        preferencias={
            "tema": "oscuro" if i % 2 == 0 else "claro",
            "idioma": "es" if i % 2 == 0 else "en",
        },
        configuracion={
            "notificaciones_push": True,
            "notificaciones_email": True,
            "notificaciones_sms": False,
        },
        estadisticas={
            "visitas": i * 5,
            "tiempo_sesion": i * 10,
            "paginas_vistas": i * 3,
        },
        historial=[f"accion_{j}" for j in range(i % 10)],
        favoritos=[f"item_{j}" for j in range(i % 5)],
        seguidores=i % 100,
        siguiendo=i % 50,
        posts=i % 20,
        comentarios=i % 30,
        likes_recibidos=i % 200,
        likes_dados=i % 150,
        compartidos=i % 25,
        grupos=[f"grupo_{j}" for j in range(i % 3)],
        eventos=[f"evento_{j}" for j in range(i % 2)],
        mensajes_enviados=i % 40,
        mensajes_recibidos=i % 35,
        archivos_subidos=i % 15,
        espacio_usado=i * 1024,
        limite_espacio=1_000_000,
        premium=(i % 20 == 0),
        fecha_premium=(
            f"2024-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}" if i % 20 == 0 else None
        ),
        metodos_pago=[f"tarjeta_{j}" for j in range(i % 2)],
        facturacion={"mensual": i % 2 == 0, "anual": i % 3 == 0},
        ultima_actividad=f"2024-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        dispositivos=[f"dispositivo_{j}" for j in range(i % 3)],
        sesiones_activas=i % 2,
        ip_ultima=f"192.168.1.{i % 255}",
        user_agent=f"Browser_{i % 10}",
        referrer=f"site_{i % 5}.com",
        utm_source=f"source_{i % 3}",
        utm_medium=f"medium_{i % 2}",
        utm_campaign=f"campaign_{i % 4}",
        utm_term=f"term_{i % 6}",
        utm_content=f"content_{i % 3}",
        geolocalizacion={"lat": 40.4168 + (i % 100) / 1000, "lng": -3.7038 + (i % 100) / 1000},
        zona_horaria=("Europe/Madrid" if i % 2 == 0 else "America/Mexico_City"),
        idioma_nativo=("es" if i % 2 == 0 else "en"),
        moneda=("EUR" if i % 2 == 0 else "USD"),
        formato_fecha=("DD/MM/YYYY" if i % 2 == 0 else "MM/DD/YYYY"),
        formato_hora=("24h" if i % 2 == 0 else "12h"),
        unidades=("metric" if i % 2 == 0 else "imperial"),
        temperatura=("celsius" if i % 2 == 0 else "fahrenheit"),
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


def _estadisticas_basicas(usuarios: List[User]) -> Dict[str, Any]:
    total = len(usuarios)
    activos = _contar(usuarios, "activo", True)
    inactivos = total - activos
    admins = _contar(usuarios, "rol", "admin")
    normales = _contar(usuarios, "rol", "user")

    # Estadísticos de edad y puntos
    edad_stats = aggregate_stats([u["edad"] for u in usuarios])
    puntos_stats = aggregate_stats([u["puntos"] for u in usuarios])

    # Distribuciones sencillas
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
        "tema_oscuro": sum(1 for u in usuarios if u["preferencias"]["tema"] == "oscuro"),
        "tema_claro": sum(1 for u in usuarios if u["preferencias"]["tema"] == "claro"),
        "notificaciones_push": sum(1 for u in usuarios if u["configuracion"]["notificaciones_push"]),
        "notificaciones_email": sum(1 for u in usuarios if u["configuracion"]["notificaciones_email"]),
        "notificaciones_sms": sum(1 for u in usuarios if u["configuracion"]["notificaciones_sms"]),
    }

    # Totales de uso/actividad
    uso = {
        "total_visitas": sum(u["estadisticas"]["visitas"] for u in usuarios),
        "total_tiempo_sesion": sum(u["estadisticas"]["tiempo_sesion"] for u in usuarios),
        "total_paginas_vistas": sum(u["estadisticas"]["paginas_vistas"] for u in usuarios),
        "total_seguidores": sum(u["seguidores"] for u in usuarios),
        "total_siguiendo": sum(u["siguiendo"] for u in usuarios),
        "total_posts": sum(u["posts"] for u in usuarios),
        "total_comentarios": sum(u["comentarios"] for u in usuarios),
        "total_likes_recibidos": sum(u["likes_recibidos"] for u in usuarios),
        "total_likes_dados": sum(u["likes_dados"] for u in usuarios),
        "total_compartidos": sum(u["compartidos"] for u in usuarios),
        "total_mensajes_enviados": sum(u["mensajes_enviados"] for u in usuarios),
        "total_mensajes_recibidos": sum(u["mensajes_recibidos"] for u in usuarios),
        "total_archivos_subidos": sum(u["archivos_subidos"] for u in usuarios),
        "total_espacio_usado": sum(u["espacio_usado"] for u in usuarios),
        "total_soporte_tickets": sum(u["soporte_tickets"] for u in usuarios),
        "total_tickets_resueltos": sum(u["tickets_resueltos"] for u in usuarios),
        "satisfaccion_promedio": safe_div(
            float(sum(u["satisfaccion"] for u in usuarios)), float(total)
        )
        if total > 0
        else 0.0,
        "total_sesiones_activas": sum(u["sesiones_activas"] for u in usuarios),
    }

    # Otros contadores
    premium = sum(1 for u in usuarios if u["premium"])

    # Porcentajes con división segura
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
        "porcentaje_premium": pct(premium),
        "porcentaje_tema_oscuro": pct(preferencias["tema_oscuro"]),
        "porcentaje_tema_claro": pct(preferencias["tema_claro"]),
    }

    return {
        "resumen": {
            "total_usuarios": total,
            "usuarios_activos": activos,
            "usuarios_inactivos": inactivos,
            "usuarios_admin": admins,
            "usuarios_normales": normales,
            "usuarios_premium": premium,
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
        "estadisticas_uso": uso,
        "porcentajes": porcentajes,
    }


def _mensaje_para(u: User) -> str:
    """Construye un mensaje legible según rol/nivel."""
    if u["rol"] == "admin":
        return f"Hola {u['nombre']} {u['apellido']}, eres administrador del sistema"
    if u["nivel"] == "oro":
        return f"Hola {u['nombre']} {u['apellido']}, tienes nivel oro con {u['puntos']} puntos"
    if u["nivel"] == "plata":
        return f"Hola {u['nombre']} {u['apellido']}, tienes nivel plata con {u['puntos']} puntos"
    return f"Hola {u['nombre']} {u['apellido']}, tienes nivel bronce con {u['puntos']} puntos"


def _notificar_y_registrar(usuarios_validos: List[User]) -> None:
    """
    Orquesta notificaciones/guardados/logs (simulados) sin try/except genéricos.
    """
    for u in usuarios_validos:
        if not u["activo"]:
            continue
        _ = _mensaje_para(u)
        if u["notificaciones"]:
            if u["configuracion"]["notificaciones_push"]:
                pass
            if u["configuracion"]["notificaciones_email"]:
                pass
            if u["configuracion"]["notificaciones_sms"]:
                pass
        if u["newsletter"]:
            pass

    # Simulaciones de persistencia y logs (mantener para el taller)
    for _u in usuarios_validos:
        pass
    for _u in usuarios_validos:
        pass


# =========================
# API pública
# =========================
def funcion_mega_larga_con_responsabilidades_masivas() -> Dict[str, Any]:
    """
    Orquesta la generación, validación, cálculo de estadísticas y simulación
    de notificaciones/guardados/logs. Devuelve un reporte con la misma forma
    que el original, pero con responsabilidades separadas y baja complejidad.
    """
    usuarios = _build_users(TOTAL_USUARIOS_DEFAULT)
    usuarios_validos, errores_validacion = _filtrar_y_validar(usuarios)

    # Estadísticas y contadores (sobre TODOS los usuarios, como el original)
    estad = _estadisticas_basicas(usuarios)

    # Simula notificaciones/persistencia/logs para los válidos
    _notificar_y_registrar(usuarios_validos)

    # Ensambla reporte final, agregando válidos/ inválidos al resumen
    reporte: Dict[str, Any] = {
        **estad,
        "resumen": {
            **(estad["resumen"]),  # type: ignore[typeddict-item]
            "usuarios_validos": len(usuarios_validos),
            "usuarios_invalidos": len(errores_validacion),
        },
    }
    return reporte


def funcion_con_parametros_masivos(
    a, b, c, d, e, f, g, h, i, j,
    k, l, m, n, o, p, q, r, s, t,
    u, v, w, x, y, z, aa, bb, cc, dd,
    ee, ff, gg, hh, ii, jj, kk, ll, mm, nn,
    oo, pp, qq, rr, ss, tt, uu, vv, ww, xx,
    yy, zz, aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, jjj, kkk, lll, mmm, nnn,
    ooo, ppp, qqq, rrr, sss, ttt, uuu, vvv, www, xxx, yyy, zzz,
    aaaa, bbbb, cccc, dddd, eeee, ffff, gggg, hhhh, iiii, jjjj, kkkk, llll, mmmm, nnnn, oooo,
    pppp, qqqq, rrrr, ssss, tttt, uuuu, vvvv, wwww, xxxx, yyyy, zzzz,
) -> float:
    """
    Refactor: reduce la complejidad extrema reemplazando anidamientos por
    reglas declarativas. Mantiene la firma original (104 parámetros) para no
    romper llamadas existentes.

    Estrategia:
      - Se suman únicamente los valores numéricos > 0.
      - Si TODOS los argumentos son numéricos y > 0, se aplica una bonificación
        (aquí neutra = 1.0) para mantener comportamiento estable/predecible.

    Returns:
        float: Suma legible y determinista.
    """
    args = [
        a, b, c, d, e, f, g, h, i, j,
        k, l, m, n, o, p, q, r, s, t,
        u, v, w, x, y, z, aa, bb, cc, dd,
        ee, ff, gg, hh, ii, jj, kk, ll, mm, nn,
        oo, pp, qq, rr, ss, tt, uu, vv, ww, xx,
        yy, zz, aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, jjj, kkk, lll, mmm, nnn,
        ooo, ppp, qqq, rrr, sss, ttt, uuu, vvv, www, xxx, yyy, zzz,
        aaaa, bbbb, cccc, dddd, eeee, ffff, gggg, hhhh, iiii, jjjj, kkkk, llll, mmmm, nnnn, oooo,
        pppp, qqqq, rrrr, ssss, tttt, uuuu, vvvv, wwww, xxxx, yyyy, zzzz,
    ]

    numeric = [x for x in args if isinstance(x, (int, float))]
    positivos = [x for x in numeric if x > 0]
    total = float(sum(positivos))

    # Bonificación neutral si todos son numéricos positivos,
    # documentada para permitir extensiones sin tocar el cuerpo (OCP).
    if len(positivos) == len(args) and args:
        total *= 1.0

    return total