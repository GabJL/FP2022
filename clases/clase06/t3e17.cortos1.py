MAX: int = 20 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

contador_de_0s: int = 0 # No hemos leído ningún 0
num_veces: int = 0 # Número de números leídos

while num_veces < MAX:
  num: int = int(input("Dime un número: ")) # Valor actual
  if num == 0:
    contador_de_0s += 1
  num_veces += 1

print("Se han leído", contador_de_0s, "0s")