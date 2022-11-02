N: int = int(input("Dime un número: "))

suma: int = 0
for n in range(2, N+1, 2):
    suma += n

print("La suma de los pares entre 1 y", N, "es", suma)