def actualizar_suscripcion(suscripciones, **kwargs):
    # Extraer el nombre del usuario y el tipo de suscripción del diccionario kwargs
    usuario = kwargs.pop('usuario', None)
    suscripcion = kwargs.pop('suscripcion', None)
    
    # Verificar si el usuario ya tiene suscripciones
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    
    # Actualizar el historial de suscripciones
    if suscripcion:
        suscripciones[usuario].append(suscripcion)
    
    # Aquí puedes manejar otras opciones adicionales, como auto-renovación
    opciones_adicionales = kwargs
    if opciones_adicionales:
        print(f"Opciones adicionales para {usuario}: {opciones_adicionales}")
    
    return suscripciones

# Diccionario de suscripciones inicial
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

# Actualizar la suscripción
suscripciones_actualizadas = actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)

# Mostrar el estado actualizado de las suscripciones
print(suscripciones_actualizadas)
