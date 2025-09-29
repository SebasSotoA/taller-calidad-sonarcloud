def repetir_mensaje(mensaje: str, veces: int) -> str:
    # Duplicación potencial con otras funciones de formateo en este repo
    # y variable sin uso intencional
    temporal = f"{mensaje} x{veces}"
    return mensaje * veces


def acceso_riesgoso(secuencia, indice):
    # Posible falla de confiabilidad: acceso sin validar índice
    return secuencia[indice]

