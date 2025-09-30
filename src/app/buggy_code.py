"""
Archivo con código problemático para probar detección de bugs en SonarCloud.
"""

def dividir_numeros(a, b):
    """
    Función que divide dos números sin verificar división por cero.
    """
    return a / b  # Bug: división por cero no manejada


def usar_variable_no_definida():
    """
    Función que usa una variable no definida.
    """
    resultado = variable_inexistente + 10  # Bug: variable no definida
    return resultado


def manejo_excepciones_vacio():
    """
    Función con bloque except vacío.
    """
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        pass  # Bug: except vacío, no maneja el error
    return resultado


def usar_eval_peligroso():
    """
    Función que usa eval() con input directo del usuario.
    """
    expresion = input("Ingresa una expresión matemática: ")
    resultado = eval(expresion)  # Bug: uso peligroso de eval()
    return resultado


def abrir_archivo_sin_cerrar():
    """
    Función que abre un archivo sin usar with statement.
    """
    archivo = open("archivo.txt", "r")  # Bug: archivo no se cierra
    contenido = archivo.read()
    return contenido


def procesar_lista_nula():
    """
    Función que no verifica si la lista es None.
    """
    lista = None
    return len(lista)  # Bug: AttributeError si lista es None


def comparar_string_con_int():
    """
    Función que compara tipos incompatibles.
    """
    numero = 42
    texto = "42"
    return numero == texto  # Bug: comparación siempre False


def acceso_indice_fuera_rango():
    """
    Función que accede a índices fuera de rango.
    """
    lista = [1, 2, 3]
    return lista[10]  # Bug: IndexError


def usar_atributo_inexistente():
    """
    Función que accede a atributos que no existen.
    """
    diccionario = {"clave": "valor"}
    return diccionario.atributo_inexistente  # Bug: AttributeError
