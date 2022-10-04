pares: int = 0
impares: int = 0


num: int = int(input("Dime un número: "))
while num >= 0:
  if num%2 ==  0:
    pares += 1
  else:
    impares += 1
  num = int(input("Dime un número: "))

print("Se han leído", pares, "números pares y", impares, "números impares")