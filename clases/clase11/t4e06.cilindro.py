import math


def área_círculo(radio: float) -> float:
    resultado: float = math.pi * radio * radio
    return resultado


def longitud_círculo(radio: float) -> float:
    return 2 * math.pi * radio


def área_rectángulo(base: float, altura: float) -> float:
    return base * altura


def área_cilindro(radio: float, altura: float) -> float:
    return 2 * área_círculo(radio) + área_rectángulo(longitud_círculo(radio), altura)


def volumen_cilindro(radio: float, altura: float) -> float:
    return área_círculo(radio) * altura


def mostrar_menu() -> None:
    print("Menú")
    print("1.- Área del cilindro")
    print("2.- Volumen del cilindro")
    print("Elige la opción oportuna (1 o 2):")


def pedir_opción() -> int:
    mostrar_menu()
    opción = int(input())
    while opción != 1 and opción != 2:
        opción = int(input("Opción incorrecta. Elija una opción entre 1 y 2: "))
    return opción


def pedir_valores() -> (float, float):
    radio: float = float(input("Indique el radio: "))
    while radio <= 0:
        radio = float(input("El radio debe ser positivo. Indique el radio: "))

    altura: float = float(input("Indique la altura: "))
    while altura <= 0:
        altura = float(input("La altura debe ser positiva. Indique la altura: "))

    return radio, altura


opt = pedir_opción()
r, h = pedir_valores()

if opt == 1:
    print("El área del cilindro es", área_cilindro(r, h))
else:
    print("El volumen del cilindro es", volumen_cilindro(r, h))