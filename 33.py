def simular_ventas(*ventas):
    total_ingresos = 0
    
    # Recorrer cada venta en *ventas
    for venta in ventas:
        producto, cantidad, precio = venta
        # Calcular el ingreso de esta venta y agregarlo al total
        total_ingresos += cantidad * precio
    
    return total_ingresos

# Ejemplo de uso
total = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print(total)
