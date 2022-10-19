def contar_letras(texto: str, letra: str) -> int:
    contador: int = 0
    for l in texto:
        if l == letra:
            contador += 1
    return contador


def cantidad_palabras(texto: str) -> int:
    return contar_letras(texto, " ")


def escribir_frecuencia(texto: str) -> None:
    for l in "abcdefghijklmnopqrstuvwyxz":
        print("La letra", l, "aparece", contar_letras(texto, l), "veces")


# Programa principal
t: str = input("Dime una frase: ")
print("Hay", cantidad_palabras(t), "palabras")
print("La frecuencia de las letras son: ")
escribir_frecuencia(t)