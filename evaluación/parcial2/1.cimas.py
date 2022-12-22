# Funciones
def cima(l: list) -> int:
    cimas = 0
    for i in range(1,len(l)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            cimas += 1
    return cimas

# Programa principal
print(cima([1, 2, 1, 3, 1, 5])) # -> 2
print(cima([1, 2, 3, 4]))       # -> 0