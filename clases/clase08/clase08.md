# Clase del 05 de octubre

En esta clase empezamoss el bucle `for` cuyo componente más importante es el rango sobre el que itera. Por ello, empezamos con algunos ejemplos en el que vamos configurando diferentes versiones del `range`. 

Una vez ya entendido el bucle `for` pasamos a realizar diferentes ejercicios típicos para practicar principalmente el bucle `for` aunque también se pueden hacer usando el `while` (incluso en algún caso se pueden hacer versiones indeterministas que sean más eficientes).


## Tabla del 7 (con for)
*El siguiente bucle while escribe la tabla de multiplicar del 7:*

```python
num = 1
while num <= 10:
  print("7 x", num, "=", 7*num)
  num += 1
```

*Modifique el código para usar el bucle for. Tenga en cuenta que `num` es una variable que toma los valores enteros 1, 2, 3, 4,..., 10*

Este ejercicio cuadra mucho con un `for`, lo único que hay que plantear es como generar esos valores. El `range` nos permite generar exactamente esos valores indicando que empiece en 1 y que llegue hasta 11 (sin incluirlo): `range(1,11)`.

[[Ver solución](t3e27.tabla7_for.py)]
## Ejercicios cortos de for
*Basándonos en el siguiente código:*

```python
for i in range(1,11):
  print(i, "->", i*i)
```

*Se piden realizar las siguientes modificaciones:*

### `for` hasta número leído de teclado
*Modifique el programa para que en vez de hacer un número fijo de iteraciones, le pida al usuario el número (N) y muestre todos los cuadrados entre el 1 y el número leído (incluído).*

En este caso, tras leer el valor, hay que hacer que el rango vaya hasta este valor y eso se hace cambiando el segundo parámetro que indica el límite superior. Cuidado que el valor indicado no se incluye en el rango y si queremos hacerlo hay que poner el rango hasta uno más: `range(1, N+1)`

[[Ver código](t3e28.cortos_for1.py)]

### `for` solo impares
*Modifique el programa anterior para que sólo muestre los cuadrados de los números impares (1, 3, 5, 7, ...).*

Aquí hay que modificar el paso para que en vez de ir de uno en uno vaya de 2 en 2: `range(1, N+1, 2)`

[[Ver código](t3e30.cortos_for3.py)]

### `for` con orden inverso
*Modifique el programa anterior para que muestre los cuadrados pero de manera inversa (N, N-1, N-2, ..., 1)*

En este caso, hay que modificar los tres parámetros del `range`:
* El inicio será `N`
* El final será `0` (esto escribe el 1 pero no el 0)
* El paso será `-1` para que vaya "bajando"

[[Ver código](t3e29.cortos_for2.py)]

### `for` con múltiplos de 2 o 3
*Modifique el programa anterior para que sólo muestre los cuadrados de los números que sean múltiplos de 2 o 3.*

En este caso no lo podemos controlar con el rango generado ya que no tiene un paso general y hay que controlarlo dentro del bucle escribiendo a veces y otras no:

[[Ver código](t3e31.cortos_for4.py)]

## Escribir 10 asteriscos
*Escribir por pantalla 10 asteriscos*

Sabemos escribir fácilmente un asterisco, pero hay que tener cuidado que como no queremos saltar de línea debemos indicarlo: `print("*", end="")`. Luego eso hay que repetirlo 10 veces y al saber cuántas veces se va a repetir lo más sencillo es utilizar el bucle determinista `for` (en la solución también se muestra con `while`). Lo que hay que conseguir que se repita 10 veces hay que crear una colección o rango de 10 valores (los valores realmente nos da igual). Por ejemplo, podemos usar: `range(10)`.

[[Ver código](t3e32.10asteriscos.py)]

## Sumar números
*Sumar todos los números hasta el 1000*

