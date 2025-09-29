from utilidades_matematicas import division_riesgosa, funcion_grande
from codigo_duplicado import sumar_numeros, agregar_numeros

def main():
    # --- New Issue: variable sin usar
    variable_inutil = "Nunca se usa"

    # --- Reliability: posible división por cero
    print("División riesgosa:", division_riesgosa(10, 0))

    # --- Maintainability: función muy larga y difícil de mantener
    datos = [1, 2, 3, 4, 5]
    print("Resultado función grande:", funcion_grande(datos))

    # --- Duplications: funciones con lógica repetida
    print("Sumar números:", sumar_numeros(3, 4))
    print("Agregar números:", agregar_numeros(3, 4))

if __name__ == "__main__":
    main()
