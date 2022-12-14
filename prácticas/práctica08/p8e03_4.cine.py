def lee_peliculas(nombre_fichero: str) -> dict:
    f = open(nombre_fichero)
    lista: list = []
    for linea in f:
        linea = linea.strip()
        if linea[0] == "*":
            res: dict = {
                "Nombre": linea[1:],
                "Descripcion": ""
            }
            lista.append(res)
        else:
            lista[-1]["Descripcion"] += linea

    f.close()
    return lista


def busca_pelicula(lista_peliculas: str, nombre: str) -> str:
    esta: bool = False
    descripción: str = ""
    i: int = 0
    while i < len(lista_peliculas) and not esta:
        if lista_peliculas[i]["Nombre"] == nombre:
            descripción = lista_peliculas[i]["Descripcion"]
            esta = True
        i += 1
    return descripción


# Programa Principal
peliculas = lee_peliculas("cine2017.txt")
print(busca_pelicula(peliculas, "Coco"))
print(busca_pelicula(peliculas, "Nemo"))
