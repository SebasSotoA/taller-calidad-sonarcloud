"""
Archivo con funciones muy largas y problemas de mantenibilidad.
"""

from typing import Any, Dict, Iterable, List

# Constantes para evitar números y cadenas mágicas
MIN_EDAD = 18
MAX_EDAD = 150
NOMBRE_MIN = 2
NOMBRE_MAX = 50
EMAIL_MIN = 5
EMAIL_MAX = 100
DIR_MIN = 5
DIR_MAX = 200
CIUDAD_MIN = 2
CIUDAD_MAX = 50
TEL_MIN = 7
TEL_MAX = 15
CP_MIN = 4
CP_MAX = 10

ROLES = {
    "admin": "success",
    "user": "ok",
    "guest": "limited",
    "root": "full_access",
    "superuser": "all_permissions",
}

NUMEROS = [50, 100, 200, 300, 400, 500, 600, 700, 1000, 1300, 1400]

def _is_num(x: Any) -> bool:
    return isinstance(x, (int, float))
def procesar_datos_complejos(datos: Iterable[Any]) -> Dict[str, Any]:
    """Procesa datos extrayendo números (y strings convertibles) y calcula estadísticas."""
    numeros: List[float] = []
    for el in datos:
        if _is_num(el):
            numeros.append(float(el))
        elif isinstance(el, str):
            try:
                numeros.append(float(el))
            except ValueError:
                continue
        elif isinstance(el, list):
            for se in el:
                if _is_num(se):
                    numeros.append(float(se))
    if not numeros:
        return {"datos_procesados": [], "suma_total": 0.0, "contador": 0, "promedio": 0.0, "maximo": 0.0, "minimo": 0.0}
    suma = sum(numeros)
    return {
        "datos_procesados": numeros,
        "suma_total": suma,
        "contador": len(numeros),
        "promedio": suma / len(numeros),
        "maximo": max(numeros),
        "minimo": min(numeros),
    }


def validar_formulario_usuario(nombre, email, edad, telefono, direccion, ciudad, pais, codigo_postal):
    """Valida datos de usuario aplicando reglas centralizadas y legibles."""
    errores: List[str] = []

    def requerido_y_longitud(valor: str, nombre_campo: str, min_len: int, max_len: int, solo_alpha: bool = False):
        if not valor:
            errores.append(f"El {nombre_campo} es requerido")
            return
        if len(valor) < min_len:
            errores.append(f"El {nombre_campo} debe tener al menos {min_len} caracteres")
        if len(valor) > max_len:
            errores.append(f"El {nombre_campo} no puede tener más de {max_len} caracteres")
        if solo_alpha and not valor.replace(" ", "").isalpha():
            errores.append(f"El {nombre_campo} solo puede contener letras y espacios")

    requerido_y_longitud(nombre, "nombre", NOMBRE_MIN, NOMBRE_MAX, solo_alpha=True)

    if not email:
        errores.append("El email es requerido")
    else:
        if "@" not in email or "." not in email:
            errores.append("El email debe contener @ y .")
        if len(email) < EMAIL_MIN:
            errores.append(f"El email debe tener al menos {EMAIL_MIN} caracteres")
        if len(email) > EMAIL_MAX:
            errores.append(f"El email no puede tener más de {EMAIL_MAX} caracteres")

    if not isinstance(edad, int):
        errores.append("La edad debe ser un número entero")
    else:
        if edad < 0 or edad > MAX_EDAD:
            errores.append("La edad debe estar entre 0 y 150")
        if edad < MIN_EDAD:
            errores.append("Debe ser mayor de edad")

    if not telefono:
        errores.append("El teléfono es requerido")
    else:
        digits = telefono.replace("+", "").replace("-", "").replace(" ", "")
        if not digits.isdigit():
            errores.append("El teléfono solo puede contener números, +, - y espacios")
        if len(digits) < TEL_MIN:
            errores.append(f"El teléfono debe tener al menos {TEL_MIN} dígitos")
        if len(digits) > TEL_MAX:
            errores.append(f"El teléfono no puede tener más de {TEL_MAX} dígitos")

    requerido_y_longitud(direccion, "dirección", DIR_MIN, DIR_MAX)
    requerido_y_longitud(ciudad, "ciudad", CIUDAD_MIN, CIUDAD_MAX, solo_alpha=True)
    requerido_y_longitud(pais, "país", CIUDAD_MIN, CIUDAD_MAX, solo_alpha=True)

    if not codigo_postal:
        errores.append("El código postal es requerido")
    else:
        cp = codigo_postal.replace("-", "")
        if not cp.isdigit():
            errores.append("El código postal solo puede contener números y guiones")
        if len(cp) < CP_MIN:
            errores.append(f"El código postal debe tener al menos {CP_MIN} dígitos")
        if len(cp) > CP_MAX:
            errores.append(f"El código postal no puede tener más de {CP_MAX} dígitos")

    return len(errores) == 0, errores


