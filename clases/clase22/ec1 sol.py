def coprimos(a: int, b: int) -> bool:
    son_coprimos: bool = True
    div: int = 2
    while div <= a and div <= b and son_coprimos:
        if a%div == 0 and b%div == 0:
            son_coprimos = False
        div += 1
    
    return son_coprimos


# Programa principal
print(coprimos(7, 15)) # True
print(coprimos(7, 14)) # False