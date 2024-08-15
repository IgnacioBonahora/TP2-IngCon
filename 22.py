def calcular_precio_total(paquetes):
    # Crear un diccionario para almacenar el precio total por destino
    precios_totales = {}
    
    # Recorrer la lista de paquetes
    for destino, precio_por_dia, duracion in paquetes:
        # Calcular el precio total para el paquete
        precio_total = precio_por_dia * duracion
        # Añadir el destino y el precio total al diccionario
        precios_totales[destino] = precio_total
    
    return precios_totales

# Lista de paquetes turísticos
paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

# Llamar a la función y mostrar el resultado
resultados = calcular_precio_total(paquetes)
print(resultados)
