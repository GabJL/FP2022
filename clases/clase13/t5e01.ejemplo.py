def escribir_positivos(l: list) -> None:
  for v in l:
    if v > 0:
      print(v, end=" ")

def suma_lista(l: list) -> int:
  res = 0
  for v in l:
    res += v
  return res

# --------------- PRINCIPAL ---------------
lista:list = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

print(suma_lista(lista))

escribir_positivos(lista)