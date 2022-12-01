def ejercicio_con_read(filename: str) -> float:
    f = open(filename)
    todo: list = f.read()
    f.close()
    valores = todo.split()
    suma: float = 0
    for v in valores:
        suma += float(v)
    return suma


def ejercicio_con_for(filename: str) -> float:
    f = open(filename)
    suma: float = 0
    for l in f:
        valores: list = l.split()
        for v in valores:
            suma += float(v)
    f.close()
    return suma


nombre: str = input("Dime el nombre del fichero: ")
print("La suma (usando read) es", ejercicio_con_read(nombre))
print("La suma (usando for) es", ejercicio_con_for(nombre))