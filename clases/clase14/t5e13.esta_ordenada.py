# --------- FUNCIONES -------------
def está_ordenada(l: list) -> bool:
    pos = 1
    while pos < len(l) and l[pos-1] <= l[pos]:
        pos += 1
    return pos >= len(l)


# --------- PROGRAMA PRINCIAL -------------
lista = [1, 3, 4, -1, 0, 5]
lista2 = [1, 5, 5, 8, 9]
if está_ordenada(lista):
    print("La lista", lista, "está ordenada")
else:
    print("La lista", lista, "NO está ordenada")

if está_ordenada(lista2):
    print("La lista", lista2, "está ordenada")
else:
    print("La lista", lista2, "NO está ordenada")