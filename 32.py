def publicar(nombre_usuario, texto_publicacion, etiquetas=None, **kwargs):
    # Crear un diccionario para almacenar los detalles de la publicación
    publicacion = {
        "nombre_usuario": nombre_usuario,
        "texto_publicacion": texto_publicacion,
        "etiquetas": etiquetas if etiquetas is not None else []
    }
    
    # Añadir las opciones adicionales desde kwargs al diccionario
    for clave, valor in kwargs.items():
        publicacion[clave] = valor
    
    return publicacion

# Ejemplo de uso
resultado = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)

print(resultado)
