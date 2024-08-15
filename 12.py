def producto_mas_caro(productos):
    # Inicializamos el producto más caro con el primer producto de la lista
    mas_caro = productos[0]
    
    # Recorremos la lista de productos
    for producto in productos:
        # Comparamos el precio del producto actual con el precio del producto más caro
        if producto[1] > mas_caro[1]:
            mas_caro = producto
    
    return mas_caro

# Lista de productos
productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

# Llamamos a la función y mostramos el producto más caro
print(producto_mas_caro(productos))
