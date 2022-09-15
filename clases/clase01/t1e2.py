# Ejercicio 2 del Tema 1
# Este programa dibuja un cuadrado de lado 80 usando "turtle"

# Importamos el módulo "turtle" para poder usar sus operaciones
from turtle import *

# Lado 1
forward(80) # Dibujamos el lado
left(90) # Giramos para prepararnos para el siguiente lado

# El resto de lados es igual (hay que dibujar 3)
forward(80)
left(90)

forward(80)
left(90)

forward(80)
left(90) # El último giro no es necesario pero no pasa nada si lo hacemos
