Salud: dict = {
  "Bioquímica estructural": [0.66, 0.61, 0.47, 0.64, 0.92, 0.92, 0.75],
  "Cálculo": [0.55, 0.52, 0.48, 0.29, 0.29, 0.06, 0.17],
  "Fundamentos de la programación": [0.58, 0.66, 0.53, 0.76, 0.7, 0.6, 0.49],
  "Física I": [0.23, 0.41, 0.38, 0.45, 0.37, 0.4, 0.56],
  "Álgebra lineal": [0.48, 0.44, 0.46, 0.54, 0.61, 0.41, 0.51]
}

for asignatura in Salud:
    tasas: list = Salud[asignatura]
    suma: float = 0
    for t in tasas:
        suma += t
    media: float = suma/len(tasas)
    print("La tasa media para", asignatura, "es", media)