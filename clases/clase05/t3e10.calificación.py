nota: float = float(input("Dime la nota: "))

if nota < 5:
    print("Suspenso :(")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
elif nota < 10:
    print("Sobresaliente")
else:
    print("Matricula de Honor")