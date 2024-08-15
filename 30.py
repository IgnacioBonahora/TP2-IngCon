def configurar_perfiles(usuarios, **kwargs):
    # Crear un diccionario para almacenar las configuraciones de cada usuario
    perfiles = {}
    
    # Convertir las configuraciones de kwargs en una lista
    configuraciones = list(kwargs.values())
    
    # Asignar las configuraciones a cada usuario
    for usuario in usuarios:
        perfiles[usuario] = configuraciones
    
    return perfiles

# Lista de usuarios
usuarios = ["Ana", "Luis", "María"]

# Llamar a la función y mostrar el resultado
perfiles_configurados = configurar_perfiles(
    usuarios, 
    idioma="es", 
    modo_oscuro=True, 
    notificaciones=False
)
print(perfiles_configurados)
