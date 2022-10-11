altura: int = int(input("Dime la altura: "))

espacios: int = 2*altura - 2
asteriscos: int = 1
for l in range(altura):
    for e in range(espacios):
        print(".", end="")
    for a in range(asteriscos):
        print("*.", end="")
    print()
    espacios -= 2
    asteriscos +=  2
    
