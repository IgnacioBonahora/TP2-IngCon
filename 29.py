def calcular_promedios(notas_estudiantes):
    # Crear un diccionario para almacenar los promedios de calificaciones
    promedios = {}
    
    # Recorrer la lista de tuplas
    for nombre, calificaciones in notas_estudiantes:
        # Calcular el promedio de las calificaciones
        promedio = sum(calificaciones) / len(calificaciones)
        # Añadir el promedio al diccionario
        promedios[nombre] = promedio
    
    return promedios

# Lista de notas de los estudiantes
notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

# Llamar a la función y mostrar el resultado
promedios_estudiantes = calcular_promedios(notas_estudiantes)
print(promedios_estudiantes)
