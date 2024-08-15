def calcular_promedio(*args):
    # Verificar si se han pasado notas
    if len(args) == 0:
        return "No se han proporcionado notas."
    
    # Calcular el promedio de las notas
    promedio = sum(args) / len(args)
    
    return promedio

# Ejemplo de uso
notas = (85, 90, 78, 92)
promedio = calcular_promedio(*notas)
print(f"El promedio de las notas es: {promedio:.2f}")

