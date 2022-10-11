altura: int = int(input("Dime la altura: "))

# Primera línea
for a in range(altura*2-1):
    print("*", end="")
print()

# Central
espacios1: int = 1
espacios2: int = 2*altura - 5
for l in range(altura-2):
    for e in range(espacios1):
        print(".", end="")
    print("*", end="")
    for e in range(espacios2):
        print(".", end="")
    print("*", end="")
    print()
    espacios1 += 1
    espacios2 -= 2
# Última línea
for e in range(altura -1):
    print(".", end="")
print("*")