n: int = int(input("Dime la altura: "))

num_espacios: int = n - 1
num_asteriscos: int = 1

# Triángulo superior
for linea in range(n):
    # Dibujamos la línea:
    # Primero espacios
    for i in range(num_espacios):
        print(" ", end="")
    # Luego asteriscos
    for i in range(num_asteriscos):
        print("*", end= "")
    # Y acabamos con un salto de línea
    print()
    # Ahora actualizamos los espacios y asteriscos para la siguiente línea
    num_espacios -= 1
    num_asteriscos += 2
    
# Triángulo superior
num_espacios += 2 
num_asteriscos -= 4

for linea in range(n):
    # Dibujamos la línea:
    # Primero espacios
    for i in range(num_espacios):
        print(" ", end="")
    # Luego asteriscos
    for i in range(num_asteriscos):
        print("*", end= "")
    # Y acabamos con un salto de línea
    print()
    # Ahora actualizamos los espacios y asteriscos para la siguiente línea
    num_espacios += 1
    num_asteriscos -= 2
