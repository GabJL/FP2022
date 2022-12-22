# Funciones
def sum_pol(p1: dict, p2: dict) -> dict:
    suma: dict = {}
    for g_p1 in p1:
        if g_p1 in p2:
            suma[g_p1] = p1[g_p1] + p2[g_p1]
        else:
            suma[g_p1] = p1[g_p1]
            
    for g_p2 in p2:
         if g_p2 not in p1:
             suma[g_p2] = p2[g_p2]
    return suma

def sum_pol2(p1: dict, p2: dict) -> dict:
    suma: dict = {}
    for g_p1 in p1:
        suma[g_p1] = p1[g_p1]
            
    for g_p2 in p2:
        if g_p2 not in p1:
            suma[g_p2] = p2[g_p2]
        else:
            suma[g_p2] += p2[g_p2]
    return suma
# Programa principal
# 3x^2 - 2 => {2:3, 0:-2}
# 5x^2 - x + 3 => {2:5, 1:-1, 0:3}

print(sum_pol2({2:3, 0:-2}, {2:5, 1:-1, 0:3})) # {2:8, 1:-1, 0:1}