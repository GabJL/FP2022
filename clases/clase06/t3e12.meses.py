mes: str = input("Dime el mes ")

if mes == "febrero":
    dias = 28
elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
    dias = 30
else:
    dias = 31

print("El mes", mes, "tiene", dias, "días")