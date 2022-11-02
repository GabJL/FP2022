def hay_negativos(l: int) -> bool:
  i: int = 0
  while i < len(l) and l[i] >= 0:
    i += 1
  return i < len(l)

# --------------- PRINCIPAL ---------------
lista: list = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

if hay_negativos(lista):
  print(f"En la lista hay valores negativos")
else:
  print(f"La lista solo tiene valores positivos")
