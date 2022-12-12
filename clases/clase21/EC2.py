def sumaDiv(n: int) -> int:
    suma: int = 0
    for i in range(1,n):
        if n%i==0:
            suma+=i
    return suma

def esPerf(n: int) -> bool:
    es_perfecto: bool = False
    suma: int = sumaDiv(n)
    if n==suma:
        es_perfecto=True
    return es_perfecto
    # return n == sumaDiv(n) 

# Programa principal:
print(esPerf(6)) # True
print(esPerf(28)) # True
print(esPerf(29)) # False
print(esPerf(496)) # True