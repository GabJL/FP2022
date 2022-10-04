MAX: int = 20 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

pares: int = 0
impares: int = 0

num_veces: int = 0

while num_veces < MAX:
  num = int(input("Dime un número: "))
  if num%2 ==  0:
    pares += 1
  else:
    impares += 1
  num_veces += 1

# Se podría evitar contar los impares y calcularlo como num_veces - pares

print("Se han leído", pares, "números pares y", impares, "números impares")