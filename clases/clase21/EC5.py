def leer_secuencias(nombre_fichero: str) -> dict:
    f = open(nombre_fichero, encoding="utf8")
    secuencias: dict = {}
    for linea in f:
        # Analizar linea y añadir a secuencias
        linea = linea.strip()
        if linea[0] == ">":
            # nombre
            nombre: str = linea[1:]
            secuencias[nombre] = ""
        else:
            # secuencia
            secuencias[nombre] += linea
    f.close()
    return secuencias


def tienen_secuencia(secuencias: dict, subsec: str) -> list:
    lista: list = []
    for nombre, secuencia in secuencias.items():
        if subsec in secuencia:
            lista.append(f"{nombre} -> {secuencia}")
    return lista


# Programa principal
seqs: dict = leer_secuencias("seq.txt")
print(seqs)
print(tienen_secuencia(seqs, "AAGG")) # ['Glaucocystis', 'Macrocystis pyrifera']

