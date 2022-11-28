def decodificar_linea(peli):
    título, directores, actores, generos, resto = peli.split("#")
    directores = directores.split(", ")
    generos = generos.split(", ")
    actores = actores.split(", ")
    año, punt_imdb, duración, recaudado = resto.split()
    d = {
        "título": título,
        "directores": directores,
        "actores": actores,
        "géneros": generos,
        "año": int(año),
        "puntuación": float(punt_imdb),
        "duración": int(duración),
        "recaudación": float(recaudado)
    }
    return d

def leer_fichero(filename):
    fichero = open(filename)
    lista = []
    for línea in fichero:
        diccionario = decodificar_linea(línea)
        lista.append(diccionario)
    fichero.close()
    return lista

# Programa principal
l = leer_fichero("pelis.txt")

# 1.- Cantidad de películas
print("1.- En el fichero hay", len(l), "películas")
# 2.- Último genero de la película en la posición 6
print("2.- El último género de la película es", l[5]["géneros"][-1])

# 3.- Tres actores película en la posición 6
print("3.- Los tres actores de la película son", ", ".join(l[5]["actores"][:3]))

# 4.- ¿Cuántas películas hay posterior al 2000?
despues_2000 = 0
for p in l:
    if p["año"] > 2000:
        despues_2000 += 1
print("4.- Hay", despues_2000, "películas posterior a 2000")
# 5.- Cantidad de pelis con el género drama
pelis_drama = 0
for p in l:
    if "Drama" in p["géneros"]:
        pelis_drama += 1
print("5.- Hay", pelis_drama, "películas dramáticas")
# 6.- Duración de la más larga
mas_larga = l[0]
for p in l:
    if p["duración"] > mas_larga["duración"]:
        mas_larga = p
print("6.- La peli más larga dura", mas_larga["duración"])
# 7.- Título de la más larga
print("7.- La peli más larga es", mas_larga["título"])
# 8.- Más valorada según metascore
mejor = l[0]
for p in l:
    if p["puntuación"] > mejor["puntuación"]:
        mejor = p
print("8.- La mejor peli es", mejor["título"])
# 9.- Posición de Avengers: Endgame
peli = "Avengers: Endgame"
i = 0
while i < len(l) and l[i]["título"] != peli: i += 1
posicion = 1
for p in l:
    if p["puntuación"] > l[i]["puntuación"]:
        posicion += 1
print("9.- La posición de Avengers: Endgame es", posicion)
# 10.- Número de generos
géneros = []
for p in l:
    for g in p["géneros"]:
        if g not in géneros:
            géneros.append(g)
print("10.- Hay", len(géneros), "géneros")
# 11.- Más activo
actores = {}
for p in l:
    for a in p["actores"]:
        if a in actores:
            actores[a] += 1
        else:
            actores[a] = 1
actor = list(actores)[0]
for a in actores:
    if actores[a] > actores[actor]:
        actor = a
print("11.- El actor más activo es:", actor,"-", actores[actor])
# 12.- Más rentable
actores = {}
for p in l:
    if p["recaudación"] > 0:
        for a in p["actores"]:
            if a in actores:
                actores[a][0] += 1
                actores[a][1] += p["recaudación"]
            else:
                actores[a] = [1, p["recaudación"]]
actor = list(actores)[0]
rentabilidad = actores[actor][1]/actores[actor][0]
for a in actores:
    rentabilidad2 = actores[a][1]/actores[a][0]
    if rentabilidad2 > rentabilidad:
        actor = a
        rentabilidad = rentabilidad2
print("12.- El actor más activo es:", actor,"-", actores[actor])