A diferencia del ejercicio anterior si estamos interesados en generar un rango concreto (los números del 1 al 1000). Eso es fácil con `range(1, 1001)` (recuerde que para que el 1000 esté en el rango debemos ir hasta el 1001). Luego, una vez tenemos los números que necesitamos sumarlos, para ello vamos a usar un acumulador. La forma de pensarla es lo siguiente:
* Imaginemos que ya hemos tratado 15 números (del 1 al 15), ¿de esos 15 números que información nos interesa tener? Lo que nos interesa realmente no son los números sino la suma de todos ellos => variable `suma`
* Muy bien, tenemos una variable que tiene la `suma` de todo lo anterior y tenemos un nuevo `número`, ¿cómo actualizamos las variables (especialmente la importante que es `suma`)? Pues simplemente la siguiente suma será la actual con el nuevo valor: `suma += número` (recuerde que eso es la forma compacta de `suma = suma + número`).
* Finalmente nos queda decir los valores iniciales de la variable, ¿cuánto vale la `suma` al inicio? Pues si no hemos tratado ningún número, la `suma` debe valer 0.

[[Ver código](t3e33.suma1000.py)]

## Factorial
*Realice un programa que lea un número y calcule el factorial. El factorial de un número n es n! = n*(n-1)*(n-2)*...*3*2*1. El factorial solo está definido para números positivos con el caso especial de que el factorial de 0 es 1 por definición (0! = 1).*

Bastante similar al ejercicio previo pero ahora hay que generar números del 1 al n (incluido) y en vez de sumarlos hay que multiplicarlos.

[[Ver código](t3e34.factorial.py)]

## Es primo
*Averiguar si un número dado es primo. Un número es primo si solo tiene como divisores al 1 y el mismo.*

En este caso la idea es generar todos los números entre 1 y el número y comprobar cuántos son divisores del número. Si hay más de dos, no será primo

[[Ver código](t3e35.primo1.py)]

Una solución más eficiente es ir de 2 al número/2 y en cuanto encuentre un divisor paro y digo que no es primo, si llego al final sí es primo. En este caso al ser un bucle indetermiista hay que emplear un bucle `while`:

[[Ver código](t3e36.primo2.py)]


## Es perfecto
*Averiguar si un número dado es perfecto. Un número es perfecto si la suma de sus divisores (sin incluirse) da el mismo número.*

Muy similar al anterior (la versión del `for`) pero en vez de contar, va acumulando y el bucle no incluye el valor leído.

[[Ver código](t3e37.perfecto.py)]

## Figuras

La idea de todos estos ejercicios es practicar los bucles anidados por lo que evitaremos utilizar cosas como `"*"*n`. En general:
* Tendremos un bucle externo que se encarga de dibujar las líneas
* De forma interna hay que pintar cada línea y actualizar las variables para cada línea.
* Hay que decidir qué forma cada línea. Por ejemplo la cuarta línea está formada por: muchos asteriscos + muchoes espacios + nuchos asteriscos + salto de línea:
  *  Muchos asteriscos: ```for i in range(num_asteriscos): print("*", end="")
  *  Muchos espacios: ```for i in range(num_espacios): print(" ", end="")
  *  Salto de línea: ```print()```
* Ahora hay que decidir como inicializar las variables que controlan los bucles y como cambian en cada línea. En el mismo ejemplo de antes:
  *  `num_asteriscos` empieza con 1 y cada vez que cambiemos de línea sumamos 1 (en cada lado)
  *  `num_espacios` empieza con 2\*n - 2 (si n es la altura) y cada línea se decrementa en 2

[[Ver código del cuadrado](t3e38.fig.cuadrado.py)]

[[Ver código del triángulo 1](t3e39.fig.triángulo1.py)]

[[Ver código del triángulo 2](t3e40.fig.triángulo2.py)]

[[Ver código del triángulo 3](t3e41.fig.triángulo3.py)]

[[Ver código del triángulo 4](t3e42.fig.triángulo4.py)]


