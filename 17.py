def empleados_con_sueldo_mayor(empleados, salario_umbral):
    # Crear un diccionario para almacenar los empleados que ganan más que el salario umbral
    empleados_mayores = {}
    
    # Recorrer el diccionario de empleados
    for id_empleado, info in empleados.items():
        nombre, edad, salario = info
        # Verificar si el salario del empleado es mayor que el umbral
        if salario > salario_umbral:
            empleados_mayores[id_empleado] = info
    
    return empleados_mayores

# Diccionario de empleados
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

# Ejemplo de uso
salario_umbral = 2800
resultado = empleados_con_sueldo_mayor(empleados, salario_umbral)

# Imprimir el resultado
print(resultado)
