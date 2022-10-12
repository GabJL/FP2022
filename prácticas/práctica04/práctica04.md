# Práctica 4

Uso de sentencias de repetición (while y for) en python. 

## p4e01.orden.py (★✰✰✰✰) 
*Escriba un programa que lea de forma continua tres valores hasta que los tres números sean valores __estrictamente__ crecientes. Ejemplo:*

```
Diga tres números crecientes: 
20 
22 
19
Diga tres números crecientes: 
-1 
2 
2
Diga tres números crecientes: 
38 
50 
77
¡Gracias!
```

*__OBJETIVOS:__ Realizar un bucle indeterminista simple.*

[[Ver código](p4e01.orden.py)]

## p4e02.primo.py (★★★✰✰) 
*Escribir un programa que lea por teclado un número natural y muestre por pantalla Si el número es primo o no. Dos ejemplos:*

```
Introduce un número natural: 13
El número 13 es primo

Introduce un numero natural: 26
El número 26 no es primo
```

*__NOTA:__ La definición de un número primo es que solo es divisible entre 1 y sí mismo. Genere todos los otros posibles divisores (2, 3, 4, …, numero-1). Será primo si no encuentra nuevos divisores. Intente hacer una versión eficiente.*

*__OBJETIVOS:__ Uso del bucle `for` y contadores.*

[[Ver código](p4e02.primo.py)]

## p4e03.primos2.py (★★★★✰) 
*Haga una copia del programa del ejercicio anterior y modifícalo de la siguiente forma: lea dos valores y muestre todos los primos en el rango (no debe suponer que los valores estén ordenados). Ejemplo:*

```
Introduce dos valores: 10 2
Los primos en el rango son 2 3 5 7
```

*__NOTA:__ Tenga la precaución de a la hora de calcular si un número es primo o no (bucle interno) de reiniciar todas las variables que sean utilizadas por dicho proceso.*

*__OBJETIVOS:__ Bucle anidados.*

[[Ver código](p4e03.primos2.py)]

## p4e04.figura.py (★★✰✰✰) 
*Partiendo del código del ejercicio anterior, modifícalo de la siguiente forma: lea dos valores y muestre todos los primos en el rango (no debe suponer que los valores estén ordenados). Ejemplo:*

```
Lado: 5

XXXXX
X   X
X   X
X   X
XXXXX
```

*__OBJETIVOS:__ Bucles anidados y ser capaz de dividir el problema en partes y resolverlas por separado*

[[Ver código](p4e04.figura.py)]

## p4e05.suma_digitos.py (★★★★★) 
*Escribir un algoritmo que lea por teclado un número natural y muestre por pantalla la suma de todos sus dígitos. Ejemplo:*

```
Introduce un número natural: 12321
La suma de los dígitos es 9
```

*__NOTA:__ Las operaciones de división enteras son muy útiles para este caso:*
* *Puedo obtener un dígito de un número con el resto entre 10 (`%10` => `1234 % 10` es `4`).*
* *Una vez tratado el dígito puede eliminarlo con el cociente entero entre 10 (`//10` => `1234 // 10` es `1234`).*
* *Vaya quitando dígito a dígito y sumándolos y cuando el número que nos quede sea 0, ya habremos acabado.*

*__OBJETIVOS:__ Diseño de algoritmos con bucles que requieren pensar. Bucles cuya condición dependen de cálculos.*

[[Ver código](p4e05.suma_digitos.py)]
