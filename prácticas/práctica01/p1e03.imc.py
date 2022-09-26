peso: float = float(input("Indique su peso (en kg): "))
altura: float = float(input("Indique su altura (en metros): "))

imc: float = peso/(altura**2)

print("Su IMC es", imc)