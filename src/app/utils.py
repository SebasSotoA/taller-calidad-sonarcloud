"""
Utilidades con problemas de calidad específicos para SonarCloud.
"""

import json  # New Issue: import innecesario
import datetime  # New Issue: import innecesario


def format_string(data):
    """Formatea string."""
    return data.strip().upper()


def format_number(data):
    """Formatea número."""
    return round(float(data), 2)


def format_boolean(data):
    """Formatea booleano."""
    return bool(data)


# Duplication Issue: funciones similares (mismo patrón)
def calculate_total_price(items):
    """Calcula precio total."""
    total = 0
    for item in items:
        if 'price' in item and 'quantity' in item:
            total += item['price'] * item['quantity']
    return total


def calculate_total_cost(items):
    """Calcula costo total."""
    total = 0
    for item in items:
        if 'cost' in item and 'quantity' in item:
            total += item['cost'] * item['quantity']
    return total


def calculate_total_value(items):
    """Calcula valor total."""
    total = 0
    for item in items:
        if 'value' in item and 'quantity' in item:
            total += item['value'] * item['quantity']
    return total


# Maintainability Issue: función muy larga (más de 50 líneas)
def handle_user_registration_and_validation_and_notification(user_info):
    """Función muy larga con muchas responsabilidades."""
    # Validar entrada
    if not user_info:
        return None
    if not user_info.get('username'):
        return None
    if not user_info.get('password'):
        return None
    if not user_info.get('email'):
        return None
    if not user_info.get('first_name'):
        return None
    if not user_info.get('last_name'):
        return None
    
    # Procesar datos
    username = user_info['username'].strip().lower()
    password = user_info['password']
    email = user_info['email'].strip().lower()
    first_name = user_info['first_name'].strip().title()
    last_name = user_info['last_name'].strip().title()
    
    # Validar formato
    if len(username) < 3:
        return None
    if len(password) < 8:
        return None
    if '@' not in email:
        return None
    if len(first_name) < 2:
        return None
    if len(last_name) < 2:
        return None
    
    # Crear usuario
    user = {
        'id': 12345,
        'username': username,
        'password': password,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f"{first_name} {last_name}",
        'active': True,
        'created_at': datetime.datetime.now().isoformat(),
        'permissions': ['read', 'write'],
        'profile': {
            'theme': 'light',
            'language': 'es',
            'notifications': True
        }
    }
    
    # Simular guardado
    print(f"Usuario creado: {username}")
    print(f"Email enviado a: {email}")
    print(f"Perfil configurado para: {user['full_name']}")
    
    return user


# Reliability Issue: función sin validación
def divide_numbers(a, b):
    """Divide dos números sin validación."""
    return a / b  # Puede generar ZeroDivisionError


# Reliability Issue: función sin validación
def get_array_element(array, index):
    """Obtiene elemento de array sin validación."""
    return array[index]  # Puede generar IndexError


# Reliability Issue: función sin validación
def get_dict_value(dictionary, key):
    """Obtiene valor de diccionario sin validación."""
    return dictionary[key]  # Puede generar KeyError


# New Issue: función sin usar
def unused_helper():
    """Función que nunca se usa."""
    return "Helper sin usar"


# New Issue: variable sin usar
unused_config = {"debug": True, "version": "1.0"}