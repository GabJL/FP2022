MAX: int = 10 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

suma: int = 0 # No hemos leído ningún valor por lo tanto la suma actual es 0
num_veces: int = 0 # Número de valores leídos

while num_veces < MAX:
  num: int = int(input("Dime un número: ")) # Valor actual
  suma += num
  num_veces += 1

print("La suma vale", suma)