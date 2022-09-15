# Clase 01: 14 de septiembre de 2022

En esta clase se hizo la presentación de la asignatura. Este curso ha habido cambios importantes en la evaluación de la asignatura, por lo que se recomienda leerla, especialmente si se quiere intentar la evaluación continua sin examen final.

Tras eso se introdujeron conceptos básicos como 
* Algoritmo: conjunto de pasos que resuelven un problema, 
* Código fuente: es un algoritmo escrito en un lenguaje de programación
* Implementar: es el proceso de pasar el algoritmo a código fuente.

Luego se vieron algunos ejemplos de manera informal donde se presentaron conceptos como la secuencialidad, variables, comentarios, expresiones, bucles...

Los códigos de los ejercicios desarrollados se muestran a continuación

## Figura en forma de pirámide de números

Este es un ejemplo relativamente complicado que incluye muchos elementos que no veremos hasta el tema 3 (al menos). Únicamente se usa a modo de ejemplo de cosas que haremos en clase a lo largo del curso. Realmente no se espera que se entienda ahora, pero por si alguno quiere probarlo, os dejo el código:

[Ver Código](t1e0.py)

## Ejercicio de robot (con lenguaje natural)

Este ejercicio pide dar la secuencia de movimientos para mover un robot desde la posición (0,0) suponiendo que mira a la derecha hasta la (100, 100). Las operaciones a utilizar son avanzar X metros y girar a la izquierda Y grados. La idea del ejercicio es pensar qué movimientos hacer y ver que hay diferentes posibilidades para resolver un mismo problema. Por ejemplo algunas de las planteadas en clase fueron:

**Solucion 1:**
> Avanzar 100 metros
> 
> Girar 90 grados a la izquierda
> 
> Avanzar 100 metros

**Solucion 2:**
> Girar 90 grados a la izquierda
> 
> Avanzar 100 metros
> 
> Girar 270 grados a la izquierda
> 
> Avanzar 100 metros

**Solucion 3:**
> Girar 135 grados a la derecha
> 
> Avanzar 141.42

## Ejercicio 1: robot-tortuga (en Python)

Similar al ejercicio anterior pero ahora con las instrucciones que nos ofrece Python o la biblioteca `turtle`:
* `print(X)`: escribe el texto X por pantalla
* `forward(X)`: avanza y dibuja la tortuga X metros
* `left(X)\right(Y)`: gira a la izquierda\derecha Y ángulos

En este caso es prácticamente es convertir linea a línea la solución 1 a las instrucciones concretas que facilita el lenguaje. 

[Ver Código](t1e1.py)

## Ejercicio 2: robot-tortuga (en Python): Cuadrado

Basándonos en el código del ejercicio anterior ahora la idea es generar un cuadrado de lado 80 en el cuadrante positivo y dejando la tortuga orientada a la derecha. 

[Ver Código](t1e2.py)

Versión avanzada usando variables para evitar repetir un valor y que sea más sencillo cambiar el lado y ángulo.

[Ver Código](t1e3a.py)

Versión avanzada usando adicionalmente bucles.

[Ver Código](t1e3b.py)

## Ejercicio 3: robot-tortuga (en Python): Pentagono

Para dibujar un pentágono hay que cambiar el lado, el ángulo y repetir una vez más lo de dibujar un lado.

[Ver Código](t1e3.py)

## Ejercicio 4: robot-tortuga (en Python): Espiral

Aquí el ángulo vuelve a ser 90, pero el valor del tamaño del lado hay que cambiarlo cada cierto tiempo.

[Ver Código](t1e4.py)


