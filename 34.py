def hacer_reserva(reservas, fecha, nombre_huesped, habitacion, precio):
    # Verificar si la fecha ya existe en el diccionario de reservas
    if fecha not in reservas:
        # Si la fecha no existe, crear una nueva entrada con una lista vacía
        reservas[fecha] = []
    
    # Verificar si la habitación está disponible en la fecha seleccionada
    for reserva in reservas[fecha]:
        _, habitacion_asignada, _ = reserva
        if habitacion_asignada == habitacion:
            print(f"La habitación {habitacion} ya está ocupada en la fecha {fecha}.")
            return reservas
    
    # Si la habitación está disponible, agregar la nueva reserva
    reservas[fecha].append((nombre_huesped, habitacion, precio))
    print(f"Reserva realizada para {nombre_huesped} en la habitación {habitacion} en la fecha {fecha}.")
    
    return reservas

# Diccionario de reservas
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

# Ejemplo de uso
reservas_actualizadas = hacer_reserva(reservas, "2024-08-15", "Marta", 103, 200)
reservas_actualizadas = hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 160)  # Habitación ocupada
reservas_actualizadas = hacer_reserva(reservas, "2024-08-17", "Laura", 101, 150)  # Nueva fecha

# Mostrar el diccionario actualizado
print(reservas_actualizadas)
