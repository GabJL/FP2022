from json import load

f = open("songs.txt", encoding="utf-8")
SONGS = load(f)

f.close() 

# 1
print("1.- Título de la canción 79:", SONGS[78]["track_name"])
# 2
print("2.- Mejor puesto de la última canción:", SONGS[-1]["peak_rank"])
# 3
print("3.- Segundo cantante de la segunda canción:", SONGS[1]["artist_names"][1])
# 4
print("4.- Cantidad de canciones:", len(SONGS))
# 5
tiempo: int = 0
for s in SONGS:
    tiempo += s["duration_ms"]
tiempo = tiempo // 1000
print("5.- Tiempo en segundo:", tiempo)
print(f"5.- Tiempo: {tiempo//3600}:{(tiempo%3600)//60}:{tiempo%60}")
# 6
canciones_vivo: int = 0
for s in SONGS:
    if s["liveness"] > 0.6:
        canciones_vivo += 1
print("6.- Cantidad de canciones en vivo: ", canciones_vivo)
# 7 
energia: float = 0
cantidad: int = 0
for s in SONGS:
    if "ROSALÍA" in s["artist_names"]:
        cantidad += 1
        energia += s["energy"]
print(f"7.- Energía media de las canciones de ROSALIA: {energia/cantidad:.2f}")
# 8
mas_cantantes: dict = SONGS[0]
for s in SONGS:
    if len(s["artist_names"]) > len(mas_cantantes["artist_names"]):
        mas_cantantes = s
print("8.- La que tiene más cantantes:", mas_cantantes["track_name"],len(mas_cantantes["artist_names"]))
# 9
corta = SONGS[0]
for s in SONGS:
    if s["duration_ms"] <= corta["duration_ms"]:
        corta = s
print("9.- La más corta:", corta["track_name"],corta["duration_ms"]//1000)
# 10
artistas = []
for s in SONGS:
    for cantante in s["artist_names"]:
        if cantante not in artistas:
            artistas.append(cantante)
print("10.- Cantidad de artistas:", len(artistas))
# 11
print("11.- 10 últimos artistas:", ":-:".join(artistas[-10:]))
# 12
canciones_por_cantante = {}
for cantante in artistas:
    canciones_por_cantante[cantante] = 0
    for s in SONGS:
        if cantante in s["artist_names"]:
            canciones_por_cantante[cantante] += 1
print("12.- Cantidad de canciones de Imagine Dragons:", canciones_por_cantante["Imagine Dragons"])
# 13
cantante_max = artistas[0]
canciones = canciones_por_cantante[cantante_max]
for gen, can in canciones_por_cantante.items():
    if can > canciones:
        cantante_max = gen
        canciones = can
print("13.- El cantante con más canciones:", cantante_max, canciones)
