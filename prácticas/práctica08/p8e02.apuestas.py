#  Funciones

def lee_apuestas(nomre_fichero: str) -> list:
    f = open(nomre_fichero)

    l:list = []
    for línea in f:
        nombre, números = línea.split(":")
        resultado, apuesta = números.split()
        dic: dict = {
            "nombre": nombre,
            "resultado": int(resultado),
            "apuesta": float(apuesta)
        }
        l.append(dic)

    f.close()

    return l


def totales_apostados(apuestas: list, ganador: int) -> (int, int):
    total: int = 0
    total_ganador: int = 0
    for ap in apuestas:
        total += ap["apuesta"]
        if ganador == ap["resultado"]:
            total_ganador += ap["apuesta"]
    return total, total_ganador


def imprime_premios(apuestas: list, ganador: int) -> None:
    tot, tot_gan = totales_apostados(apuestas, ganador)
    ratio: float = tot / tot_gan
    # Recopilamos las ganancias en un diccionario con pares nombre-ganancias
    dic: dict = {}
    for ap in apuestas:
        if ganador == ap["resultado"]:
            nombre: str = ap["nombre"]
            if nombre in dic:
                dic[nombre] += ap["apuesta"] * ratio
            else:
                dic[nombre] = ap["apuesta"] * ratio
    # Escribimos las ganancias
    for nombre in dic:
        print(f"{nombre} GANA {dic[nombre]}")


#  Programa principal
apuestas = lee_apuestas("apuestas.txt")
print("Probando la lectura de fichero:", apuestas)
print("Probando totales (0):", totales_apostados(apuestas, 0))
print("Probando totales (1):", totales_apostados(apuestas, 1))
print("Probando totales (2):", totales_apostados(apuestas, 2))
print("Probando la impresión (0):")
imprime_premios(apuestas, 0)
print("Probando la impresión (1):")
imprime_premios(apuestas, 1)
print("Probando la impresión (2):")
imprime_premios(apuestas, 2)
