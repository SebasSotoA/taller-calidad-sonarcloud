"""
Calculadora con problemas de calidad específicos para SonarCloud.
"""

import os  # New Issue: import innecesario
import sys  # New Issue: import innecesario


class Calculator:
    """Calculadora básica."""
    
    def __init__(self):
        self.history = []
        self.unused_variable = "No se usa"  # New Issue: variable sin usar
    
    def add(self, a, b):
        """Suma dos números."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Resta dos números."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplica dos números."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide dos números."""
        # Reliability Issue: división por cero sin validación
        result = a / b  # Puede generar ZeroDivisionError
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Obtiene el historial."""
        return self.history
    
    def clear_history(self):
        """Limpia el historial."""
        self.history = []


# Duplication Issue: funciones similares (mismo patrón)
def calculate_area_rectangle(length, width):
    """Calcula área de rectángulo."""
    return length * width


def calculate_area_square(side):
    """Calcula área de cuadrado."""
    return side * side


def calculate_area_triangle(base, height):
    """Calcula área de triángulo."""
    return (base * height) / 2


# Duplication Issue: funciones similares (mismo patrón)
def validate_email(email):
    """Valida email."""
    return "@" in email and "." in email


def validate_phone(phone):
    """Valida teléfono."""
    return len(phone) >= 10 and phone.isdigit()


def validate_name(name):
    """Valida nombre."""
    return len(name) >= 2 and name.isalpha()


# Maintainability Issue: función muy larga (más de 50 líneas)
def process_user_data_and_validate_and_save_and_send_notification(user_data):
    """Función muy larga con demasiadas responsabilidades."""
    # Validar datos
    if not user_data.get('name'):
        return False
    if not user_data.get('email'):
        return False
    if not user_data.get('phone'):
        return False
    if not user_data.get('age'):
        return False
    if not user_data.get('address'):
        return False
    
    # Procesar datos
    processed_name = user_data['name'].strip().upper()
    processed_email = user_data['email'].strip().lower()
    processed_phone = user_data['phone'].replace('-', '').replace(' ', '')
    processed_age = int(user_data['age'])
    processed_address = user_data['address'].strip().title()
    
    # Validar formato
    if not validate_email(processed_email):
        return False
    if not validate_phone(processed_phone):
        return False
    if not validate_name(processed_name):
        return False
    if processed_age < 18:
        return False
    if len(processed_address) < 10:
        return False
    
    # Simular guardado
    user_record = {
        'id': 12345,
        'name': processed_name,
        'email': processed_email,
        'phone': processed_phone,
        'age': processed_age,
        'address': processed_address,
        'created_at': '2024-01-01',
        'status': 'active',
        'permissions': ['read', 'write'],
        'metadata': {
            'source': 'web',
            'version': '1.0',
            'ip': '127.0.0.1'
        }
    }
    
    # Simular notificación
    print(f"Usuario procesado: {processed_name}")
    print(f"Email enviado a: {processed_email}")
    print(f"Registro guardado con ID: {user_record['id']}")
    
    return user_record


# Reliability Issue: función sin validación
def calculate_average(numbers):
    """Calcula promedio sin validar lista vacía."""
    total = sum(numbers)
    count = len(numbers)
    return total / count  # Puede generar ZeroDivisionError


# Reliability Issue: función sin validación
def get_list_item(items, index):
    """Obtiene elemento sin validar índice."""
    return items[index]  # Puede generar IndexError


# Reliability Issue: función sin validación
def access_dict_key(data, key):
    """Accede a clave sin validar existencia."""
    return data[key]  # Puede generar KeyError


# New Issue: función sin usar
def unused_function():
    """Esta función nunca se usa."""
    return "Función sin usar"


# New Issue: variable sin usar
unused_global = "Variable global sin usar"