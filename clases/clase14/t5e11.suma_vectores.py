# --------- FUNCIONES -------------
def sumar_vectores(l1: list, l2: list) -> list:
    l3: list =[]
    for pos in range(len(l1)): # Ambas listas deben tener la misma longitud
        l3.append(l1[pos] + l2[pos])
    return l3


# --------- PROGRAMA PRINCIAL -------------
lista = [1, 3, 5, 8, 1, 2]
otra_lista = [9, 3, 4, -1, 0, -5]
lista_suma = sumar_vectores(lista, otra_lista)
print(lista, "+", otra_lista, "=", lista_suma)