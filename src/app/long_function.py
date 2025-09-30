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


def funcion_con_muchos_if_anidados():
    """
    Función con demasiados if anidados - aumenta complejidad ciclomática.
    """
    resultado = 0
    for i in range(10):
        if i > 0:
            if i > 1:
                if i > 2:
                    if i > 3:
                        if i > 4:
                            if i > 5:
                                if i > 6:
                                    if i > 7:
                                        if i > 8:
                                            if i > 9:
                                                resultado += i * 10
                                            else:
                                                resultado += i * 9
                                        else:
                                            resultado += i * 8
                                    else:
                                        resultado += i * 7
                                else:
                                    resultado += i * 6
                            else:
                                resultado += i * 5
                        else:
                            resultado += i * 4
                    else:
                        resultado += i * 3
                else:
                    resultado += i * 2
            else:
                resultado += i * 1
        else:
            resultado += 0
    return resultado


def funcion_con_muchos_elif():
    """
    Función con demasiados elif - aumenta complejidad ciclomática.
    """
    valor = 5
    if valor == 1:
        return "uno"
    elif valor == 2:
        return "dos"
    elif valor == 3:
        return "tres"
    elif valor == 4:
        return "cuatro"
    elif valor == 5:
        return "cinco"
    elif valor == 6:
        return "seis"
    elif valor == 7:
        return "siete"
    elif valor == 8:
        return "ocho"
    elif valor == 9:
        return "nueve"
    elif valor == 10:
        return "diez"
    elif valor == 11:
        return "once"
    elif valor == 12:
        return "doce"
    elif valor == 13:
        return "trece"
    elif valor == 14:
        return "catorce"
    elif valor == 15:
        return "quince"
    elif valor == 16:
        return "dieciséis"
    elif valor == 17:
        return "diecisiete"
    elif valor == 18:
        return "dieciocho"
    elif valor == 19:
        return "diecinueve"
    elif valor == 20:
        return "veinte"
    else:
        return "desconocido"


def funcion_con_muchos_bucles_anidados():
    """
    Función con múltiples bucles anidados - aumenta complejidad.
    """
    resultado = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        for n in range(5):
                            for o in range(5):
                                for p in range(5):
                                    resultado += i + j + k + l + m + n + o + p
    return resultado


def funcion_con_muchas_condiciones_complejas():
    """
    Función con condiciones muy complejas - aumenta complejidad ciclomática.
    """
    resultado = 0
    for i in range(20):
        if (i > 0 and i < 10) or (i > 15 and i < 20):
            if i % 2 == 0 and i % 3 == 0:
                if i > 5 or i < 8:
                    if i != 6 and i != 9:
                        if i in [1, 2, 3, 4, 5, 7, 8]:
                            if i not in [2, 4]:
                                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8:
                                    if i == 1:
                                        resultado += 1
                                    elif i == 3:
                                        resultado += 3
                                    elif i == 5:
                                        resultado += 5
                                    elif i == 7:
                                        resultado += 7
                                    elif i == 8:
                                        resultado += 8
    return resultado


def funcion_con_muchos_try_except():
    """
    Función con múltiples bloques try-except - aumenta complejidad.
    """
    resultado = 0
    try:
        resultado += 1
        try:
            resultado += 2
            try:
                resultado += 3
                try:
                    resultado += 4
                    try:
                        resultado += 5
                        try:
                            resultado += 6
                            try:
                                resultado += 7
                                try:
                                    resultado += 8
                                    try:
                                        resultado += 9
                                        try:
                                            resultado += 10
                                        except:
                                            resultado += 11
                                    except:
                                        resultado += 12
                                except:
                                    resultado += 13
                            except:
                                resultado += 14
                        except:
                            resultado += 15
                    except:
                        resultado += 16
                except:
                    resultado += 17
            except:
                resultado += 18
        except:
            resultado += 19
    except:
        resultado += 20
    return resultado


def funcion_con_muchos_while():
    """
    Función con múltiples bucles while - aumenta complejidad.
    """
    resultado = 0
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            k = 0
            while k < 5:
                l = 0
                while l < 5:
                    m = 0
                    while m < 5:
                        resultado += i + j + k + l + m
                        m += 1
                    l += 1
                k += 1
            j += 1
        i += 1
    return resultado


def funcion_con_muchos_operadores_logicos():
    """
    Función con operadores lógicos complejos - aumenta complejidad.
    """
    resultado = 0
    for i in range(10):
        if (i > 0 and i < 5) or (i > 7 and i < 10):
            if i % 2 == 0 and i % 3 != 0:
                if i == 2 or i == 4 or i == 8:
                    if i != 1 and i != 3 and i != 5 and i != 7 and i != 9:
                        if i in [2, 4, 8] and i not in [1, 3, 5, 6, 7, 9]:
                            if (i == 2 and i > 1) or (i == 4 and i > 3) or (i == 8 and i > 7):
                                if not (i == 1 or i == 3 or i == 5 or i == 6 or i == 7 or i == 9):
                                    resultado += i
    return resultado


