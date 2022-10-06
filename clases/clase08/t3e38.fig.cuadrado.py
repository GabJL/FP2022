n: int = int(input("Dime la altura: "))

num_asteriscos: int = n

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_asteriscos):
    print("*", end="")
  print()
