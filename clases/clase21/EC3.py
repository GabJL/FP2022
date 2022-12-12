def intersección(l1: list, l2: list) -> list:
    res: list = []
    for elemento in l1:
        if elemento in l2 and elemento not in res:
            veces_l1: int = l1.count(elemento)
            veces_l2: int = l2.count(elemento)
            if veces_l1 < veces_l2:
                menor = veces_l1
            else:
                menor = veces_l2
            for i in range(menor):
                res.append(elemento)
    return res


def intersección2(l1: list, l2: list) -> list:
    res: list = []
    for elemento in l1:
        if elemento in l2:
            res.append(elemento)
            l2.remove(elemento)
    return res


# Programa principal
print(intersección2([1,2], [2,4])) # [2]
print(intersección2([1,4,2], [2,4])) # [4,2]
print(intersección2([1,2,2,3,5, 5], [5,2,2,2,4])) # [2,2,5]
print(intersección2([1,2], [3,4])) # []
