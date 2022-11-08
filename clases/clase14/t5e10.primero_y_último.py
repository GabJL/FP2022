# --------- FUNCIONES -------------
def primero_y_último(l: list, valor: int) -> (int, int):
    first: int = -1
    last : int= -1
    for pos in range(len(l)):
        if l[pos] == valor:
            last = pos # Siempre actualizamos el último
        if first == -1: # Si el primero no lo hemos cambiado (vale -1) pues lo cambiamos solo esta vez
            first = pos
    return first, last


# --------- PROGRAMA PRINCIAL -------------
lista = [1, 3, 5, 8, 1, 2]
v = int(input("Dime un valor: "))
primer, último = primero_y_último(lista, v)
print("Con la lista", lista, "el valor", v, "aparece por primera vez en", primer,"y como última vez en", último)