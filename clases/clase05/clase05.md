# Clase 5 (27/09/2022)

En esta clase vemos la estructura de control selectiva que nos permitirá decidir si un código se ejecuta o no atendiendo a una condición.

## Ejemplo 1: Ecuación de segundo grado

Se muestra como ejemplo un código básico para resolver una ecuación de orden 2. Esta solución se indica que puede tener posibles problemas si se aplica la raíz cuadrada a un número negativo (aunque Python maneja de forma nativa los números complejos con el tipo `complex`) o si se intenta dividir entre 0, si a vale 0 (esto si es provoca un error). Esto demuestra que para ejecutar ciertos códigos, primero sus componentes deben cumplir ciertas condiciones

[[Ver código](t3e03.ec_grado2.py)]

## Ejemplo 2: Valor absoluto

Como ejemplo de uso de la sentencia de selección simple, se muestra el código del valor absoluto que debe cambiar el signo si el número es negativo pero no hacer nada si es positivo.

[[Ver código](t3e04.absoluto.py)]

## Ejemplo 3: Positivo o negativo

Como próximo ejemplo se muestra un código que clasifica el número leído en positivo (incluyendo al 0) o negativo. Para esto es necesario utilizar una sentencia de selección binaria donde el mensaje puede ser uno entre dos posibles

[[Ver código](t3e05.pos_o_neg.py)]

## Ejercicio 1: Menor de dos valores

En este caso se muestran varias alternativas para calcular el menor de dos números leídos de teclado. Todos son correctos, pero hay algunos mejores que otros:

Uno de los código a evitar es:

```python
if a < b:
  b = a
else:
  b = b
print("El menor es:", b)
```

El principal problema de este código es que usa `b = b` que realmente es código que no hace nada y no debería utilizarle.

Otro código poco recomendable es:

```python
if a < b:
  print("El menor es:", a)
else:
  print("El menor es:", b)
```

En este caso repite el `print` en ambas opciones del `if`, lo cual no es recomendable. Si hay partes comunes, lo mejor es evitar repeticiones y sacarlo fuera (antes o después del `if ` atendiendo a la necesidad) y solo ponerlas una vez.

El resto de soluciones son adecuadas y quizás dependiendo del caso podría convenir una más que otra.

# Ejercicio 2: Hora

Realice un programa que pregunte la hora en formato 24h y nos devuelva esa misma hora en formato am/pm. am (Ante meridiem) representa las 12 primeras horas del día y pm (Post meridiem) las últimas 12 horas. 

Aunque se pueden considerar más situaciones, en este caso hay dos posibles casos diferenciados:
* Menor de 12: las horas no cambian y se pone "am"
* Mayor o igual de las 12: a las horas se les resta 12 y se pone "pm"

Con lo visto hasta el momento este ejercicio hay que hacerlo con `if` y `else`:

[[Ver código](t3e06.conversion_hora1.py)]

Aunque también se puede hacer con un `if` simple

[[Ver código](t3e06.conversion_hora2.py)]

## Ejercicio 3: Año bisiesto

*Según la Wikipedia un año es bisiesto si "es divisible entre 4, a menos que sea divisible entre 100. Sin embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta bisiesto."*

*Escriba un programa que dado un año, indique si es bisiesto o no.*

Primero debemos recordar cómo se indicaba la divilidad en python. Usaremos la definición de que b divide a si al hacer la división entre a/b no da de resto 0 (es decir la división da un cociente entero). Eso en python se pone como `a%b == 0`.

Una vez sabido eso es ver como plantear lo que dice el enunciado. Si observamos bien este código plantea 3 posibilidades
* Si es divisible entre 4 y no entre 100 => Bisiesto
* Si es divisible entre 100 y también entre 400 => En este caso si comprobamos solo entre 400 ya se validan ambas de un tirón => Bisiesto
* Resto de casos => No bisiesto

Las dos primeras se podrían unir en una única condición unidas con el operador `or` o ponerlas como casos diferentes en un `if` múltiple. En la siguiente solución se ofrece la priemra alternativa:

[[Ver Código](t3e07.bisiesto.py)]

## Ejercicio 4: Menor de tres números

*Realiza un programa que lea 3 números y diga cuál es el menor (use solo condiciones simples, sin and/or)*

Este ejercicio se ha propuesto para que lo hagáis por vuestra cuenta y además en la práctica se hará uno similar. En todo caso, a continuación se facilita el código:

[[Ver Código](t3e08.menor_de_3.py)]

## Ejercicio 5: Sonda Rosetta:

*Un problema al que se enfrentan los ingenieros para el control remoto de estas sondas es que los mensajes sufren un enorme retraso debido a las distancias. Por ejemplo, las comunicaciones entre la tierra y la sonda Rosetta tenían un retraso de 24 minutos. Se nos solicita que se realice un programa que lea la hora de
recepción de un mensaje (hora y minutos) y nos diga la hora en la que fue enviado y si fue en el mismo día o el anterior.*

Este se mando en la actividad de la semana 3. Existen múltiples soluciones, voy a plantear una sencilla con `if` anidados:

[[Ver Código](t3e09.rosetta.py)]

Como alternativa también se muestra otra solución con un `if` simple:

[[Ver Código](t3e09.rosetta2.py)]

## Ejercicio 6: Calificación

*Pasar de calificación numérica a texto*

Esto aparece en las transparencias como ejemplo, pero ya que de las transparencias se puede copiar peor y por completitud, también lo pongo aquí.

[[Ver Código](t3e10.calificación.py)]

## Ejercicio 7: Generación

*Realice un programa que lea el año de nacimiento y diga a qué generación perteneces de acuerdo a la siguiente tabla:*

| Años | Generación |
| ---- | ---- |
| < 1946 | No considerados |
| 1946 - 1961 | Baby Boomer |
| 1962 - 1980 | Generación X |
| 1981 - 1996 | Generación Y (millenials) |
| 1997 - 2010 | Generación Z |
| \> 2010 | Generación T (táctil) |

Este es muy parecido al ejemplo anterior. Y de nuevo, lo importante es utilizar el conocimiento y en vez de usar cosas como `elif 1946 <= año and año <= 1961:` y poner cosas como `elif año <= 1961:` aprovechando el conomiento de que las condiciones previas son falsas.

[[Ver Código](t3e11.generación.py)]