número: int = int(input("Dime un número: ")) # Lectura previa al bucle

anterior: int = número
esta_ordenado: bool = True
while número != 0:
    # Hacer cosas con el número
    if número < anterior:
        esta_ordenado = False
    anterior = número
    número: int = int(input("Dime otro número: "))
    
if esta_ordenado:
    print("Está ordenado")
else:
    print("No está ordenado")