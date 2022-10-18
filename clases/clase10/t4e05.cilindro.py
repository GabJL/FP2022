# import
import math


# Funciones
def área_círculo(radio: float) -> float:
    resultado = math.pi * radio * radio
    return resultado


def longitud_círculo(radio: float) -> float:
    return 2 * math.pi * radio


def área_rectángulo(base: float, altura: float) -> float:
    return base * altura


def área_cilindro(radio: float, altura: float) -> float:
    return 2 * área_círculo(radio) + área_rectángulo(longitud_círculo(radio), altura)


# Programa principal
r: float = float(input("Indique el radio: "))
h: float = float(input("Indique la altura: "))

print("El área del cilindro es", área_cilindro(r,h))
