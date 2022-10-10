print("Introduce notas (acabe con una incorrecta): ")

aprobados: int = 0
suma: float = 0
nota: float = float(input("Nota: "))
mejor: float = nota
while nota >= 0 and nota <= 10:
    if nota >= 5:
        aprobados += 1
        suma += nota
    if nota > mejor:
        mejor = nota
    nota = float(input("Nota: "))
        
if aprobados == 0:
    print("No hay alumnos aprobados")
else:
    print("Hay", aprobados, "alumnos aprobados con nota media de ", suma/aprobados)
    
if mejor >= 0 and mejor <= 10:
    print("La mejor nota fue un", mejor)
else:
    print("No se introdujeron valores correctos")
