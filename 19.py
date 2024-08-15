def calcular_totales(resultados):
    # Inicializar los contadores de goles anotados y recibidos
    total_goles_anotados = 0
    total_goles_recibidos = 0
    
    # Recorrer el diccionario de resultados
    for goles_anotados, goles_recibidos in resultados.values():
        total_goles_anotados += goles_anotados
        total_goles_recibidos += goles_recibidos
    
    return total_goles_anotados, total_goles_recibidos

# Diccionario de resultados
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

# Llamar a la función y mostrar los resultados
total_anotados, total_recibidos = calcular_totales(resultados)
print(f"Total de goles anotados: {total_anotados}")
print(f"Total de goles recibidos: {total_recibidos}")
