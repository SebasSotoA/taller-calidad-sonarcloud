"""
Pruebas simples para calculator.py
"""

import pytest
from src.app.calculator import Calculator, calculate_average, validate_email


class TestCalculator:
    """Pruebas para Calculator."""
    
    def test_calculator_init(self):
        """Prueba inicialización."""
        calc = Calculator()
        assert calc.history == []
    
    def test_add(self):
        """Prueba suma."""
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
    
    def test_subtract(self):
        """Prueba resta."""
        calc = Calculator()
        result = calc.subtract(5, 3)
        assert result == 2
    
    # Coverage Issue: falta prueba para multiply
    # Coverage Issue: falta prueba para divide
    # Coverage Issue: falta prueba para get_history
    # Coverage Issue: falta prueba para clear_history


def test_calculate_average():
    """Prueba promedio."""
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    assert result == 3.0


def test_validate_email():
    """Prueba validación de email."""
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


# Coverage Issue: falta prueba para calculate_area_rectangle
# Coverage Issue: falta prueba para calculate_area_square
# Coverage Issue: falta prueba para calculate_area_triangle
# Coverage Issue: falta prueba para validate_phone
# Coverage Issue: falta prueba para validate_name
# Coverage Issue: falta prueba para process_user_data_and_validate_and_save_and_send_notification