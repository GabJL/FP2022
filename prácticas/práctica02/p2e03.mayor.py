a = int(input("Indique un número: "))
mayor = a

a = int(input("Indique otro número: "))
if a > mayor:
    mayor = a

a = int(input("Indique otro número: "))
if a > mayor:
    mayor = a

print("El mayor número es el", mayor)