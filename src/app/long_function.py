"""
Archivo con funciones muy largas y problemas de mantenibilidad.
"""

def procesar_datos_complejos(datos):
    """
    Función muy larga con lógica repetitiva y condiciones innecesarias.
    Esta función debería ser refactorizada en funciones más pequeñas.
    """
    # Comentario redundante: inicializar variables
    resultado = []
    suma_total = 0
    contador = 0
    promedio = 0
    maximo = 0
    minimo = 0
    # Comentario redundante: procesar cada elemento
    for elemento in datos:
        # Comentario redundante: verificar si es número
        if isinstance(elemento, (int, float)):
            # Comentario redundante: agregar a resultado
            resultado.append(elemento)
            # Comentario redundante: sumar
            suma_total += elemento
            # Comentario redundante: incrementar contador
            contador += 1
            # Comentario redundante: calcular máximo
            if elemento > maximo:
                maximo = elemento
            # Comentario redundante: calcular mínimo
            if contador == 1:
                minimo = elemento
            elif elemento < minimo:
                minimo = elemento
        # Comentario redundante: verificar si es string
        elif isinstance(elemento, str):
            # Comentario redundante: convertir a número si es posible
            try:
                numero = float(elemento)
                resultado.append(numero)
                suma_total += numero
                contador += 1
                if numero > maximo:
                    maximo = numero
                if contador == 1:
                    minimo = numero
                elif numero < minimo:
                    minimo = numero
            except ValueError:
                # Comentario redundante: ignorar si no se puede convertir
                pass
        # Comentario redundante: verificar si es lista
        elif isinstance(elemento, list):
            # Comentario redundante: procesar lista recursivamente
            for sub_elemento in elemento:
                if isinstance(sub_elemento, (int, float)):
                    resultado.append(sub_elemento)
                    suma_total += sub_elemento
                    contador += 1
                    if sub_elemento > maximo:
                        maximo = sub_elemento
                    if contador == 1:
                        minimo = sub_elemento
                    elif sub_elemento < minimo:
                        minimo = sub_elemento
    # Comentario redundante: calcular promedio
    if contador > 0:
        promedio = suma_total / contador
    # Comentario redundante: retornar estadísticas
    return {
        "datos_procesados": resultado,
        "suma_total": suma_total,
        "contador": contador,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo
    }


def validar_formulario_usuario(nombre, email, edad, telefono, direccion, ciudad, pais, codigo_postal):
    """
    Función con demasiados parámetros y validaciones repetitivas.
    """
    errores = []
    
    # Validación redundante de nombre
    if nombre is None or nombre == "":
        errores.append("El nombre es requerido")
    elif len(nombre) < 2:
        errores.append("El nombre debe tener al menos 2 caracteres")
    elif len(nombre) > 50:
        errores.append("El nombre no puede tener más de 50 caracteres")
    elif not nombre.replace(" ", "").isalpha():
        errores.append("El nombre solo puede contener letras y espacios")
    
    # Validación redundante de email
    if email is None or email == "":
        errores.append("El email es requerido")
    elif "@" not in email:
        errores.append("El email debe contener @")
    elif "." not in email:
        errores.append("El email debe contener un punto")
    elif len(email) < 5:
        errores.append("El email debe tener al menos 5 caracteres")
    elif len(email) > 100:
        errores.append("El email no puede tener más de 100 caracteres")
    
    # Validación redundante de edad
    if edad is None:
        errores.append("La edad es requerida")
    elif not isinstance(edad, int):
        errores.append("La edad debe ser un número entero")
    elif edad < 0:
        errores.append("La edad no puede ser negativa")
    elif edad > 150:
        errores.append("La edad no puede ser mayor a 150")
    elif edad < 18:
        errores.append("Debe ser mayor de edad")
    
    # Validación redundante de teléfono
    if telefono is None or telefono == "":
        errores.append("El teléfono es requerido")
    elif not telefono.replace("+", "").replace("-", "").replace(" ", "").isdigit():
        errores.append("El teléfono solo puede contener números, +, - y espacios")
    elif len(telefono.replace("+", "").replace("-", "").replace(" ", "")) < 7:
        errores.append("El teléfono debe tener al menos 7 dígitos")
    elif len(telefono.replace("+", "").replace("-", "").replace(" ", "")) > 15:
        errores.append("El teléfono no puede tener más de 15 dígitos")
    
    # Validación redundante de dirección
    if direccion is None or direccion == "":
        errores.append("La dirección es requerida")
    elif len(direccion) < 5:
        errores.append("La dirección debe tener al menos 5 caracteres")
    elif len(direccion) > 200:
        errores.append("La dirección no puede tener más de 200 caracteres")
    
    # Validación redundante de ciudad
    if ciudad is None or ciudad == "":
        errores.append("La ciudad es requerida")
    elif len(ciudad) < 2:
        errores.append("La ciudad debe tener al menos 2 caracteres")
    elif len(ciudad) > 50:
        errores.append("La ciudad no puede tener más de 50 caracteres")
    elif not ciudad.replace(" ", "").isalpha():
        errores.append("La ciudad solo puede contener letras y espacios")
    
    # Validación redundante de país
    if pais is None or pais == "":
        errores.append("El país es requerido")
    elif len(pais) < 2:
        errores.append("El país debe tener al menos 2 caracteres")
    elif len(pais) > 50:
        errores.append("El país no puede tener más de 50 caracteres")
    elif not pais.replace(" ", "").isalpha():
        errores.append("El país solo puede contener letras y espacios")
    
    # Validación redundante de código postal
    if codigo_postal is None or codigo_postal == "":
        errores.append("El código postal es requerido")
    elif not codigo_postal.replace("-", "").isdigit():
        errores.append("El código postal solo puede contener números y guiones")
    elif len(codigo_postal.replace("-", "")) < 4:
        errores.append("El código postal debe tener al menos 4 dígitos")
    elif len(codigo_postal.replace("-", "")) > 10:
        errores.append("El código postal no puede tener más de 10 dígitos")
    
    return len(errores) == 0, errores


