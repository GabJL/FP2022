def leer_datos(nombre_fichero: str, equipo: str) -> dict:
    futbolistas: dict = {}
    f = open(nombre_fichero, encoding="utf8")
    for linea in f:
        jornada, jug_eq, goles = linea.split(":")
        jug, eq = jug_eq.split("-")
        jug = jug.strip()
        eq = eq.strip()
        if eq == equipo:
            if jug in futbolistas:
                futbolistas[jug] += int(goles)
            else:
                futbolistas[jug] = int(goles)
    f.close()
    return futbolistas

def máximos_goleadores(goleadores: dict) -> list:
    max_goleadores: list = []
    max_goles = list(goleadores.values())[0]
    for k, v in goleadores.items():
        if v > max_goles:
            max_goles = v
    for k, v in goleadores.items():
        if v == max_goles:
            max_goleadores.append(k)
    
    return max_goleadores

# Programa principal
goleadores: list = leer_datos("futbol.txt", "Real Madrid")
print(goleadores)
print(máximos_goleadores(goleadores))