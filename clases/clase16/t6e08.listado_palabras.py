def listado_palabras(texto: str) -> str:
    lista: list = texto.split()
    new_text: str = " - ".join(lista)
    return new_text


# ----- PROGRAMA_PRINCIPAL -----------
t: str = input("Di un texto: ")
print(f"El texto tiene separado es: {listado_palabras(t)}")