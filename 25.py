def analizar_finanzas(**kwargs):
    # Calcular el balance sumando todos los valores en kwargs
    balance = sum(kwargs.values())
    return balance

# Ejemplo de uso
balance_final = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"Balance final: {balance_final}")