def funcion_con_muchos_parametros(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    """
    Función con demasiados parámetros (>7) - Code Smell detectado por SonarCloud.
    """
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t


def funcion_con_complejidad_ciclamatica():
    """
    Función con alta complejidad ciclomática - múltiples condiciones anidadas.
    """
    resultado = 0
    for i in range(10):
        if i % 2 == 0:
            if i % 3 == 0:
                if i % 5 == 0:
                    resultado += i * 2
                else:
                    resultado += i
            elif i % 4 == 0:
                if i > 5:
                    resultado += i * 3
                else:
                    resultado += i * 2
            else:
                resultado += i
        elif i % 3 == 0:
            if i % 7 == 0:
                resultado += i * 4
            else:
                resultado += i * 2
        else:
            if i > 7:
                resultado += i * 5
            elif i > 3:
                resultado += i * 3
            else:
                resultado += i
    return resultado


def funcion_con_muchas_variables_locales():
    """
    Función con demasiadas variables locales (>8) - Code Smell.
    """
    variable1 = 1
    variable2 = 2
    variable3 = 3
    variable4 = 4
    variable5 = 5
    variable6 = 6
    variable7 = 7
    variable8 = 8
    variable9 = 9
    variable10 = 10
    variable11 = 11
    variable12 = 12
    variable13 = 13
    variable14 = 14
    variable15 = 15
    variable16 = 16
    variable17 = 17
    variable18 = 18
    variable19 = 19
    variable20 = 20
    
    return variable1 + variable2 + variable3 + variable4 + variable5 + variable6 + variable7 + variable8 + variable9 + variable10 + variable11 + variable12 + variable13 + variable14 + variable15 + variable16 + variable17 + variable18 + variable19 + variable20


def funcion_con_muchos_return():
    """
    Función con demasiados return statements (>3) - Code Smell.
    """
    if True:
        return 1
    elif False:
        return 2
    elif True:
        return 3
    elif False:
        return 4
    elif True:
        return 5
    elif False:
        return 6
    elif True:
        return 7
    elif False:
        return 8
    elif True:
        return 9
    elif False:
        return 10
    else:
        return 11


def funcion_con_strings_magicos():
    """
    Función con strings mágicos hardcodeados - Code Smell.
    """
    if "admin" == "admin":
        return "success"
    elif "user" == "user":
        return "ok"
    elif "guest" == "guest":
        return "limited"
    elif "root" == "root":
        return "full_access"
    elif "superuser" == "superuser":
        return "all_permissions"
    else:
        return "denied"


def funcion_con_numeros_magicos():
    """
    Función con números mágicos hardcodeados - Code Smell.
    """
    if 100 > 50:
        return 200
    elif 300 < 400:
        return 500
    elif 600 == 600:
        return 700
    elif 800 != 900:
        return 1000
    elif 1100 >= 1200:
        return 1300
    else:
        return 1400


def funcion_con_duplicacion_interna():
    """
    Función con código duplicado internamente - Code Smell.
    """
    # Bloque duplicado 1
    resultado1 = 0
    for i in range(5):
        resultado1 += i * 2
    resultado1 = resultado1 * 3
    
    # Bloque duplicado 2 (idéntico al 1)
    resultado2 = 0
    for i in range(5):
        resultado2 += i * 2
    resultado2 = resultado2 * 3
    
    # Bloque duplicado 3 (idéntico al 1)
    resultado3 = 0
    for i in range(5):
        resultado3 += i * 2
    resultado3 = resultado3 * 3
    
    return resultado1 + resultado2 + resultado3


def funcion_con_comentarios_todos():
    """
    Función con comentarios TODO/FIXME - Code Smell.
    """
    # TODO: Implementar validación de entrada
    # FIXME: Corregir cálculo de impuestos
    # TODO: Agregar manejo de errores
    # FIXME: Optimizar algoritmo
    # TODO: Refactorizar código duplicado
    # FIXME: Actualizar documentación
    # TODO: Implementar tests unitarios
    # FIXME: Corregir bug en línea 42
    
    valor = 42
    return valor * 2


def funcion_con_imports_no_usados():
    """
    Función con imports no utilizados - Code Smell.
    """
    import os
    import sys
    import json
    import datetime
    import random
    import math
    import re
    import urllib.request
    
    # Solo usamos una variable simple
    resultado = 10
    return resultado


# Código comentado innecesario - Code Smell
# def funcion_eliminada():
#     return "Esta función ya no se usa"
# 
# def otra_funcion_eliminada():
#     return "Esta tampoco"
# 
# # Variables comentadas - Code Smell
# # variable_inutil = "no se usa"
# # otra_variable = 123
# 
# # Imports comentados - Code Smell
# # import os
# # import sys
# # from datetime import datetime
# 
# # Código muerto comentado - Code Smell
# # if True:
# #     print("Esto nunca se ejecutará")
# #     resultado = 42
# #     return resultado
