# Con el end forzamos los dos saltos
print("Hola Gabriel!", end="\n\n") 

# En este caso como por defecto el print añade un salto y en el texto pongo manualmente otro, tengo los dos saltos
print("Este es mi primer programa en Python ... de este tema\n") 

horas: int = 0
minutos: int = 21
# En este caso los dos saltos los logro con 2 print que cada uno hace uno (en el siguiente no escribo nada, solo el salto).
print("Han pasado", horas*3600 + minutos*60,"segundos desde el inicio de clase", end="\n\n")
print()
