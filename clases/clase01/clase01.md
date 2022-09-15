# Clase 01: 14 de septiembre de 2022

En esta clase se hizo la presentación de la asignatura. Este curso ha habido cambios importantes en la evaluación de la asignatura, por lo que se recomienda leerla, especialmente si se quiere intentar la evaluación continua sin examen final (requiere realizar trabajo continuado a lo largo del curso).

Tras eso se introdujeron conceptos básicos como 
* **Algoritmo**: conjunto de pasos que resuelven un problema, 
* **Código fuente**: es un algoritmo escrito en un lenguaje de programación
* **Implementar**: es el proceso de pasar el algoritmo a código fuente.

Luego se vieron algunos ejemplos de manera informal donde se presentaron conceptos como la secuencialidad, variables, comentarios, expresiones, bucles...

Los códigos de los ejercicios desarrollados se muestran a continuación

## Figura en forma de pirámide de números

Este es un ejemplo relativamente complicado que incluye muchos elementos que no veremos hasta el tema 3 (al menos). Únicamente se usa a modo de ejemplo de cosas que haremos en clase a lo largo del curso. Realmente no se espera que se entienda ahora, pero por si alguno quiere probarlo, os dejo el código:

[Ver Código](t1e0.py)

## Ejercicio de robot (con lenguaje natural)

Este ejercicio pide dar la secuencia de movimientos para mover un robot desde la posición (0,0) suponiendo que mira a la derecha hasta la (10, 10). Las operaciones a utilizar son avanzar X metros y girar a la izquierda Y grados. La idea del ejercicio es pensar qué movimientos hacer y ver que hay diferentes posibilidades para resolver un mismo problema. Observe que el ejercicio no coincide totalmente con el enunciado de las transparencias. Por ejemplo algunas de las planteadas en clase fueron:

**Solucion 1:**
```
Avanzar 10 metros
Girar 90 grados a la izquierda
Avanzar 10 metros
```

**Solucion 2:**
```
Girar 90 grados a la izquierda
Avanzar 10 metros
Girar 270 grados a la izquierda
Avanzar 10 metros
```

**Solucion 3:**
```
Girar 135 grados a la derecha
Avanzar 14.142
```

Observe que hay diferentes soluciones y todas hacen lo que se pide en el ejercicio y se consideran correctas. Pero esto no tiene porqué ser siempre así. Una código que haga lo que se pida no tiene porque ser totalmente válido. Por ejemplo, aunque el siguiente código hace lo que se pide, no sería correcto totalmente:

**Solucion 4: (Incorrecta)**
```
Avanzar -10 metros
Avanzar 20 metros
Girar 90 grados a la izquierda
Avanzar 10 metros
```

## Ejercicio 1: robot-tortuga (en Python)

Similar al ejercicio anterior pero ahora con las instrucciones que nos ofrece Python o la biblioteca `turtle`:
* `print(X)`: escribe el texto X por pantalla
* `forward(X)`: avanza y dibuja la tortuga X metros
* `left(X)\right(Y)`: gira a la izquierda\derecha Y ángulos

En este caso es prácticamente es convertir linea a línea la solución 1 a las instrucciones concretas que facilita el lenguaje (de nuevo observe que el enunciado no corresponde totalmente con el enunciado de las transparencias). 

[Ver Código](t1e1.py)

## Ejercicio 2: robot-tortuga (en Python): Cuadrado

Basándonos en el código del ejercicio anterior ahora la idea es generar un cuadrado de lado 80 en el cuadrante positivo y dejando la tortuga orientada a la derecha. 

[Ver Código](t1e2.py)

Versión avanzada usando variables para evitar repetir un valor y que sea más sencillo cambiar el lado y ángulo.

[Ver Código](t1e2a.py)

Puede encontrar una explicación en el siguiente [vídeo](https://drive.google.com/file/d/1P3bCPyyhSbcXakGDfP9aREf0nd7l0B1n/view?usp=sharing) (también puede encontrar una versión avanzada usando bucles en este [vídeo](https://drive.google.com/file/d/1ctVIrjOlmCHxr6gybAtktecMyeczDZVG/view?usp=sharing)).

Versión avanzada usando adicionalmente bucles.

[Ver Código](t1e2b.py)

## Ejercicio 3: robot-tortuga (en Python): Pentagono

Para dibujar un pentágono hay que cambiar el lado, el ángulo y repetir una vez más lo de dibujar un lado.

[Ver Código](t1e3.py)

La solución anterior es sin bucles. La solución con bucle sería igual que la [última del ejercicio previo](t1e2b.py) pero cambiando la variable `número_lados` a 5.

## Ejercicio 4: robot-tortuga (en Python): Espiral

Aquí el ángulo vuelve a ser 90, pero el valor del tamaño del lado hay que cambiarlo cada cierto tiempo. Observe que para evitar usar valores fijos podemos hacer cosas como `lado = lado + 50` (esto le suma a `lado` 50 unidades).

[Ver Código](t1e4.py)

La variante con bucles en este caso es un poco diferente a las anteriores porque ahora la parte que se repite debe abarcar más instrucciones (hasta cambiar de lado)

[Ver Código](t1e4b.py)

