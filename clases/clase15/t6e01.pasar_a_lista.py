def obtener_lista(texto: str) -> list:
    l: list = texto.split()
    l_num: list = []
    for v in l:
        l_num.append(float(v))
    return l_num


# ----- PROGRAMA_PRINCIPAL -----------
t: str = input("Dame muchos números: ")
l: list = obtener_lista(t)
print("Se han leído: ", l)