def promedio_calificaciones(registro, matricula):
    # Verificamos si el número de matrícula está en el registro
    if matricula in registro:
        # Obtenemos las calificaciones del estudiante
        calificaciones = registro[matricula]["calificaciones"]
        
        # Calculamos el promedio de las calificaciones
        promedio = sum(calificaciones.values()) / len(calificaciones)
        
        return promedio
    else:
        return "Número de matrícula no encontrado"

# Registro de estudiantes
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

# Ejemplo de uso
matricula = 101
print(f"El promedio de calificaciones del estudiante con matrícula {matricula} es:", promedio_calificaciones(estudiantes, matricula))
