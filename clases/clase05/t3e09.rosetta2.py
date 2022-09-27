# Lectura de valores
hora: int = int(input("Hora de la recepción: "))
minutos: int = int(input("Minutos de la recepción: "))

# Constantes
RETRASO: int = 24

# Cálculos de valores
# Valores más probables
dia: str = "hoy"

# Convertimos todo a minutos
minutos_totales: int = hora*60 + minutos - RETRASO

# Ajustamos si no son los valores probables
if minutos_totales < 0: # Cambio de día
  minutos_totales = minutos_totales + 60*24 # Sumamos un día entero para que sea positivo
  dia = "ayer"

# Reconvertimos los minutos a horas y minutos
horas_finales: int = minutos_totales // 60
minutos_finales: int = minutos_totales % 60

# Escritura de valores

# Ponemos 2 cifras siempre
if horas_finales < 10:
  horas_finales = "0" + str(horas_finales)
if minutos_finales < 10:
  minutos_finales = "0" + str(minutos_finales)
print("El mensaje fue enviadoa las ", horas_finales, ":", minutos_finales, " (", dia, ")", sep="")