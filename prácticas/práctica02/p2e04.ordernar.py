a:int  = int(input("Indique un número: "))
b: int = int(input("Indique otro número: "))
c: int = int(input("Indique otro número: "))

if a > b:
    aux = a
    a = b
    b = aux
# Tras este primer if a tiene el valor más pequeño entre a y b
if a > c:
    aux = a
    a = c
    c = aux
# Tras este segundo if a tiene el valor más pequeño entre los 3 valores
if b > c:
    aux = b
    b = c
    c = aux
# Tras este if ya tenemos todos ordenados
print("Los números ordenados son: ", a, b, c)
