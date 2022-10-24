from math import sqrt

def altura_triángulo(lado: float) -> float:
    return lado*sqrt(3)/2

def área_triángulo(lado: float) -> float:
    return lado*altura_triángulo(lado)

# Programa principal
l: float = float(input("Dime el lado del triángulo: "))
print("Su área es: ", área_triángulo(l))