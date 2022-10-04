MAX: int = 20

hay_vocales: bool = False # Aún no hemos encontrado ninguna vocal

num_veces: int = 0

while num_veces < MAX:
    letra = input("Dime una letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        hay_vocales = True
    num_veces += 1

if hay_vocales:
    print("Se ha leído alguna vocal")
else:
    print("No había vocales en el texto")