# Funciones
def solo_numeros_y_sep(t: str) -> str:
    texto: str = ""
    for v in t:
        if v >= "0" and v <= "9":
            texto += v
        else:
            texto += " "
    return texto


def convertir_textos_a_num(lt: list) -> list:
    l: list = []
    for v in lt:
        l.append(float(v))
    return l


def sumar_lista(l: list) -> float:
    suma: float = 0
    for v in l:
        suma += v
    return suma


def suma_num_encontrados(t: str) -> float:
    t1: str = solo_numeros_y_sep(t)
    l: list = t1.split()  # Listado con palabras y cada palabra es un número
    l2: list = convertir_textos_a_num(l)
    suma: float = sumar_lista(l2)
    return suma


# Programa principal
texto: str = input("Dime un texto: ")
s: float = suma_num_encontrados(texto)
print(f"La suma de los números en el texto vale {s}")