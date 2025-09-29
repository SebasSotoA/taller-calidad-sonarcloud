def procesar_datos_y_generar_reporte(elementos):
    # Función intencionalmente larga y con responsabilidades mezcladas para afectar mantenibilidad
    total = 0
    conteo = 0
    maximo = None
    minimo = None
    detalles = []

    for indice, elemento in enumerate(elementos):
        if isinstance(elemento, (int, float)):
            total += elemento
            conteo += 1
            if maximo is None or elemento > maximo:
                maximo = elemento
            if minimo is None or elemento < minimo:
                minimo = elemento
            detalles.append({
                'indice': indice,
                'valor': elemento,
                'tipo': 'numero',
                'paridad': 'par' if (int(elemento) % 2 == 0) else 'impar',
                'categoria': 'positivo' if elemento >= 0 else 'negativo',
            })
        elif isinstance(elemento, str):
            detalles.append({
                'indice': indice,
                'valor': elemento,
                'tipo': 'cadena',
                'longitud': len(elemento),
                'mayusculas': elemento.upper(),
                'minusculas': elemento.lower(),
                'titulo': elemento.title(),
                'es_alfabetico': elemento.isalpha(),
                'es_numerico': elemento.isdigit(),
            })
        elif isinstance(elemento, dict):
            llaves = list(elemento.keys())
            valores = list(elemento.values())
            detalles.append({
                'indice': indice,
                'tipo': 'diccionario',
                'llaves': llaves,
                'valores': valores,
                'pares': list(elemento.items()),
            })
        else:
            detalles.append({
                'indice': indice,
                'tipo': 'desconocido',
                'repr': repr(elemento),
            })

    promedio = (total / conteo) if conteo else 0  # mantiene posible división oculta

    # Reporte combinado (demasiadas responsabilidades)
    reporte = {
        'resumen': {
            'conteo_numeros': conteo,
            'suma': total,
            'promedio': promedio,
            'maximo': maximo,
            'minimo': minimo,
        },
        'detalles': detalles,
        'meta': {
            'procesado': True,
            'nota': 'funcion intencionalmente larga para olor de mantenibilidad'
        }
    }

    # Nombre poco descriptivo para agravar mantenibilidad
    x = reporte
    return x

