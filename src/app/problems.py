"""
Archivo con problemas de calidad específicos para SonarCloud.
"""

import os  # New Issue: import innecesario
import sys  # New Issue: import innecesario
import json  # New Issue: import innecesario


# New Issue: variable sin usar
unused_global_variable = "Esta variable nunca se usa"


# New Issue: función sin usar
def unused_function():
    """Esta función nunca se usa."""
    return "Función sin usar"


# Duplication Issue: funciones idénticas
def get_user_name(user):
    """Obtiene nombre de usuario."""
    return user.get('name', 'Unknown')


def get_user_email(user):
    """Obtiene email de usuario."""
    return user.get('email', 'Unknown')


def get_user_phone(user):
    """Obtiene teléfono de usuario."""
    return user.get('phone', 'Unknown')


# Duplication Issue: funciones similares
def calculate_sum(numbers):
    """Calcula suma."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_product(numbers):
    """Calcula producto."""
    total = 1
    for num in numbers:
        total *= num
    return total


def calculate_max(numbers):
    """Calcula máximo."""
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


# Maintainability Issue: función muy larga
def process_complete_user_registration_and_validation_and_database_storage_and_email_notification_and_logging(user_data):
    """Función extremadamente larga con demasiadas responsabilidades."""
    # Validar entrada
    if not user_data:
        return None
    if not user_data.get('username'):
        return None
    if not user_data.get('password'):
        return None
    if not user_data.get('email'):
        return None
    if not user_data.get('first_name'):
        return None
    if not user_data.get('last_name'):
        return None
    if not user_data.get('phone'):
        return None
    if not user_data.get('address'):
        return None
    
    # Procesar datos
    username = user_data['username'].strip().lower()
    password = user_data['password']
    email = user_data['email'].strip().lower()
    first_name = user_data['first_name'].strip().title()
    last_name = user_data['last_name'].strip().title()
    phone = user_data['phone'].replace('-', '').replace(' ', '')
    address = user_data['address'].strip().title()
    
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
    if len(phone) < 10:
        return None
    if len(address) < 10:
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
        'phone': phone,
        'address': address,
        'active': True,
        'created_at': '2024-01-01',
        'permissions': ['read', 'write', 'admin'],
        'profile': {
            'theme': 'light',
            'language': 'es',
            'notifications': True,
            'privacy': 'public'
        },
        'metadata': {
            'source': 'web',
            'version': '1.0',
            'ip': '127.0.0.1',
            'user_agent': 'Mozilla/5.0'
        }
    }
    
    # Simular guardado en base de datos
    print(f"Usuario guardado en BD: {username}")
    
    # Simular envío de email
    print(f"Email de bienvenida enviado a: {email}")
    
    # Simular logging
    print(f"Registro de usuario logueado: {user['full_name']}")
    
    return user


# Reliability Issue: función sin validación
def divide_by_zero(a, b):
    """Divide sin validar cero."""
    return a / b  # Puede generar ZeroDivisionError


# Reliability Issue: función sin validación
def access_invalid_index(items, index):
    """Accede a índice sin validar."""
    return items[index]  # Puede generar IndexError


# Reliability Issue: función sin validación
def access_invalid_key(data, key):
    """Accede a clave sin validar."""
    return data[key]  # Puede generar KeyError


# Reliability Issue: función sin validación
def calculate_average_invalid(numbers):
    """Calcula promedio sin validar lista vacía."""
    total = sum(numbers)
    count = len(numbers)
    return total / count  # Puede generar ZeroDivisionError
