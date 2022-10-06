n: int = int(input("Dime un número: "))

divisores: int = 0
for i in range(2, n):
  if n%i == 0:
    divisores += 1
    
if divisores == 0:
  print(n, "es primo")
else:
  print(n, "no es primo")
