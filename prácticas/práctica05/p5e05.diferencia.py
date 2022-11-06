def diferencia(a: list, b: list) -> list:
    l: list = []
    for v in a:
        if v not in b:
            l.append(v)
    return l


# Programa principal
print(diferencia([1, 2, 3, 4, 2, 8, 9], [1, 2, 9]))
