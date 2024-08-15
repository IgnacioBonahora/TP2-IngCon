def analizar_ventas(ventas_mensuales):
    # Calcular el total de ventas
    total_ventas = sum(ventas_mensuales)
    
    # Calcular el promedio mensual
    promedio_mensual = total_ventas / len(ventas_mensuales)
    
    # Encontrar el mes con mayores ventas (índice del máximo valor)
    mes_max_ventas = ventas_mensuales.index(max(ventas_mensuales)) + 1  # +1 para que sea 1-indexado
    
    # Crear el diccionario con las estadísticas
    estadisticas = {
        "Total de ventas": total_ventas,
        "Promedio mensual": promedio_mensual,
        "Mes con mayores ventas": mes_max_ventas
    }
    
    return estadisticas

# Array de ventas mensuales
ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

# Llamar a la función y mostrar el resultado
estadisticas_ventas = analizar_ventas(ventas_mensuales)
print(estadisticas_ventas)
