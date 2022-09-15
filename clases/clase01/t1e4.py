# Ejercicio 4 del Tema 1
# Este programa dibuja una espiral

# Importamos el módulo "turtle" para poder usar sus operaciones
from turtle import *

# Variables / Constantes
número_lados: int = 7 # Cantidad de lados de la figura (valor entero)
lado: float = 50 # longitud de cada lado (valor real)
ángulo: float = 90 # giro que hay que hacer tras cada lado (valor real)

forward(lado) # Dibujamos el lado
left(ángulo) # Giramos para prepararnos para el siguiente lado
forward(lado)
left(ángulo)

lado = lado + 50 # Cambiamos el tamaño del lado

forward(lado)
left(ángulo)
forward(lado)
left(ángulo)

lado = lado + 50 # Cambiamos el tamaño del lado

forward(lado)
left(ángulo)
forward(lado)
left(ángulo)

lado = lado + 50 # Cambiamos el tamaño del lado

forward(lado)
left(ángulo)
forward(lado)
left(ángulo)
