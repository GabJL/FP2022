print("Dimes números acabado en uno negativo")

num_pares: int = 0
número: int = int(input())

while número >= 0:
    if número%2 == 0:
        num_pares += 1
        if num_pares == 1 or mínimo > número:
            mínimo = número
    número = int(input())

if num_pares == 0:
    print("No se leyó ningún par.")
else:
    print("El número de pares leídos fue", num_pares, "y el menor", mínimo)