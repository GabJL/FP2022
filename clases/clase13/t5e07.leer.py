MAX_VALORES: int = 10

# --------- FUNCIONES -------------
def leer_lista() -> list:
  l: list = []
  for i in range(MAX_VALORES):
    valor = int(input("Dime un valor: "))
    l.append(valor) # También vale l = l +[valor]
  return l

# --------- PROGRAMA PRINCIAL -------------
lista: list = leer_lista()
print("La lista leída es:", lista)
