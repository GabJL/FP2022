# Pedimos datos
precio: float = float(input("Precio: "))

# Cálculos
IVA: float = 0.21
precio_sin_iva: float = precio/(1+IVA)

# Mostrar resultado
print("El precio sin IVA es", precio_sin_iva)