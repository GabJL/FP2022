MAX_NOTAS: int = 5

print("Introduce", MAX_NOTAS,"notas:")

aprobados: int = 0
suma: flota = 0
for i in range(MAX_NOTAS):
  nota: float = float(input("Nota: "))
  if nota >= 5:
    aprobados += 1
    suma += nota
        
if aprobados == 0:
  print("No hay alumnos aprobados")
else:
  print("Hay", aprobados, "alumnos aprobados con nota media de ", suma/aprobados)
