nombre: str = input("Nombre: ")
apellido: str = input("Apellido: ")
edad_nacimiento: str = input("Edad de nacimiento: ")

correo1: str = nombre[0] + "." + apellido + edad_nacimiento[-2:] + "@uma.es"
correo2: str = nombre[:3] + apellido[:3] + edad_nacimiento[-2:] + "@uma.es"
"""
Algunas observaciones:
* nombre[:3] es equivalente nombre[0:3] o lo que es lo mismo: nombre[0] + nombre[1] + nombre[2]
* edad_nacimiento[-2:] son las dos últimas letras de la edad  
"""

print("Correos:", correo1, "y", correo2)