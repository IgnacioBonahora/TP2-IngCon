def filtrar_rutas(rutas, distancias_max):
    rutas_validas = []
    
    # Asegurarse de que la lista de rutas y la lista de distancias máximas tengan la misma longitud
    if len(rutas) != len(distancias_max):
        raise ValueError("La longitud de la lista de rutas debe ser igual a la longitud de la lista de distancias máximas")
    
    # Recorrer la lista de rutas y distancias máximas
    for ruta, distancia_max in zip(rutas, distancias_max):
        origen, destino, distancia = ruta
        
        # Comparar la distancia de la ruta con la distancia máxima permitida
        if distancia <= distancia_max:
            rutas_validas.append(ruta)
    
    return rutas_validas

# Lista de rutas y distancias máximas permitidas
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

# Ejemplo de uso
rutas_filtradas = filtrar_rutas(rutas, distancias_max)

# Mostrar el resultado
print(rutas_filtradas)
