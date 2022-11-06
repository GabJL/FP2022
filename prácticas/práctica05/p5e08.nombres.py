def purga(l: list) -> list:
    res: list = []
    for v in l:
        if v not in res:
            res.append(v)
    return res


def limpiar(nombres: list) -> list:
    res: list = purga(nombres)
    res.sort()
    return res


def longitud_más_largo(nombres: list) -> int:
    max_long: int = len(nombres[0])
    for nombre in nombres:
        if len(nombre) > max_long:
            max_long = len(nombre)
    return max_long


def nombres_con_longitud(nombres: list, x: int) -> list:
    l: list = []
    for nombre in nombres:
        if len(nombre) == x:
            l.append(nombre)
    return l


# Programa principal
alumnos: list = ["Marwa", "Maha", "Inas", "Paula", "Ilyass", "Huasim", "Pablo", "Israe", "Julia", "Yussef", "Silvia",
                 "Carlos", "Esther", "José María", "Sergio", "Antonio", "Lucía", "José Mario", "Antonio", "Benjamín",
                 "Antonio", "Joncee Jomira", "Asmaa", "Iván", "Irene", "Andrea", "Aissa Omar", "Ghita", "Lucía",
                 "Lucía", "Antonio", "Natalia", "Laura", "Jimena", "Irene María", "Sara", "Marina", "Guillermo",
                 "María Jesús", "Adriana", "Carmen", "Francisco Javier", "Luis", "Alejandra", "Alejandro", "Paloma",
                 "Javier", "Celia", "Carlos", "Miguel", "Jaime", "Alberto", "Andrea", "Juan Ignacio", "Miguel Angel",
                 "María", "Gema", "Trinidad", "Miguel Angel", "Africa", "Hugo", "Antonio", "Javier", "Lucía",
                 "Alejandra"]

alumnos = limpiar(alumnos)

for i in range(longitud_más_largo(alumnos) + 1):
    l = nombres_con_longitud(alumnos, i)
    if l != []:  # len(l) > 0
        print(i, "->", l)


