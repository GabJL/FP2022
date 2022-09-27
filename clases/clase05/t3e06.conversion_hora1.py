hora: int = int(input("Hora: "))

if hora < 12:
    valor: str = "am"
else:
    hora = hora - 12
    valor: str = "pm"

print("Son las", hora, valor)