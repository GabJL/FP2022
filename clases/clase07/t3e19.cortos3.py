MAX: int = 10 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

suma: int = 0 # No hemos leído ningún 0

num_veces: int = 0

while num_veces < MAX:
  num = int(input("Dime un número: "))
  suma += num
  num_veces += 1

print("La media vale", suma/10)
