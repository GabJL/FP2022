# Pedimos/leemos los datos (convirtiéndolos de forma oportuna)
distancia: int = int(input("Distancia: "))
tiempo_en_minutos: int = int(input("Tiempo: "))

# Calculamos la velocidad tras convertir el tiempo a horas
tiempo_en_horas: float = tiempo_en_minutos / 60
velocidad: float = distancia / tiempo_en_horas

# Escribimos el resultado
print("Velocidad media:", velocidad, "km/h")