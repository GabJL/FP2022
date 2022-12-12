def esc(l1: list, l2: list) -> float:
    suma:int=0
    for i in range(len(l1)):
        suma+=l1[i]*l2[i]
    return suma


# Programa principal
print(esc([1.0, 2, 3] , [3, 2, 1])) # 10.0
print(esc([0, 1.1, 0, 2] , [-1, 10, 0, 2])) # 15.0