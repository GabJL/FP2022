# Posibilidad 1: Como lista
def max_list(l: list) -> int:
    maximo: int = l[0]
    for v in l[1:]:
        if v > maximo:
            maximo = v
    return maximo


# Posibildiad 2: Como diccionario
def max_dict(d: dict) -> int:
    clave: str = list(d)[0]
    maximo: int = d[clave]
    for k in d:
        if d[k] > maximo:
            maximo = d[k]
    return maximo


# Programa principal
Málaga: dict = {"enero": 12, "febrero": 12, "marzo": 14, "abril": 16, "mayo": 19, "junio": 23, "julio": 26, "agosto": 26,"septiembre": 23, "octubre": 19, "noviembre": 15, "diciembre": 13}
Yakustk: dict = {"enero": -38, "febrero": -34, "marzo": -20, "abril": -5, "mayo": 8, "junio": 16, "julio": 20, "agosto": 15, "septiembre": 6, "octubre": -8, "noviembre": -27, "diciembre": -37}

# Posibilidad 1: Como lista
l_málaga: list = list(Málaga.values())
l_yakustk: list = list(Yakustk.values())
print("Málaga:", max_list(l_málaga))
print("Yakustk:", max_list(l_yakustk))

# Posibildiad 2: Como diccionario
print("Málaga:", max_dict(Málaga))
print("Yakustk:", max_dict(Yakustk))
