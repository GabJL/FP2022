# Funciones
def cantidad_divisores(n: int) -> int:
    # Generamos todos los valores entre 1 y n
    # Contamos los números que dividen a n
    contador: int = 0
    for i in range(1, n+1):
        # para cada valor, mirar si es divisor y contarlo en caso afirmativo
        if n%i == 0:
            contador += 1
    return contador


def es_primo(n: int) -> bool:
    # un número es primo si tiene 1 o 2 divisores únicamente
    if cantidad_divisores(n) <= 2:
        primo = True
    else:
        primo = False
    return primo


# Programa principal
# Leer 2 números
número1: int = int(input("Dime un número: "))
número2: int = int(input("Dime otro número: "))

# Calcular cuál es el mayor y menor de esos números
menor: int = min(número1, número2)
mayor: int = max(número1, número2)

# Mostrar los primos entre menor y mayor:
# 1.- Generar todos los valores entre menor y mayor
# 2.- Para cada valor mirar si es primo (si es primo lo mostramos)
print("Los números primos entre", menor, "y", mayor, "son:", end=" ")
for número in range(menor, mayor+1):
    if es_primo(número):
        print(número, end=" ")
