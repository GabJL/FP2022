def intersección(l1: list, l2: list) -> list:
    res: list = []
    for v in l1:
        if v in l2 and v not in res:
            res.append(v)
    return res


# Programa principal
print(intersección([1, 2, 3, 2, 4], [2, 4, 8]))