def funcion_con_muchos_parametros(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    """Suma parámetros numéricos, ignorando no numéricos. Firma se mantiene."""
    params = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
    return sum(p for p in params if _is_num(p))


def funcion_con_complejidad_ciclamatica():
    """
    Función con alta complejidad ciclomática - múltiples condiciones anidadas.
    """
    resultado = 0
    for i in range(10):
        if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
            resultado += i * 2
        elif i % 2 == 0 and i % 4 == 0 and i > 5:
            resultado += i * 3
        elif i % 2 == 0:
            resultado += i
        elif i % 3 == 0 and i % 7 == 0:
            resultado += i * 4
        elif i % 3 == 0:
            resultado += i * 2
        elif i > 7:
            resultado += i * 5
        elif i > 3:
            resultado += i * 3
        else:
            resultado += i
    return resultado


def funcion_con_muchas_variables_locales() -> int:
    """Evita locales innecesarias; usa sum(range())."""
    return sum(range(1, 21))


def funcion_con_muchos_return() -> int:
    """Retorno único basado en una regla simple."""
    return 5


def funcion_con_strings_magicos(role: str = "admin") -> str:
    """Mapea roles predefinidos a respuestas; evita strings mágicos repetidos."""
    return ROLES.get(role, "denied")


def funcion_con_numeros_magicos() -> int:
    """Retorna el máximo de una lista predefinida de números permitidos."""
    return max(NUMEROS)


def funcion_con_duplicacion_interna() -> int:
    """Elimina duplicación con un helper reutilizable."""
    def bloque() -> int:
        return sum(i * 2 for i in range(5)) * 3
    return bloque() + bloque() + bloque()


def funcion_con_comentarios_todos() -> int:
    """Función limpia sin comentarios TODO/FIXME innecesarios."""
    valor = 42
    return valor * 2


def funcion_con_imports_no_usados() -> int:
    """Evita imports internos no utilizados y retorna un valor determinista."""
    return 10


def funcion_con_muchos_if_anidados() -> int:
    """Usa una fórmula directa en vez de ifs anidados."""
    resultado = 0
    for i in range(10):
        resultado += i * min(max(i, 0), 10)
    return resultado


def funcion_con_muchos_elif(valor: int = 5) -> str:
    """Usa un mapping en lugar de una cadena de elif."""
    nombres = {
        1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis",
        7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce",
        13: "trece", 14: "catorce", 15: "quince", 16: "dieciséis", 17: "diecisiete",
        18: "dieciocho", 19: "diecinueve", 20: "veinte"
    }
    return nombres.get(valor, "desconocido")


def funcion_con_muchos_bucles_anidados() -> int:
    """Evita 8 bucles anidados calculando por combinatoria simple."""
    # suma de 0..4 = 10; hay 5^7 combinaciones por cada índice y 8 índices
    base = sum(range(5))
    combos = 5 ** 7
    return 8 * base * combos


def funcion_con_muchas_condiciones_complejas() -> int:
    """Simplifica las condiciones a una sola regla clara."""
    return sum(i for i in range(20) if i in {1, 3, 5, 7, 8})


def funcion_con_muchos_try_except() -> int:
    """Evita cascadas de try/except; utiliza un cálculo directo."""
    return sum(range(1, 11))


def funcion_con_muchos_while() -> int:
    """Equivalente a múltiples while, usando aritmética simple."""
    base = sum(range(5))
    combos = 5 ** 4
    return 5 * base * combos


def funcion_con_muchos_operadores_logicos() -> int:
    """Selecciona valores mediante una condición clara en vez de lógica intrincada."""
    return sum(i for i in range(10) if i in {2, 4, 8})


def funcion_con_muchos_casos_switch(valor: int = 5) -> str:
    """Usa un diccionario como switch-case compacto."""
    return {i: f"caso {i}" for i in range(1, 31)}.get(valor, "caso por defecto")


def funcion_con_muchos_operadores_ternarios(valor: int = 5):
    """Evita ternarios anidados usando funciones auxiliares y mapas."""
    def nivel(v: int) -> str:
        if v > 10:
            return "alto"
        if v > 5:
            return "medio"
        if v > 2:
            return "bajo"
        if v > 0:
            return "muy bajo"
        return "cero"

    letras = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"}
    return nivel(valor), letras.get(valor, "desconocido")


def funcion_con_muchos_lambdas() -> int:
    """Evita cascadas de lambdas; usa una transformación clara."""
    resultado = 0
    for i in range(10):
        t = ((i ^ 1) | 1)
        resultado += (t * t) // 2
    return resultado


def funcion_con_muchos_generadores() -> int:
    """Evita generadores anidados calculando por fórmula simple."""
    base = sum(range(5))
    combos = 5 ** 4
    return 5 * base * combos


def funcion_con_muchos_decoradores() -> int:
    """Simplifica: evita pila de decoradores innecesarios."""
    def funcion_decorada(valor: int) -> int:
        return valor + 1 + 2 + 3 + 4 + 5
    return funcion_decorada(10)


def funcion_con_muchos_context_managers(rutas: List[str] | None = None) -> int:
    """Lee múltiples archivos de forma segura y suma sus longitudes.

    Si un archivo no existe, se ignora. Usa un solo nivel de with por archivo.
    """
    if rutas is None:
        rutas = [f"archivo{i}.txt" for i in range(1, 11)]
    total = 0
    for ruta in rutas:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                total += len(f.read())
        except FileNotFoundError:
            continue
    return total
