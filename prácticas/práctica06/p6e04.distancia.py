def distancia(cadena: str, a: str) -> int:
    primero: int = -1
    último: int = -1
    for i in range(len(cadena)):
        if cadena[i] == a:
            último = i
            if primero == -1:
                primero = i
    if primero == último:
        dist = -1
    else:
        dist = último - primero
    return dist


sec: str = "ATCCATTACGA"
print(distancia(sec, "C"))