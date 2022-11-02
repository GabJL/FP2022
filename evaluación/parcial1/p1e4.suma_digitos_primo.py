def es_primo(N: int) -> bool:
    div: int = 2
    while N%div != 0:
        div += 1
    return div >= N

def sumar_digitos(N: int) -> int:
    suma: int = 0
    while N != 0:
        suma += N%10
        N = N//10
    return suma

# Programa principal
número: int = int(input("Dime un número: "))

suma = sumar_digitos(número)
while not es_primo(suma):
    número += 1
    suma = sumar_digitos(número)

print("El primer número que cumple la condición es", número)