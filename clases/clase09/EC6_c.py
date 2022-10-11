inferior: int = int(input("Parte de abajo: "))
superior: int = int(input("Dime la parte de arriba: "))

#  Primera linea
for e in range((inferior-superior)//2):
    print(".", end="")
for a in range(superior):
    print("*", end= "")
print()

# Parte central
lineas: int =  (inferior-superior)//2 - 1
espacios1: int = (inferior-superior)//2 - 1
espacios2: int = superior
for l in range(lineas):
    for e in range(espacios1):
        print(".", end="")
    print("*", end="")
    for e in range(espacios2):
        print(".", end="")
    print("*", end="")
    print()
    espacios1 -= 1
    espacios2 +=  2
    
# Última linea
for i in range(inferior):
    print("*", end= "")
print()