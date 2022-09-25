velocidad: int = int(input("Indique la velocidad de descarga (en Mbps): "))
tamaño: int = int(input("Indique el tamaño del fichero a descargar (en MB): "))

tiempo: int = tamaño*8 // velocidad

print("El tiempo de descarga estimado es", tiempo, "segundos")