# --------- FUNCIONES -------------
def filtrar_positivos(l: list) -> list:
    res =[]
    for v in l:
        if v > 0:
            res.append(v)
    return res


# --------- PROGRAMA PRINCIAL -------------
lista = [9, 3, 4, -1, 0, -5]
filtrada = filtrar_positivos(lista)
print(lista, "filtrada a solo positivos", filtrada)