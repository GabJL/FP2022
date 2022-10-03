peso: float = float(input("Indique su peso (en kg): "))
altura: float = float(input("Indique su altura (en m): "))

imc: float = peso / altura ** 2

if imc < 16:
    información = "Ingrese en el hospital"
elif imc < 18:
    información = "Bajo peso"
elif imc < 25:
    información = "Peso normal (Saludable)"
elif imc < 35:
    información = "Sobrepreso"
else:
    información = "Obesidad"

print("Su IMC es:", imc, ":", información)
