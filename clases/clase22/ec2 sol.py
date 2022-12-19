def suma_crecientes(l: list) -> list:
    resultado: list = []
    suma: int = l[0]
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            resultado.append(suma)
            suma = l[i]
        else:
            suma += l[i]
            
    resultado.append(suma)
    
    return resultado


# Programa principal
print(suma_crecientes([1, 3, 4, 2, 3])) # [8, 5]
print(suma_crecientes([1, 3, 4, 5])) # [13]
print(suma_crecientes([3, 2, 1])) # [3, 2, 1]
print(suma_crecientes([1, 1, 2, 3, 1, 2, 3, 2, 4])) # [7, 6, 6]