# Ejercicio 3 del Tema 1
# Este programa dibuja un pentágono de lado 80 usando "turtle"

# Importamos el módulo "turtle" para poder usar sus operaciones
from turtle import *

# Variables / Constantes
número_lados: int = 5 # Cantidad de lados de la figura (valor entero)
lado: float = 80 # longitud de cada lado (valor real)
ángulo: float = 360 / número_lados # giro que hay que hacer tras cada lado (valor real)

# Lado 1
forward(lado) # Dibujamos el lado
left(ángulo) # Giramos para prepararnos para el siguiente lado

# El resto de lados es igual (hay que dibujar 3)
forward(lado)
left(ángulo)

forward(lado)
left(ángulo)

forward(lado)
left(ángulo)

# Añadimos el quinto lado
forward(lado)
left(ángulo)
