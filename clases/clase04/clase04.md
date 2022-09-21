# Clase 04: 21 de septiembre de 2022

En la primera parte de la clase vimos algunos detalles sobre las cadenas de caracteres (string) y que operaciones podemos hacer. De especial interés es cómo acceder a una letra concreta dentro del texto completo mediante su posición.

Luego, empezamoe sl tema 3 donde comenzamos viendo cómo expresar condiciones y las variables booleanas o lógicas (tipo `bool`).

## Generando correos
*La UMA está pensando en autogenerar los correos de los alumnos y estápensando dos posible esquemas:*

* *Primera letra del nombre + un punto + primer apellido + 2 últimas cifras del añode nacimiento*
* *3 primeras letras del nombre + 3 primeras letras del primer apellido + 2 últimascifras del añode nacimiento.*

*Realice un programa que lea el nombre, el apellido y su año de nacimiento (como texto) y genere los dos posibles correos.*

En este ejercicio queremos practica las operaciones sobre cadenas (`str`):
* Para unir textos usamos `+`
* Para acceder a una letra usamos `[pos]`. Por ejemplo, la primera del nombre es `nombre[0]`. Recuerde que las posiciones se numeran empezando en 0.
* Para acceder a subcadenas usamos `[inicio:fin]`. Por ejemplo, los dos últimos de la año sería `año[-2:]` (año debe ser un texto) o las tres primeras del nombre es `nombre[:3]`. 

[[Ver Código](t2e09.correos.py)]

## Ejercicio 1: Evaluación de expresiones lógicas

En este ejercicio se inicializaban ciertas variables y luego se daban una serie de expresiones que usaban operadores lógicos (`and`, `or` y `no`) y había que decir si su evaluación daba verdadero (`True`) o falso (`False`). A continuación se facilita un código para probarlas, aunque la idea importante es saber porqué dan esos valores.

[[Ver código](t3e01.eval_exp_lógicas.py)]

## Ejercicio 2: Escribir expresiones lógicas

En este ejercicio se dan una serie de condiciones y se pide que se expresen en código Python.

[[Ver código](t3e02.escribir_exp_log.py)]