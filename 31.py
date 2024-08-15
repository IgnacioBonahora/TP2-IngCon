def calcular_promedio_general(calificaciones):
    # Combinar todas las calificaciones en una sola lista
    todas_calificaciones = []
    for materia, notas in calificaciones.items():
        todas_calificaciones.extend(notas)
    
    # Calcular el promedio general
    if todas_calificaciones:
        promedio_general = sum(todas_calificaciones) / len(todas_calificaciones)
    else:
        promedio_general = 0
    
    return promedio_general

def ranking_estudiantes(estudiantes):
    # Crear un diccionario para almacenar los promedios de cada estudiante
    promedios = {}
    
    # Calcular el promedio general de cada estudiante
    for estudiante_id, calificaciones in estudiantes.items():
        promedio_general = calcular_promedio_general(calificaciones)
        promedios[estudiante_id] = promedio_general
    
    # Ordenar los estudiantes por promedio en orden descendente
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

# Diccionario de estudiantes con sus calificaciones
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

# Llamar a la función y mostrar el ranking
ranking = ranking_estudiantes(estudiantes)
print(ranking)
