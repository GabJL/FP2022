n: int = int(input("Dime un número: "))
mayor: int = n

while n < 0:
    if n > mayor:
        mayor = n
    n = int(input("Dime un número: "))

if mayor >= 0:
    print("No se leyeron números válidos")
else:
    print("El mayor valor leído fue", mayor)