def funcion_con_muchos_casos_switch():
    """
    Función que simula un switch con muchos casos - aumenta complejidad.
    """
    valor = 5
    if valor == 1:
        return "caso 1"
    elif valor == 2:
        return "caso 2"
    elif valor == 3:
        return "caso 3"
    elif valor == 4:
        return "caso 4"
    elif valor == 5:
        return "caso 5"
    elif valor == 6:
        return "caso 6"
    elif valor == 7:
        return "caso 7"
    elif valor == 8:
        return "caso 8"
    elif valor == 9:
        return "caso 9"
    elif valor == 10:
        return "caso 10"
    elif valor == 11:
        return "caso 11"
    elif valor == 12:
        return "caso 12"
    elif valor == 13:
        return "caso 13"
    elif valor == 14:
        return "caso 14"
    elif valor == 15:
        return "caso 15"
    elif valor == 16:
        return "caso 16"
    elif valor == 17:
        return "caso 17"
    elif valor == 18:
        return "caso 18"
    elif valor == 19:
        return "caso 19"
    elif valor == 20:
        return "caso 20"
    elif valor == 21:
        return "caso 21"
    elif valor == 22:
        return "caso 22"
    elif valor == 23:
        return "caso 23"
    elif valor == 24:
        return "caso 24"
    elif valor == 25:
        return "caso 25"
    elif valor == 26:
        return "caso 26"
    elif valor == 27:
        return "caso 27"
    elif valor == 28:
        return "caso 28"
    elif valor == 29:
        return "caso 29"
    elif valor == 30:
        return "caso 30"
    else:
        return "caso por defecto"


def funcion_con_muchos_operadores_ternarios():
    """
    Función con operadores ternarios anidados - aumenta complejidad.
    """
    valor = 5
    resultado = "alto" if valor > 10 else ("medio" if valor > 5 else ("bajo" if valor > 2 else ("muy bajo" if valor > 0 else "cero")))
    
    resultado2 = "A" if valor == 1 else ("B" if valor == 2 else ("C" if valor == 3 else ("D" if valor == 4 else ("E" if valor == 5 else ("F" if valor == 6 else ("G" if valor == 7 else ("H" if valor == 8 else ("I" if valor == 9 else ("J" if valor == 10 else "desconocido")))))))))
    
    return resultado, resultado2


def funcion_con_muchos_lambdas():
    """
    Función con múltiples lambdas - aumenta complejidad.
    """
    lambda1 = lambda x: x * 2
    lambda2 = lambda x: x + 1
    lambda3 = lambda x: x - 1
    lambda4 = lambda x: x / 2
    lambda5 = lambda x: x ** 2
    lambda6 = lambda x: x % 2
    lambda7 = lambda x: x // 2
    lambda8 = lambda x: x & 1
    lambda9 = lambda x: x | 1
    lambda10 = lambda x: x ^ 1
    
    resultado = 0
    for i in range(10):
        resultado += lambda1(lambda2(lambda3(lambda4(lambda5(lambda6(lambda7(lambda8(lambda9(lambda10(i))))))))))
    
    return resultado


def funcion_con_muchos_generadores():
    """
    Función con múltiples generadores anidados - aumenta complejidad.
    """
    resultado = 0
    for i in (x for x in range(5)):
        for j in (y for y in range(5)):
            for k in (z for z in range(5)):
                for l in (w for w in range(5)):
                    for m in (v for v in range(5)):
                        resultado += i + j + k + l + m
    return resultado


def funcion_con_muchos_decoradores():
    """
    Función con múltiples decoradores - aumenta complejidad.
    """
    def decorador1(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + 1
        return wrapper
    
    def decorador2(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + 2
        return wrapper
    
    def decorador3(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + 3
        return wrapper
    
    def decorador4(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + 4
        return wrapper
    
    def decorador5(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + 5
        return wrapper
    
    @decorador1
    @decorador2
    @decorador3
    @decorador4
    @decorador5
    def funcion_decorada(valor):
        return valor
    
    return funcion_decorada(10)


def funcion_con_muchos_context_managers():
    """
    Función con múltiples context managers - aumenta complejidad.
    """
    resultado = 0
    with open("archivo1.txt", "r") as f1:
        with open("archivo2.txt", "r") as f2:
            with open("archivo3.txt", "r") as f3:
                with open("archivo4.txt", "r") as f4:
                    with open("archivo5.txt", "r") as f5:
                        with open("archivo6.txt", "r") as f6:
                            with open("archivo7.txt", "r") as f7:
                                with open("archivo8.txt", "r") as f8:
                                    with open("archivo9.txt", "r") as f9:
                                        with open("archivo10.txt", "r") as f10:
                                            resultado += len(f1.read()) + len(f2.read()) + len(f3.read()) + len(f4.read()) + len(f5.read()) + len(f6.read()) + len(f7.read()) + len(f8.read()) + len(f9.read()) + len(f10.read())
    return resultado
