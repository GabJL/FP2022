n: int = int(input("Dime un número: "))

es_primo: bool = True
for i in range(2, n):
  if n%i == 0:
    es_primo = False
    
if es_primo:
  print(n, "es primo")
else:
  print(n, "no es primo")
