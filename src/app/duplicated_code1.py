"""
Archivo con código que será duplicado en otro archivo para probar detección de duplicación.
"""

def calcular_estadisticas_numericas(lista_numeros):
    """
    Función que calcula estadísticas básicas de una lista de números.
    Esta función será duplicada en duplicated_code2.py
    """
    if not lista_numeros:
        return None
    
    suma_total = 0
    contador = 0
    maximo = float('-inf')
    minimo = float('inf')
    
    for numero in lista_numeros:
        if isinstance(numero, (int, float)):
            suma_total += numero
            contador += 1
            if numero > maximo:
                maximo = numero
            if numero < minimo:
                minimo = numero
    
    promedio = suma_total / contador if contador > 0 else 0
    
    return {
        "suma": suma_total,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "contador": contador
    }


def procesar_archivo_csv(nombre_archivo):
    """
    Función que procesa un archivo CSV y extrae datos numéricos.
    Esta función también será duplicada.
    """
    datos_numericos = []
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                columnas = linea.strip().split(',')
                
                for columna in columnas:
                    try:
                        numero = float(columna)
                        datos_numericos.append(numero)
                    except ValueError:
                        continue
                        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []
    
    return datos_numericos


def validar_datos_entrada(datos):
    """
    Función de validación que será duplicada.
    """
    errores = []
    
    if datos is None:
        errores.append("Los datos no pueden ser None")
        return False, errores
    
    if not isinstance(datos, list):
        errores.append("Los datos deben ser una lista")
        return False, errores
    
    if len(datos) == 0:
        errores.append("La lista no puede estar vacía")
        return False, errores
    
    for i, dato in enumerate(datos):
        if not isinstance(dato, (int, float)):
            errores.append(f"El elemento en posición {i} no es un número")
    
    return len(errores) == 0, errores


def convertir_temperaturas(temperaturas_celsius):
    """
    Función que convierte temperaturas de Celsius a Fahrenheit.
    """
    temperaturas_fahrenheit = []
    
    for temp_c in temperaturas_celsius:
        if isinstance(temp_c, (int, float)):
            temp_f = (temp_c * 9/5) + 32
            temperaturas_fahrenheit.append(temp_f)
    
    return temperaturas_fahrenheit


def buscar_elemento_en_lista(lista, elemento):
    """
    Función de búsqueda que será duplicada.
    """
    if not lista:
        return -1
    
    for i, item in enumerate(lista):
        if item == elemento:
            return i
    
    return -1
