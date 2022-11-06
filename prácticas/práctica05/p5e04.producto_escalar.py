def producto_escalar(l1: list, l2: list) -> int:
    prod_esc: int = 0
    for i in range(len(l1)):
        prod_esc += (l1[i]*l2[i])
    return prod_esc


# Programa principal
print(producto_escalar([1, 2, 3],[3, 2, 1]))