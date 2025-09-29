"""
Utilidades simples con problemas de calidad.
"""

import json  # New Issue: import innecesario


def format_string(data):
    """Formatea string."""
    return data.strip().upper()


def format_number(data):
    """Formatea número."""
    return round(float(data), 2)


def format_boolean(data):
    """Formatea booleano."""
    return bool(data)


# Duplication Issue: funciones similares
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


# Reliability Issue: función sin validación
def get_list_item(items, index):
    """Obtiene elemento sin validar índice."""
    return items[index]  # Puede generar IndexError


def access_dict_key(data, key):
    """Accede a clave sin validar existencia."""
    return data[key]  # Puede generar KeyError


# Maintainability Issue: función muy larga
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
    
    # Procesar datos
    username = user_info['username'].strip().lower()
    password = user_info['password']
    email = user_info['email'].strip().lower()
    
    # Validar formato
    if len(username) < 3:
        return None
    if len(password) < 8:
        return None
    if '@' not in email:
        return None
    
    # Crear usuario
    user = {
        'id': 12345,
        'username': username,
        'password': password,
        'email': email,
        'active': True,
        'created_at': '2024-01-01'
    }
    
    # Simular guardado
    print(f"Usuario creado: {username}")
    
    # Simular notificación
    print(f"Email enviado a: {email}")
    
    return user


# New Issue: función sin usar
def unused_helper():
    """Función que nunca se usa."""
    return "Helper sin usar"


# New Issue: variable sin usar
unused_config = {"debug": True}
