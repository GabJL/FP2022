# Ejercicio 2 del Tema 1
# Este programa dibuja un cuadrado de lado 80 usando "turtle"

# Importamos el módulo "turtle" para poder usar sus operaciones
from turtle import *

# Variables / Constantes
número_lados: int = 4 # Cantidad de lados de la figura (valor entero)
lado: float = 80 # longitud de cada lado (valor real)
ángulo: float = 360 / número_lados # giro que hay que hacer tras cada lado (valor real)

for i in range(número_lados):
    forward(lado) # Dibujamos el lado
    left(ángulo) # Giramos para prepararnos para el siguiente lado
