n: int = int(input("Introduce un número natural: "))

i: int = 2
while i < n and n % i != 0:
    i += 1

print("El número", n, end=" ")
if i >= n:
    print("es primo")
else:
    print("no es primo")
