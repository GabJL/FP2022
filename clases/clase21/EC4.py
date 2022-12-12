def lee_notas(nombre_fichero: str) -> dict:
    f = open(nombre_fichero, encoding="utf8")
    alumnos: dict = {}
    for linea in f:
        # Analiza la linea
        nombre, resto = linea.split(":")
        notas = resto.split(",")
        for i in range(len(notas)):
            notas[i] = float(notas[i])
        # Acumulo el resultado -> Meterlo en una lista, diccionario...
        alumnos[nombre] = notas
    f.close()
    return alumnos

def nota_media(notas: list) -> float:
    suma: float = 0
    for nota in notas:
        suma += nota
    return suma/len(notas)

def alumno_nota_mas_alta(alumnos: dict) -> str:
    nombres: list = list(alumnos)
    mejor_alumno = nombres[0]
    for alumno in alumnos:
        if nota_media(alumnos[alumno]) > nota_media(alumnos[mejor_alumno]):
            mejor_alumno = alumno
    return mejor_alumno

# Programa principal
alumnos: dict = lee_notas("notas.txt")
print(alumnos)
for al in alumnos:
    print(f"{al} -> {nota_media(alumnos[al])}")
print(alumno_nota_mas_alta(alumnos))