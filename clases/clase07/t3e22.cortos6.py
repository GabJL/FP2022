suma: int = 0 # No hemos leído ningún 0

num_veces: int = 0

num: int = int(input("Dime un número: "))
while num != 0:
  suma += num
  num_veces += 1
  num = int(input("Dime un número: "))

if num_veces > 0:
    print("La media vale", suma/num_veces)
else:
    print("No se leyeron números")
