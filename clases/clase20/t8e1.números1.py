def ejercicio_con_read(filename: str) -> float:
    f = open(filename)
    todo: str = f.read()
    f.close()
    valores: list = todo.split()
    suma: float = 0
    for v in valores:
        suma += float(v)
    return suma


def ejercicio_con_readlines(filename: str) -> float:
    f = open(filename)
    lineas: list = f.readlines()
    f.close()
    suma: float = 0
    for v in lineas:
        suma += float(v)
    return suma


def ejercicio_con_readline(filename: str) -> float:
    f = open(filename)
    suma: float = 0
    linea: list = f.readline()
    while linea != "":
        suma += float(linea)
        linea = f.readline()
    f.close()
    return suma


def ejercicio_con_for(filename: str) -> float:
    f = open(filename)
    suma: float = 0
    for l in f:
        suma += float(l)
    f.close()
    return suma


nombre: str = input("Dime el nombre del fichero: ")
print("La suma (usando read) es", ejercicio_con_read(nombre))
print("La suma (usando for) es", ejercicio_con_for(nombre))
print("La suma (usando readlines) es", ejercicio_con_readlines(nombre))
print("La suma (usando readline) es", ejercicio_con_readline(nombre))
