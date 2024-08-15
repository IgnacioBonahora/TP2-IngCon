def simular_mercado(precios_diarios, operaciones):
    saldo = 0
    acciones = 0
    precio_compra = 0

    for operacion, dia in operaciones:
        precio = precios_diarios[dia]
        if operacion == "compra":
            # Comprar acciones
            precio_compra = precio
            acciones += 1
        elif operacion == "venta":
            # Vender acciones
            if acciones > 0:
                saldo += precio - precio_compra
                acciones -= 1
            else:
                print(f"No hay acciones para vender en el día {dia}")
    
    # Si aún queda alguna acción sin vender, el beneficio o pérdida no se calcula para esas acciones.
    if acciones > 0:
        print(f"Aún quedan {acciones} acciones sin vender.")

    return saldo

# Datos de ejemplo
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

# Ejecutar la simulación
beneficio_o_perdida = simular_mercado(precios_diarios, operaciones)

# Mostrar el resultado
print(f"Beneficio o pérdida total: {beneficio_o_perdida}")
