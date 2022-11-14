def cantidad_palabras(texto: str) -> int:
    lista: list = texto.split()
    return len(lista)


# ----- PROGRAMA_PRINCIPAL -----------
t: str = input("Di un texto: ")
print(f"El texto tiene {cantidad_palabras(t)} palabras")