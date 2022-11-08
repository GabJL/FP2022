# --------- FUNCIONES -------------
def comunes_sin_repeticiones(l1: list, l2: list) -> list:
    res = []
    for v in l1:
        if v in l2 and v not in res:
            res.append(v)
    return res


# --------- PROGRAMA PRINCIAL -------------
lista = [1, 3, 1, 4, -1, 0, 5]
lista2 = [1, 5, 5, 1, 8, 9]
inter = comunes_sin_repeticiones(lista, lista2)
print(lista, "interseccion", lista2, "=", inter)
