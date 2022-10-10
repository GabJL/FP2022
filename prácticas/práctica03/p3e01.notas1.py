MAX_NOTAS: int = 5

print("Introduce", MAX_NOTAS,"notas:")

aprobados: int = 0
for i in range(MAX_NOTAS):
  nota: float = float(input("Nota: "))
  if nota >= 5:
    aprobados += 1
    
print("Hay", aprobados, "alumnos aprobados")
