# --------- FUNCIONES -------------
def crear_frecuencias() -> list:
    f: list = []
    for i in range(11):
        f.append(0)
    return f


def escribir_frecuencias(f: list) -> None:
    for i in range(11):
        print(i, "->", f[i])


# --------- PROGRAMA PRINCIAL -------------
nota: int = int(input("Dime una nota: "))
frecuencias: list = crear_frecuencias()

while nota != -1:
    frecuencias[nota] += 1
    nota: int = int(input("Dime otra nota: "))

escribir_frecuencias(frecuencias)