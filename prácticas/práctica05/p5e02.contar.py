def contar(l: list, x: int) -> int:
    contador: int = 0
    for v in l:
        if v == x:
            contador += 1
    return contador


# Programa principal
lista: list = [1, 2, 3, 2, 1]
print("En", lista, "hay", contar(lista, 1), "1s")