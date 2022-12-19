def unibles(s1: list, s2: list) -> bool:
    return (s1[1] > s2[0] and s1[1] < s2[1]) or (s2[1]  > s1[0] and s2[1] < s1[1])
        
def unir(s1: list, s2: list) -> list:
    min_seg = s1[0]
    if s2[0] < min_seg:
        min_seg = s2[0]
    max_seg = s1[1]
    if s2[1] > max_seg:
        max_seg = s2[1]
    return [min_seg, max_seg]
    
def simplificar(l: list) -> list:
    resultado: list = []
    while l != []:
        pos = 1
        while pos < len(l) and not unibles(l[0], l[pos]):
            pos += 1
        if pos < len(l):
            resultado.append(unir(l[0], l[pos]))
            l.remove(l[pos])
        else:
            resultado.append(l[0])
        l.remove(l[0])
    return resultado

# Programa principal
print(simplificar([[1,3], [2,4]])) # [[1,4]]
print(simplificar([[1,7], [9,15], [2,8]])) # [[1,8], [9,15]]
print(simplificar([[1,5], [2,4]])) # [[1,5]]
print(simplificar([[1,3], [7,9], [2,4], [6,8]])) # [[1,4], [6,9]]
