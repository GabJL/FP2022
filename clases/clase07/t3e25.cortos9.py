# Vale cualquier par de valores siempre que sean los mismos para forzar que entre en el bucle.
n1: int = 0
n2: int = 0
while n1 == n2:
    n1 = int(input("Dime un número: "))
    n2 = int(input("Dime otro número: "))
