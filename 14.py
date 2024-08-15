def analizar_temperaturas(temperaturas):
    # Calcular la temperatura media
    temperatura_media = sum(temperaturas) / len(temperaturas)
    
    # Encontrar la temperatura máxima
    temperatura_maxima = max(temperaturas)
    
    # Encontrar la temperatura mínima
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima

# Array de temperaturas
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

# Llamar a la función y mostrar los resultados
media, maxima, minima = analizar_temperaturas(temperaturas)
print(f"Temperatura media del mes: {media:.2f}")
print(f"Temperatura máxima del mes: {maxima:.2f}")
print(f"Temperatura mínima del mes: {minima:.2f}")
