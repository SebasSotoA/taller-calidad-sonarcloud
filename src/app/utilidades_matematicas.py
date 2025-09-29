def division_riesgosa(a, b):
    # --- Reliability: sin validación de cero
    return a / b

def funcion_grande(datos):
    # --- Maintainability: demasiada lógica repetida en un solo método
    resultado = 0
    for i in range(len(datos)):
        resultado += datos[i] * 2
    for i in range(len(datos)):
        resultado -= datos[i] / 2
    for i in range(len(datos)):
        resultado += datos[i] ** 2
    for i in range(len(datos)):
        resultado -= datos[i] ** 0.5
    for i in range(len(datos)):
        resultado += (datos[i] * 3) - (datos[i] // 2)
    return resultado
