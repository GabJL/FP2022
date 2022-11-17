def obtener_primer_numero(texto: str) -> int:
    i: str = 0
    # Saltarnos las letras iniciales que no son un número
    while i < len(texto) and texto[i] not in "0123456789":
        i += 1

    # Cogemos el número
    numero: str = ""
    while i < len(texto) and texto[i].isdigit():
        numero += texto[i]
        i += 1

    return int(numero)


def obtener_primer_numero2(texto: str) -> int:
    t_num: str = ""
    for letra in texto:
        if letra >= "0" and letra <= "9":
            t_num += letra
        else:
            t_num += " "
    print(t_num)
    numeros: list = t_num.split()
    return int(numeros[0])


t: str = "Mañana a las -10.5 o a las 11-"
print(obtener_primer_numero2(t))
