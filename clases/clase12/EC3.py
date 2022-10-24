def es_par1(x: int) -> bool:
    par: bool = False
    if x%2 == 0:
        par = True
    return par

def es_par2(x: int) -> bool:
    if x%2 == 0:
        return True
    else:
        return False
    
def es_par3(x: int) -> bool:
    return x%2 == 0

# Programa principal
contador: int = 0
for i in range(10):
    número = int(input("Número: "))
    if es_par1(número):
        contador += 1
print("Se han leído", contador, "pares")