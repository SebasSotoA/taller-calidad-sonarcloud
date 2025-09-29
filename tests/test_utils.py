"""
Pruebas simples para utils.py
"""

import pytest
from src.app.utils import format_string, calculate_total_price


def test_format_string():
    """Prueba formato de string."""
    result = format_string("  hello  ")
    assert result == "HELLO"


def test_calculate_total_price():
    """Prueba cálculo de precio total."""
    items = [
        {'price': 10, 'quantity': 2},
        {'price': 5, 'quantity': 3}
    ]
    result = calculate_total_price(items)
    assert result == 35


# Coverage Issue: falta prueba para format_number
# Coverage Issue: falta prueba para format_boolean
# Coverage Issue: falta prueba para calculate_total_cost
# Coverage Issue: falta prueba para get_list_item
# Coverage Issue: falta prueba para access_dict_key
# Coverage Issue: falta prueba para handle_user_registration_and_validation_and_notification
