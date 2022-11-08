# --------- FUNCIONES -------------
def leer_lista(n: int) -> list:
    l: list = []
    for i in range(n):
        valor = int(input("Dime un valor: "))
        l.append(valor) # También vale l = l +[valor]
    return l


# --------- PROGRAMA PRINCIAL -------------
MAX_VALORES: int = 10
lista: list = leer_lista(MAX_VALORES)
print("La lista leída es:", lista)
