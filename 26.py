def registro_empleado(nombre, edad, salario, **kwargs):
    # Crear el diccionario con la información obligatoria
    empleado = {
        "Nombre": nombre,
        "Edad": edad,
        "Salario": salario
    }
    
    # Añadir los datos opcionales al diccionario
    empleado.update(kwargs)
    
    return empleado

# Ejemplo de uso
empleado_info = registro_empleado(
    "Ana", 
    30, 
    3000, 
    direccion="Calle Falsa 123", 
    telefono="123456789"
)

# Mostrar la información del empleado
print(empleado_info)
