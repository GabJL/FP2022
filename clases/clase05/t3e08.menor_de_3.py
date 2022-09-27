a: int = int(input("Dime un número: "))
b: int = int(input("Dime otro número: "))
c: int = int(input("Dime otro número: "))

# Se propone una solución usando if anidados y sin condiciones compuestas. Existen otro tipo de soluciones más simples
if a < b:
    if a < c:
        menor: int = a
    else:
        menor: int = c
else:
    if b < c:
        menor: int = b
    else:
        menor: int = c

print("El menor de los tres valores es ", menor)