# src/math_ops.py

def greet(name):
    unused_var = 123  # ❌ New Issue: variable no usada
    return f"Hello {name}"


def process_data(data):
    # ❌ Maintainability: función larga/compleja
    result = 0
    for i in range(len(data)):
        if data[i] % 2 == 0:
            result += data[i] * 2
        else:
            if data[i] % 3 == 0:
                result -= data[i] * 3
            else:
                if data[i] % 5 == 0:
                    result += data[i] * 5
                else:
                    result -= data[i]
    return result


def add_numbers(a, b):
    return a + b

def sum_numbers(a, b):
    return a + b

def sum_numbers(x, y):
    # ❌ Duplication: código idéntico a add_numbers
    return x + y

def risky_division(a, b):
    # ❌ Reliability: posible división por cero
    return a / b
