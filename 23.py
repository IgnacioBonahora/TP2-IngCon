def actualizar_inventario(inventario, ventas):
    # Verificar que las listas de inventario y ventas tengan el mismo tamaño
    if len(inventario) != len(ventas):
        raise ValueError("El tamaño de las listas de inventario y ventas debe ser el mismo.")
    
    # Actualizar el inventario restando las ventas
    inventario_actualizado = [inventario[i] - ventas[i] for i in range(len(inventario))]
    
    return inventario_actualizado

# Array de inventario
inventario = [50, 30, 20, 10]

# Array de ventas
ventas = [5, 10, 5, 2]

# Llamar a la función y mostrar el inventario actualizado
inventario_actualizado = actualizar_inventario(inventario, ventas)
print(inventario_actualizado)
