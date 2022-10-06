n: int = int(input("Dime la altura: "))

num_asteriscos: int = 1
num_espacios: int = 2*n - 2

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_asteriscos):
    print("*", end="")
  for i in range(num_espacios):
    print(" ", end="")
  for i in range(num_asteriscos):
    print("*", end="")
  print()
  # Actualizamos las variables para la siguiente línea
  num_asteriscos += 1
  num_espacios -= 2
