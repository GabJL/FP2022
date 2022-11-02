def calcular_precio(precio: float, impuesto: float) -> float:
    return precio*(1+impuesto/100)

# Programa principal
precio: float = float(input("Dime el precio: "))
iva: float = float(input("Dime el IVA: "))

precio_final: float = calcular_precio(precio, iva)

print("El precio final es", precio_final)