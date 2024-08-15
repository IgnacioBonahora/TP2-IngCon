def analizar_encuestas(encuestas):
    resultado = {}
    
    # Recorrer cada pregunta en el diccionario de encuestas
    for pregunta, respuestas in encuestas.items():
        # Crear un diccionario para almacenar las frecuencias de cada respuesta
        frecuencias = {}
        
        # Contar las frecuencias de cada respuesta
        for respuesta in respuestas:
            if respuesta in frecuencias:
                frecuencias[respuesta] += 1
            else:
                frecuencias[respuesta] = 1
        
        # Añadir el diccionario de frecuencias al resultado para la pregunta actual
        resultado[pregunta] = frecuencias
    
    return resultado

# Diccionario de encuestas
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

# Ejemplo de uso
resultado_analisis = analizar_encuestas(encuestas)

# Mostrar el resultado
print(resultado_analisis)
