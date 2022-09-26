TASA: float = 25.0
PRECIO_HORA: float = 60.0

horas: float = float(input("Introduzca las horas por día trabajadas: "))
días: float = float(input("Introduzca los días trabajados: "))
total: float = horas * días * PRECIO_HORA
neto: float = total - TASA

print("El valor total a pagar es:", total)
print("El valor neto a pagar es:", neto)