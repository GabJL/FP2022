def contar(l: list, x: int) -> int:
    contador: int = 0
    for v in l:
        if v == x:
            contador += 1
    return contador


def hayRepes(l: list) -> bool:
    i: int = 0
    repetido: bool = False
    while i < len(l) and not repetido:
        if contar(l, l[i]) > 1:
            repetido = True
        i += 1
    return repetido


# Programa principal
lista: list = [1, 2, 3, 3]

print("Hay repetidos en", lista, "->", hayRepes(lista))