"""
Archivo principal simplificado para demostrar problemas de calidad.
"""

from src.app.calculator import Calculator, calculate_average, validate_email
from src.app.utils import format_string, calculate_total_price


def main():
    """Función principal simplificada."""
    print("=== Demostración de problemas de calidad ===")
    
    # New Issue: variable sin usar
    unused_demo = "Variable sin usar"
    
    # Demostrar calculadora
    calc = Calculator()
    print(f"Suma: {calc.add(5, 3)}")
    print(f"Resta: {calc.subtract(10, 4)}")
    
    # Reliability Issue: división por cero
    try:
        result = calc.divide(10, 0)
        print(f"División: {result}")
    except ZeroDivisionError:
        print("Error: División por cero")
    
    # Demostrar utilidades
    formatted = format_string("  hello world  ")
    print(f"Formateado: {formatted}")
    
    # Demostrar cálculo de precios
    items = [{'price': 10, 'quantity': 2}, {'price': 5, 'quantity': 3}]
    total = calculate_total_price(items)
    print(f"Total: {total}")
    
    # Demostrar validación
    is_valid = validate_email("test@example.com")
    print(f"Email válido: {is_valid}")
    
    print("=== Demostración completada ===")


if __name__ == "__main__":
    main()