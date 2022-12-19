def lee_gastos(nombre_fichero: str) -> (float, float, float):
    suma: float = 0

    gastos: list = []
    f = open(nombre_fichero)
    for linea in f:
        for i in linea.split():
            gastos.append(float(i))

    maximo: float = gastos[0]
    minimo: float = gastos[0]

    for i in gastos:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
        suma += i
    media: float = suma / len(gastos)

    return media, minimo, maximo


# Programa principal
print(lee_gastos("gastos.txt"))