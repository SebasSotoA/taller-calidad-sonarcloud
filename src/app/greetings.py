def saludar_es(nombre: str) -> str:
    # Duplicación intencional: lógica idéntica a saludar_en
    saludo = f"Hola, {nombre}!"
    # Variable no usada (New Issue)
    variable_sin_uso = 42
    return saludo


def saludar_en(nombre: str) -> str:
    # Duplicación intencional: lógica idéntica a saludar_es
    saludo = f"Hello, {nombre}!"
    return saludo

