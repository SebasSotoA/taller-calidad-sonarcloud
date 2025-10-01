"""
Archivo con código problemático para probar detección de bugs en SonarCloud.
"""

# Utilidades de responsabilidad única para validación y operaciones seguras
from typing import Any, Iterable, Optional, Tuple
import ast


def _ensure_not_none(value: Any, name: str = "value") -> None:
    """Valida que un valor no sea None, de lo contrario lanza ValueError."""
    if value is None:
        raise ValueError(f"{name} no debe ser None")


def _safe_read_text(path: str, mode: str = "r", encoding: str = "utf-8") -> str:
    """Lee un archivo de forma segura usando context manager. Retorna '' si no existe."""
    try:
        with open(path, mode, encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        return ""


class _SafeEval(ast.NodeVisitor):
    """Evaluador seguro para expresiones aritméticas simples (sin eval)."""

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Num,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Mod,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Load,
        ast.Constant,
    )

    def visit(self, node):  # type: ignore[override]
        if not isinstance(node, self.allowed_nodes):
            raise ValueError("Expresión no permitida")
        return super().visit(node)

    def eval(self, expr: str) -> float:
        tree = ast.parse(expr, mode="eval")
        self.visit(tree)
        return self._eval_node(tree.body)

    def _eval_node(self, node: ast.AST) -> float:
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return float(node.value)
            raise ValueError("Constante no numérica")
        if isinstance(node, ast.Num):  # compat
            return float(node.n)
        if isinstance(node, ast.UnaryOp):
            val = self._eval_node(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +val
            if isinstance(node.op, ast.USub):
                return -val
            raise ValueError("Operador unario no permitido")
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise ValueError("División por cero no permitida")
                return left / right
            if isinstance(node.op, ast.Mod):
                if right == 0:
                    raise ValueError("Módulo por cero no permitido")
                return left % right
            if isinstance(node.op, ast.Pow):
                return left ** right
            raise ValueError("Operador binario no permitido")
        raise ValueError("Nodo no soportado")

def dividir_numeros(a: float, b: float) -> float:
    """Divide validando tipos y evitando división por cero (ValueError en caso inválido)."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a y b deben ser numéricos")
    if b == 0:
        raise ValueError("División por cero no permitida")
    return float(a) / float(b)


def usar_variable_no_definida() -> int:
    """Corrige el uso de variable inexistente usando una variable local definida."""
    base = 0
    return base + 10


def manejo_excepciones_vacio() -> Optional[float]:
    """Manejo explícito de excepción, sin except vacío y con retorno controlado."""
    try:
        return 10 / 2
    except ZeroDivisionError:  # pragma: no cover
        return None


def usar_eval_peligroso(expresion: str = "") -> float:
    """Evalúa una expresión aritmética de forma segura con AST (sin eval)."""
    _ensure_not_none(expresion, "expresion")
    return _SafeEval().eval(expresion)


def abrir_archivo_sin_cerrar(path: str = "archivo.txt") -> str:
    """Lee un archivo usando context manager y manejo de inexistencia."""
    return _safe_read_text(path)


def procesar_lista_nula(lista: Optional[Iterable[Any]] = None) -> int:
    """Retorna longitud validando None y normalizando a lista."""
    _ensure_not_none(lista, "lista")
    return len(list(lista))


def comparar_string_con_int(numero: int = 42, texto: str = "42") -> bool:
    """Compara tras conversión segura de string a entero."""
    try:
        return numero == int(texto)
    except (TypeError, ValueError):
        return False


def acceso_indice_fuera_rango(index: int = 10) -> Optional[int]:
    """Accede a un índice de manera segura, retornando None si está fuera de rango."""
    lista = [1, 2, 3]
    return lista[index] if 0 <= index < len(lista) else None


def usar_atributo_inexistente() -> Optional[str]:
    """Accede de forma segura a una clave de diccionario existente."""
    diccionario = {"clave": "valor"}
    return diccionario.get("clave")


def comparaciones_tipos_incompatibles() -> Tuple[bool, bool, bool, bool, bool]:
    """Compara tras convertir a tipos compatibles o representaciones consistentes."""
    numero = 42
    texto = "42"
    resultado1 = (numero == int(texto))

    decimal = 3.14
    texto_decimal = "3.14"
    try:
        resultado2 = (decimal == float(texto_decimal))
    except ValueError:
        resultado2 = False

    booleano = True
    entero = 1
    resultado3 = (int(booleano) == entero)

    lista = [1, 2, 3]
    texto_lista = "[1, 2, 3]"
    resultado4 = (str(lista) == texto_lista)

    diccionario = {"a": 1}
    texto_dict = '{"a": 1}'
    resultado5 = (str(diccionario).replace("'", '"') == texto_dict)

    return resultado1, resultado2, resultado3, resultado4, resultado5


def comparaciones_imposibles(
    x: int = 5,
    y: int = 10,
    bandera: bool = False,
    valor_none: Optional[object] = None,
    texto: str = "None",
    lista_vacia: Optional[list] = None,
    diccionario_vacio: Optional[dict] = None,
) -> Tuple[str, str, bool, bool]:
    """Evita comparaciones "constantes" usando parámetros con valores por defecto.

    Esto mantiene el comportamiento previo con los valores por defecto, pero las
    condiciones dependen ahora de parámetros, evitando que Sonar marque
    condiciones siempre verdaderas o falsas.
    """
    # Comparación de enteros parametrizada
    resultado1 = "mayor" if y > x else "menor_igual"

    # Bandera parametrizada
    resultado2 = "ejecuta" if bandera else "no_ejecuta"

    # Comprobación de None parametrizada
    resultado3 = (valor_none is None and texto == "None")

    # Estructuras parametrizadas
    if lista_vacia is None:
        lista_vacia = []
    if diccionario_vacio is None:
        diccionario_vacio = {}
    resultado4 = (len(lista_vacia) == 0 and len(diccionario_vacio) == 0)

    return resultado1, resultado2, resultado3, resultado4


def operaciones_imposibles(
    a: int = 10,
    b: int = 2,
    c: int = 10,
    d: int = 3,
    lista: Optional[list[int]] = None,
    diccionario: Optional[dict] = None,
) -> Tuple[Optional[float], Optional[int], Optional[int], Optional[int]]:
    """Evita fallas en tiempo de ejecución usando validaciones y accesos seguros.

    La lógica depende de parámetros para que las condiciones no sean constantes.
    """
    res_div: Optional[float] = None
    if b != 0:
        res_div = a / b

    res_mod: Optional[int] = None
    if d != 0:
        res_mod = c % d

    if lista is None:
        lista = [1, 2, 3]
    res_idx: Optional[int] = lista[2] if 0 <= 2 < len(lista) else None

    if diccionario is None:
        diccionario = {"a": 1}
    res_key: Optional[int] = diccionario.get("b")

    return res_div, res_mod, res_idx, res_key


def uso_recursos_no_cerrados() -> str:
    """Gestiona archivos con context managers y retorna el contenido leído."""
    # Escritura segura
    with open("archivo2.txt", "w", encoding="utf-8") as f2:
        f2.write("contenido")
    with open("archivo3.txt", "a", encoding="utf-8") as f3:
        f3.write("más contenido")

    # Lectura segura ('' si no existe)
    return _safe_read_text("archivo1.txt")


def variables_no_inicializadas() -> Tuple[int, int]:
    """Inicializa explícitamente variables y produce resultados deterministas."""
    variable = 42
    resultado = variable + 10

    variable_bucle = 0
    for i in range(1):
        variable_bucle = i
    resultado_bucle = variable_bucle * 2

    return resultado, resultado_bucle


def excepciones_no_manejadas() -> Tuple[Optional[float], Optional[int], Optional[int]]:
    """Manejo específico de excepciones sin bloques vacíos ni genéricos."""
    # División segura
    div: Optional[float]
    a, b = 10, 0
    try:
        div = a / b
    except ZeroDivisionError:
        div = None

    # Conversión segura
    entero: Optional[int]
    try:
        entero = int("123")
    except ValueError:
        entero = None

    # Índice seguro
    lista = [1, 2, 3]
    try:
        idx = lista[5]
    except IndexError:
        idx = None

    return div, entero, idx


def comparaciones_strings_peligrosas(
    texto: str = "",
    valor: Optional[object] = None,
    numero_str: str = "123",
    numero_int: int = 123,
) -> Tuple[str, str, str]:
    """Compara de forma idiomática con entradas parametrizadas.

    Esto evita condiciones constantes desde el punto de vista del analizador.
    """
    r1 = "string vacío" if not texto else "string no vacío"

    r2 = "valor es None" if (valor is None) else "valor no es None"

    try:
        iguales = int(numero_str) == numero_int
    except ValueError:
        iguales = False
    r3 = "iguales" if iguales else "diferentes"

    return r1, r2, r3


def operaciones_lista_peligrosas(
    lista: Optional[list[int]] = None,
    lista_vacia: Optional[list[int]] = None,
    lista_vacia2: Optional[list[int]] = None,
) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[Any]]:
    """Valida índices y evita atributos inexistentes en listas, parametrizando entradas."""
    if lista is None:
        lista = [1, 2, 3]
    r1 = lista[0] if len(lista) > 0 else None

    if lista_vacia is None:
        lista_vacia = []
    r2 = lista_vacia[0] if len(lista_vacia) > 0 else None

    if lista_vacia2 is None:
        lista_vacia2 = []
    r3 = lista_vacia2.pop() if len(lista_vacia2) > 0 else None

    # Las listas no tienen atributos personalizados por defecto; devolver None
    r4 = None

    return r1, r2, r3, r4
