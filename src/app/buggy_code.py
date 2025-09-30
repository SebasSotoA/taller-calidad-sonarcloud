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


def comparaciones_tipos_incompatibles():
    """
    Múltiples comparaciones entre tipos incompatibles que siempre retornan False.
    """
    # Bug: Comparación int con string - siempre False
    numero = 42
    texto = "42"
    resultado1 = numero == texto  # S2159: Incompatible types comparison
    
    # Bug: Comparación float con string - siempre False
    decimal = 3.14
    texto_decimal = "3.14"
    resultado2 = decimal == texto_decimal  # S2159: Incompatible types comparison
    
    # Bug: Comparación bool con int - siempre False
    booleano = True
    entero = 1
    resultado3 = booleano == entero  # S2159: Incompatible types comparison
    
    # Bug: Comparación list con string - siempre False
    lista = [1, 2, 3]
    texto_lista = "[1, 2, 3]"
    resultado4 = lista == texto_lista  # S2159: Incompatible types comparison
    
    # Bug: Comparación dict con string - siempre False
    diccionario = {"a": 1}
    texto_dict = '{"a": 1}'
    resultado5 = diccionario == texto_dict  # S2159: Incompatible types comparison
    
    return resultado1, resultado2, resultado3, resultado4, resultado5


def comparaciones_imposibles():
    """
    Comparaciones que siempre evalúan al mismo resultado.
    """
    # Bug: Comparación que siempre es True
    if True == True:  # S2159: Always True comparison
        resultado1 = "siempre verdadero"
    
    # Bug: Comparación que siempre es False
    if False == True:  # S2159: Always False comparison
        resultado2 = "nunca se ejecuta"
    else:
        resultado2 = "siempre se ejecuta"
    
    # Bug: Comparación de None con string - siempre False
    valor_none = None
    texto = "None"
    resultado3 = valor_none == texto  # S2159: Incompatible types comparison
    
    # Bug: Comparación de tipos diferentes
    lista_vacia = []
    diccionario_vacio = {}
    resultado4 = lista_vacia == diccionario_vacio  # S2159: Incompatible types comparison
    
    return resultado1, resultado2, resultado3, resultado4


def operaciones_imposibles():
    """
    Operaciones que siempre fallan o dan resultados incorrectos.
    """
    # Bug: División por cero
    resultado1 = 10 / 0  # S3519: Division by zero
    
    # Bug: Módulo por cero
    resultado2 = 10 % 0  # S3519: Division by zero
    
    # Bug: Acceso a índice inexistente
    lista = [1, 2, 3]
    resultado3 = lista[100]  # S3519: Index out of bounds
    
    # Bug: Acceso a clave inexistente sin verificar
    diccionario = {"a": 1}
    resultado4 = diccionario["b"]  # S3519: Key not found
    
    return resultado1, resultado2, resultado3, resultado4


def uso_recursos_no_cerrados():
    """
    Uso de recursos sin cerrarlos adecuadamente.
    """
    # Bug: Archivo abierto sin cerrar
    archivo1 = open("archivo1.txt", "r")
    contenido1 = archivo1.read()
    # No se cierra el archivo
    
    # Bug: Múltiples archivos abiertos sin cerrar
    archivo2 = open("archivo2.txt", "w")
    archivo2.write("contenido")
    # No se cierran los archivos
    
    archivo3 = open("archivo3.txt", "a")
    archivo3.write("más contenido")
    # No se cierra el archivo
    
    return contenido1


def variables_no_inicializadas():
    """
    Uso de variables que pueden no estar inicializadas.
    """
    # Bug: Variable condicionalmente inicializada
    if True:  # Esta condición podría ser False
        variable = 42
    
    # Bug: Acceso a variable que podría no existir
    resultado = variable + 10  # S3519: Variable might not be initialized
    
    # Bug: Variable en bucle que podría no ejecutarse
    for i in range(0):  # Bucle vacío
        variable_bucle = i
    
    # Bug: Acceso a variable del bucle que no se ejecutó
    resultado_bucle = variable_bucle * 2  # S3519: Variable might not be initialized
    
    return resultado, resultado_bucle


def excepciones_no_manejadas():
    """
    Excepciones que no se manejan adecuadamente.
    """
    # Bug: Except vacío
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        pass  # S1186: Empty except block
    
    # Bug: Except demasiado genérico
    try:
        resultado = int("no es un número")
    except:  # S1186: Bare except clause
        pass
    
    # Bug: Except que no maneja el error específico
    try:
        lista = [1, 2, 3]
        resultado = lista[10]
    except ValueError:  # S1186: Wrong exception type
        pass
    
    return resultado


def comparaciones_strings_peligrosas():
    """
    Comparaciones de strings que pueden ser problemáticas.
    """
    # Bug: Comparación con string vacío usando ==
    texto = ""
    if texto == "":  # S2159: Use 'not' instead of '== ""'
        resultado1 = "string vacío"
    
    # Bug: Comparación con None usando ==
    valor = None
    if valor == None:  # S2159: Use 'is None' instead of '== None'
        resultado2 = "valor es None"
    
    # Bug: Comparación de tipos diferentes
    numero_str = "123"
    numero_int = 123
    if numero_str == numero_int:  # S2159: Incompatible types comparison
        resultado3 = "iguales"
    else:
        resultado3 = "diferentes"
    
    return resultado1, resultado2, resultado3


def operaciones_lista_peligrosas():
    """
    Operaciones con listas que pueden fallar.
    """
    # Bug: Acceso a índice negativo
    lista = [1, 2, 3]
    resultado1 = lista[-10]  # S3519: Index out of bounds
    
    # Bug: Acceso a índice de lista vacía
    lista_vacia = []
    resultado2 = lista_vacia[0]  # S3519: Index out of bounds
    
    # Bug: Pop de lista vacía
    lista_vacia2 = []
    resultado3 = lista_vacia2.pop()  # S3519: Pop from empty list
    
    # Bug: Acceso a atributo de lista como si fuera objeto
    lista_obj = [1, 2, 3]
    resultado4 = lista_obj.atributo_inexistente  # S3519: AttributeError
    
    return resultado1, resultado2, resultado3, resultado4
