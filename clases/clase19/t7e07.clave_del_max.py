def max_key_dict(d: dict) -> str:
    maximo: str = list(d)[0]
    for k in d:
        if d[k] > d[maximo]:
            maximo = k
    return maximo


# Programa principal
Málaga: dict = {"enero": 12, "febrero": 12, "marzo": 14, "abril": 16, "mayo": 19, "junio": 23, "julio": 26, "agosto": 26,"septiembre": 23, "octubre": 19, "noviembre": 15, "diciembre": 13}
Yakustk: dict = {"enero": -38, "febrero": -34, "marzo": -20, "abril": -5, "mayo": 8, "junio": 16, "julio": 20, "agosto": 15, "septiembre": 6, "octubre": -8, "noviembre": -27, "diciembre": -37}

print("Málaga:", max_key_dict(Málaga))
print("Yakustk:", max_key_dict(Yakustk))
