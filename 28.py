def libros_post_2000(biblioteca):
    # Crear una lista para almacenar los títulos de los libros publicados después del año 2000
    libros_recientes = []
    
    # Recorrer el diccionario de la biblioteca
    for titulo, info in biblioteca.items():
        # Verificar si el año de publicación es mayor a 2000
        if info["año"] > 2000:
            libros_recientes.append(titulo)
    
    return libros_recientes

# Diccionario de la biblioteca
biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

# Llamar a la función y mostrar el resultado
libros_recientes = libros_post_2000(biblioteca)
print(libros_recientes)
