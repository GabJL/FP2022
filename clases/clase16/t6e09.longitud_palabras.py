# Funciones
def longitud_palabras(texto: str) -> list:
    t: list = texto.split()
    L: list = []
    for i in t:
        L.append(len(i))
    return L


# Programa principal
t: str = "Hola que tal estás? Aquí intentando hacer los ejercicios"
print(longitud_palabras(t))