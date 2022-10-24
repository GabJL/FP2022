def leer_números() -> float:
    contador_total: int = 0
    contador_positivos: int = 0
    num = int(input("Número: "))
    while num != 0:
        contador_total += 1
        if num > 0:
            contador_positivos += 1
        num = int(input("Número: "))
    if contador_total == 0:
        return 100
    else:
        return contador_positivos*100 / contador_total
    
porcentaje: float = leer_números()
print("Se leyeron ", porcentaje, "% de positivos")
    