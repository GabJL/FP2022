altura: int = int(input("Dime la altura: "))

ast_inicio: int = 1
ast_final: int = altura
espacios: int = altura -1

for l in range(altura):
    for e in range(espacios):
        print(" ", end= "")
    for a in range(ast_inicio):
        print("*", end="")
    print("  ", end="")
    for a in range(ast_final):
        print("*", end="")
    print()
    espacios -= 1
    ast_inicio += 2
    ast_final -= 1