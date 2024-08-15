def procesar_ventas(ventas_diarias):
    # Calcular el total de ventas
    total_ventas = sum(ventas_diarias)
    
    # Calcular el promedio de ventas por día
    if len(ventas_diarias) > 0:
        promedio_ventas = total_ventas / len(ventas_diarias)
    else:
        promedio_ventas = 0
    
    return total_ventas, promedio_ventas

# Array de ventas diarias
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

# Llamar a la función y mostrar los resultados
total, promedio = procesar_ventas(ventas_diarias)
print(f"Total de ventas: {total}")
print(f"Promedio de ventas por día: {promedio:.2f}")
