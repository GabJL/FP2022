def verParéntesis(texto: str) -> bool:
    contador: int = 0
    hay_negativos: bool = False
    i: int = 0
    while i < len(texto) and not hay_negativos:
        letra = texto[i]
        if letra == '(':
            contador += 1
        elif letra == ')':
            contador -= 1
        if contador < 0:
            hay_negativos = True
        i += 1

    return contador == 0 and not hay_negativos


# PROGRAMA PRINCIPAL --------------------------------
s = "(2+(3 - x) *4) /(3+ y)"
print(f"{verParéntesis(s)}: {s}") # True
s = "2+(3 -x) /3+ y)"
print(f"{verParéntesis(s)}: {s}") # False
s = "("
print(f"{verParéntesis(s)}: {s}") # False
