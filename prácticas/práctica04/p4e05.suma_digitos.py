n: int = int(input("Introduce un número natural: "))

suma: int = 0

while n != 0:
    ultimo_digito = n % 10
    n = n // 10
    suma += ultimo_digito

print("La suma de los dígitos es:", suma)
