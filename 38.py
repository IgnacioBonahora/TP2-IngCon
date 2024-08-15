def analizar_tendencias(hashtags, tendencias, frecuencia_minima):
    # Contar las menciones de cada hashtag en el array de hashtags
    conteo_hashtags = {}
    
    for hashtag in hashtags:
        if hashtag in conteo_hashtags:
            conteo_hashtags[hashtag] += 1
        else:
            conteo_hashtags[hashtag] = 1
    
    # Crear un diccionario para las frecuencias de tendencias
    tendencias_dict = dict(tendencias)
    
    # Filtrar los hashtags que superan la frecuencia mínima
    hashtags_filtrados = [hashtag for hashtag, conteo in conteo_hashtags.items()
                          if conteo >= frecuencia_minima and hashtag in tendencias_dict and tendencias_dict[hashtag] >= frecuencia_minima]
    
    return hashtags_filtrados

# Datos de entrada
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

# Especificar la frecuencia mínima
frecuencia_minima = 2

# Obtener los hashtags que cumplen con la frecuencia mínima
resultados = analizar_tendencias(hashtags, tendencias, frecuencia_minima)

# Mostrar el resultado
print(resultados)
