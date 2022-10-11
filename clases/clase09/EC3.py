
numeros: int = int(input('Ingresa números caballero: '))
contador: int = 0
mayor: int = 0

while numeros!=0:
    
    if numeros%5==0:
        contador +=1
        if numeros>mayor:
            mayor=numeros
    numeros: int = int(input('Ingresa números caballero: '))

print('Hay',contador,'números divisibles por 5 y el mayor es',mayor)