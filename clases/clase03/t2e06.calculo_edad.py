edad: int = int(input("Edad en meses: "))

años: int = edad // 12 # Cociente de dividir entre 12 (sin decimales)
meses: int = edad % 12 # Resto de dividir entre 12

print("Tiene", años, "años y", meses, "meses")