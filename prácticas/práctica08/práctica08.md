# Práctica 8: Ficheros y repaso

## Ejercicio 1 (p8e01.gastos.py) 
*Se tiene un fichero `gastos.txt` con las cantidades gastadas en una larga serie de compras:*
```
614.1 542.2 590.7 703.8 282.1 180.9
356.8 333.8 14.31 686.3
861.1 979.8 71.38 967.6
291.8 54.6 690.2 933 642.9
87.78 656.3 160.1 539.3 329.5
790.7 137.2 282.9 204 317.2 399 508.9
725.2 45.24 157.6 645.2
545.8 58.9 196.2 722.3 266.9
```
*Se quiere saber cuál es la cantidad media de lo gastado, lo máximo y lo mínimo. Para ello desarrollar una función capaz de leer cualquier fichero de nombre recibido en un único parámetro con el nombre del fichero, y que devuelva los tres números reales: media, mínimo y máximo. Definir la función `def leeGastos(..)` que reciba el nombre del fichero en un parámetro, y que devuelva los tres valores anteriores, para que fuera de la función se puedan imprimir al final del programa. Los gastos son números reales que están separados por espacios en varias líneas. Para los datos previos saldría: `(439.3402500000001, 14.31, 979.8)`.*

[[Ver código](p8e01.gastos.py)]

## Ejercicio 2
*Vamos a desarrollar un único ejercicio (`p8e02.apuestas.py`) con varios apartados. Esto son los 3 primeros (de 4) ejercicios del examen final de septiembre de 2020, valiendo en total 7 puntos de los 10.*

**Apartado A (★★★✰✰)** 

*Un grupo de amigos realizan una apuesta sobre el resultado de un partido de fútbol. El fichero `apuestas.txt` aparecen las respuestas en la siguiente forma:*
```
luis miguel: 0 2
lola: 1 3
juan: 2 4
ana: 2 2
luis miguel: 2 1
lola: 1 6
```

*Donde se indica el nombre del amigo, el resultado y la apuesta. El resultado del partido podrá ser 0: empate, 1: gana casa, 2: gana visitante. Cada amigo puede hacer nuevas apuestas y por lo tanto puede aparecer en el fichero más de una vez. Hacer una función `def leeApuestas(nombFiche)` que lea este tipo de apuestas y devuelva una lista de diccionarios, donde cada diccionario tiene los campos de nombre del amigo (cadena), el resultado del partido (un entero), y la apuesta (un número real). En el ejemplo quedaría: `[{"nombre":"luis miguel", "resultado": 0, "apuesta": 2}, {"nombre":"lola", "resultado": 1, "apuesta": 3}, {"nombre":"juan", "resultado": 2, "apuesta": 4}, {"nombre":"ana", "resultado": 2, "apuesta": 2}, {"nombre":"luis miguel", "resultado": 2, "apuesta": 1}, {"nombre":"lola", "resultado": 1, "apuesta": 6}]`.*

*Cree el fichero de `apuestas.txt` con el contenido del ejemplo de antes. En el programa principal llame a esta función para que lea el fichero que ha creado y escriba por pantalla la lista resultante.*

**Apartado B (★★✰✰✰)**

*Realice una función que devuelva los totales apostados, y los apostados por los ganadores. La función recibirá como parámetros la lista de apuestas y el resultado del partido (0, 1 o 2): `def totalesApostados(apuestas, ganador)`. En el programa principal, llame a esta función e imprima en pantalla los dos resultados devueltos para los tres
casos: empate (0), gana casa (1) y gana visitante (2). Esta función en realidad es útil para el siguiente problema, aquí solo estamos comprobando que funciona correctamente. Para el ejemplo tendríamos que escribiría `(18.0, 2.0)` si el resultado es un empate, `(18.0, 9.0)` si gana el equipo de casa y `(18.0, 7.0)` si gana el visitante.*

**Apartado C (★★★★★)**

*Ahora añada la función `def impimePremios(apuestas, ganador)` que usará la función desarrollada en el apartado anterior para conocer el total apostado y el total de los ganadores. Con esos dos valores se calculará el `ratio` como total apostado / total de los ganadores.*

*Para imprimir los premios, se recorre la lista de las apuestas y si la persona ganó, se imprime su nombre y después la cantidad que apostó multiplicada por el `ratio`. Observe que una persona puede haber hecho varias apuestas al ganador y debe juntar sus premios (quizás para ello pueda usar un diccionario). Si no hay ningún ganador, se debe indicar que todos recuperan los apostado. En el ejemplo, la salida podría ser:*

*Si empatan:*
```
luis miguel GANA 18.0
```
*Si gana el equipo de casa:*
```
lola GANA 18.0
```
*Si gana el visitante:*
```
juan GANA 10.28571
ana GANA 5.142857
luis miguel GANA 2.571428
```

[[Ver código](p8e02.apuestas.py)]

## Ejercicio 3 (p8e03_4.cine.py) 

*Se tiene la información de las películas del año 2017 en un fichero `cine2017.txt` de forma que detrás del título, que está en una línea, se tiene un resumen en variaslíneas. La línea del título empieza por el carácter '*' y a continuación el resto de la línea es el título de la misma:*
```
*Coco
Aspiring musician Miguel, confronted with his family’s ancestral ban on music, enters the Land of
the Dead to find his great-great-grandfather, a legendary singer
*Tres anuncios en las afueras
A mother personally challenges the local authorities to solve her daughter’s murder when they fail
to catch the culprit.
*Blade Runner 2049
A young blade runner’s discovery of a long-buried secret leads him to track down former blade
runner Rick Deckard, who’s been missing for thirty years.
*Call Me by Your Name
In Northern Italy in 1983, seventeen year-old Elio begins a relationship with visiting Oliver, his
father’s research assistant, with whom he bonds over his emerging sexuality, their Jewish heritage,
and the beguiling Italian landscape. *Logan
In the near future, a weary Logan cares for an ailing Professor X, somewhere on the Mexican border.
However, Logan’s attempts to hide from the world, and his legacy, are upended when a young
mutant arrives, pursued by dark forces.
*Dunkerque
Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army,
and evacuated during a fierce battle in World War II.
```

*Hacer una o varias funciones para que llamando a la función `def leePeliculas (...)` reciba el nombre de un fichero como el que se pone de ejemplo (`cine2017.txt`) y nos devuelva una lista con registros (`dict`) cada uno con el `'nombre'` y la `'descripción'` de cada película que haya en el fichero. Fuera de esta función, guardar esa lista devuelta en una variable.*

[[Ver código](p8e03_4.cine.py)]

## Ejercicio 6 (p8e03_4.cine.py) 
*En el mismo fichero, ahora Hacer una función `def buscaPelicula( listaPeliculas, nombre)` que reciba el listado obtenido en el problema anterior y cualquier nombre de película en el segundo parámetro. La función devolverá la descripción de la película. Si la película no estuviera, devolverá una cadena vacía. Al final de nuestro programa python llamar a la función con la lista y la película de nombre, por ejemplo, `"Coco"` primero e imprimir la descripción que se nos devuelva. Imprimir también la descripción de una película que no esté, `"Nemo"`, por ejemplo. Usar el tipo de bucle adecuado para lo que es el proceso de una búsqueda.

[[Ver código](p8e03_4.cine.py)]

