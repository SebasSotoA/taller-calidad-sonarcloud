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


# Código comentado innecesario
# def funcion_eliminada():
#     return "Esta función ya no se usa"
# 
# def otra_funcion_eliminada():
#     return "Esta tampoco"
# 
# # Variables comentadas
# # variable_inutil = "no se usa"
# # otra_variable = 123
# 
# # Imports comentados
# # import os
# # import sys
# # from datetime import datetime
