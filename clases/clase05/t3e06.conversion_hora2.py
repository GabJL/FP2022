hora: int = int(input("Hora: "))

valor: str = "am"
if hora >= 12:
    hora = hora - 12
    valor: str = "pm"

print("Son las", hora, valor)