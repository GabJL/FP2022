def lee_películas(nombre_fichero: str) -> list:
    pelis: list = []
    f = open(nombre_fichero, encoding="utf8")
    for l in f:
        l = l.strip()
        if l[0] == "*":
            d = {
                    "nombre": l[1:],
                    "descripción": ""
                }
            pelis.append(d)
        else:
            pelis[-1]["descripción"] += l + " "
    f.close()    
    return pelis

def busca_pelicula(pelis: list, nombre: str) -> str:
    descripción: str = ""
    i: int = 0
    while i < len(pelis) and pelis[i]["nombre"] != nombre:
        i += 1
    if i < len(pelis):
        descripción = pelis[i]["descripción"]
    
    return descripción

# Programa principal
peliculas: list = lee_películas("cine2017.txt")
print(peliculas)
print(f"Coco: {busca_pelicula(peliculas, 'Coco')}")
print(f"Nemo: {busca_pelicula(peliculas, 'Nemo')}")