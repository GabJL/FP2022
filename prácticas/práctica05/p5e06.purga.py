def purga(l: list) -> list:
    res: list = []
    for v in l:
        if v not in res:
            res.append(v)
    return res


# Programa principal
print(purga([3, 1, 3, 2, 2]))
