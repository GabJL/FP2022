# Funciones
def leer_en_range(minimo: int, maximo:int) -> int:
    x: int = int(input("Dime un número entre " + str(minimo) + " y " + str(maximo) + ": "))
    while x < minimo or n > maximo:
        print("El número no está en el rango.")
        x = int(input("Dime un número entre " + str(minimo) + " y " + str(maximo) + ": "))
    return x


def es_primo(num: int) -> bool:
    div: int = 2
    while num % div != 0:
        div += 1
    return div >= num

# Programa principal
n1: int = leer_en_range(1, 20)
n2: int = leer_en_range(n1, 100)

print("Los primos en el rango", n1, "-", n2,"son: ", end="")
for n in range(n1, n2+1):
    if es_primo(n):
        print(n, end=" ")

