# Lectura de valores
hora: int = int(input("Hora de la recepción: "))
minutos: int = int(input("Minutos de la recepción: "))

# Constantes
RETRASO: int = 24

# Cálculos de valores
# Valores más probables
dia: str = "hoy"
minutos_finales: int = minutos - RETRASO
horas_finales: int = hora

# Ajustamos si no son los valores probables
if minutos_finales < 0: # Cambio de hora
  horas_finales -= 1 # Reducimos la hora
  minutos_finales += 60 # Ajustamos los minutos de forma apropiada
  if horas_finales < 0: # Cambio de día
    horas_finales = 23
    dia = "ayer"

# Escritura de valores

# Ponemos 2 cifras siempre
if horas_finales < 10:
  horas_finales = "0" + str(horas_finales)
if minutos_finales < 10:
  minutos_finales = "0" + str(minutos_finales)
print("El mensaje fue enviadoa las ", horas_finales, ":", minutos_finales, " (", dia, ")", sep="")