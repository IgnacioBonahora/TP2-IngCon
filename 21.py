def ordenar_por_puntuacion(puntuaciones):
    # Ordenar la lista de tuplas por la puntuación en orden descendente
    return sorted(puntuaciones, key=lambda x: x[1], reverse=True)

# Lista de puntuaciones
puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

# Llamar a la función y mostrar el resultado
puntuaciones_ordenadas = ordenar_por_puntuacion(puntuaciones)
print(puntuaciones_ordenadas)
