lado: int = int(input("Lado: "))

# Linea superior
for i in range(lado):
    print("*", end="")
print()

# Parte central
for lineas in range(lado-2):
    print("*", end="")
    for i in range(lado-2):
        print(" ", end="")
    print("*")

# Linea inferior
for i in range(lado):
    print("*", end="")
print()
