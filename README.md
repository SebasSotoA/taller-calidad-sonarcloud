# Taller de Calidad de Código - SonarCloud

Proyecto Python simplificado con problemas de calidad intencionales para demostrar los hallazgos de SonarCloud.

## Estructura del Proyecto

```
taller-calidad-sonarcloud/
├── src/
│   └── app/
│       ├── __init__.py
│       ├── calculator.py      # Calculadora con problemas
│       └── utils.py           # Utilidades con problemas
├── tests/
│   ├── test_calculator.py     # Pruebas incompletas
│   └── test_utils.py          # Pruebas incompletas
├── main.py                    # Archivo de demostración
├── requirements.txt           # Dependencias
├── pytest.ini               # Configuración de pruebas
└── README.md                 # Este archivo
```

## Tipos de Hallazgos Generados

### 1. **New Issues** (Problemas Nuevos)
- **Variables sin usar**: `unused_variable`, `unused_demo`, `unused_global`
- **Imports innecesarios**: `import os`, `import sys`, `import json`
- **Funciones sin usar**: `unused_function()`, `unused_helper()`
- **Variables globales sin usar**: `unused_global`, `unused_config`

### 2. **Maintainability** (Mantenibilidad)
- **Funciones muy largas**:
  - `process_user_data_and_validate_and_save_and_send_notification()`
  - `handle_user_registration_and_validation_and_notification()`
- **Funciones mal nombradas** y con demasiadas responsabilidades

### 3. **Duplications** (Duplicaciones)
- **Funciones de área**: `calculate_area_rectangle()`, `calculate_area_square()`, `calculate_area_triangle()`
- **Funciones de validación**: `validate_email()`, `validate_phone()`, `validate_name()`
- **Funciones de formato**: `format_string()`, `format_number()`, `format_boolean()`
- **Funciones de cálculo**: `calculate_total_price()`, `calculate_total_cost()`

### 4. **Coverage** (Cobertura de Pruebas)
- **Cobertura actual**: 44% (baja intencionalmente)
- **Funciones sin pruebas**: `multiply()`, `divide()`, `get_list_item()`, `access_dict_key()`, etc.

### 5. **Reliability** (Confiabilidad)
- **División por cero**: `divide()` sin validación
- **Acceso sin validación**: `get_list_item()`, `access_dict_key()`
- **Lista vacía**: `calculate_average()` sin validar lista vacía

## Cómo Ejecutar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas con cobertura
python -m pytest tests/ -v --cov=src --cov-report=term-missing

# Ejecutar el archivo principal
python main.py
```

## Métricas Actuales

- **Cobertura**: 44% (112 líneas, 63 sin cobertura)
- **Pruebas**: 7 pruebas ejecutadas
- **Archivos**: 2 módulos principales

## Objetivos de Mejora

1. **Aumentar cobertura** a 80%+
2. **Eliminar duplicaciones** refactorizando código común
3. **Dividir funciones largas** en funciones más pequeñas
4. **Añadir validaciones** para mejorar confiabilidad
5. **Eliminar código muerto** (variables y funciones sin usar)

Este proyecto está diseñado para generar hallazgos específicos en SonarCloud de forma simple y manejable.