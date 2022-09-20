# Clase 03: 19 de septiembre de 2022

En esta clase continuamos viendo el tema 2 con varios conceptos como qué es una biblioteca o módulo (y como importarla), comentarios y cómo leer de teclado (`input`). 

La mayoría de algoritmos básicos tendrán la siguiente estructura:

```python
# Pedir datos 
"""
Lo que se muestra a continuación es una plantilla de lectura:
* Cambiaremos variable por el nombre apropiado según lo que vayamos a leer
* tipo lo cambiaremos al apropiado (int, float, str...)
    * Si el tipo es str, la conversión no es necesaria, es decir podría simplificarse a :
    * variable: str = input("mensaje")
* mensaje es lo que queremos escribir para informar al usuario de qué debe escribir 
"""
variable: tipo = tipo( input ("mensaje") )  

# Calculo
resultado: tipo = Expresión

# Mostrar al usuario los resultados
print("mensaje", resultado, "quizás más texto")
```
## Conversión de grados

Este ejercicio viene detallado en las transparencias los pasos seguidos y nos sirve como problema modelo para ver qué pasos hay que hacer a la hora de programar en python.

[[Ve código](t2e03.conversion.py)]

## Cálculo de la velocidad media

Este ejercicio es similar al anterior donde debemos leer los datos (en este caso 2 valores en vez de 1), hacer un cálculo simple (aquí la dificultad añadida es que antes de hacer el cálculo hay que convertir los datos a las unidades correctas) y finalmente escribir el resultado.

[[Ve código](t2e04.velocidad.py)]

## Precio Sin IVA

*Una práctica popular de los centros comerciales para aumentar sus ventas es promocionar días en los que se desquita el IVA (21%).*

*Realice un programa que recibiendo el precio normal (con IVA) nos diga cuál será el precio rebajado. NOTA: el IVA defínalo como constante.*

Este ejercicio inicialmente parece simple pero hay que pensar en detalle la solución ya que quizás no es tan obvia como parece. Si por ejemplo, un objeto vale 100 euros sin IVA, con el IVA será 121 euros. Pero si a ese producto de 121 euros le calculo el 21% sale 25,41 euros y si lo desquito sale 95,59 que no es el precio original. El calculo real lo podemos pensar `Precio_con_IVA = Precio_sin_IVA + Precio_sin_IVA*0.21` si despejamos de forma adecuada queda `Precio_sin_IVA = Precio_con_IVA/1.21`

Otros detalles importantes a tener en cuenta:
* Al leer convierta a real por si tiene decimales (`precio = float(input(...))`).
* Recuerde que los decimales si ponen con punto, es decir, 0.21 es correcto pero 0,21 no lo es.

[[Ver Código](t2e05.siniva.py)]

## Cálculo de la edad
*Es habitual que cuando se pregunta la edad de un niño pequeño se responda con la cantidad de meses y es complicado saber la edad en añosdel bebé."

*Realice un programa que reciba los meses y nos diga la edad real en años y meses del niño.*

En este caso el problema es como separar por ejemplo 28 meses en 2 años y 4 meses. Para eso podemos hacer uso de la división entera (`//`) ya que `28//12 = 2` y el resto ya que  `28%12 = 4`.

[[Ver Código](t2e06.calculo_edad.py)]

## Pulgada a centímetros (Relación del Tema 2 - Ejercicio 5)
*Hacer  un  programa  que  pida  una  longitud  en  pulgadas  y  la  imprima  en  centímetros  (1in  =  2.54cm)*

Este ejercicio es bastante sencillo y parecido a los realizados la semana pasada.
 
[[Ver Código](t2e07.inch2cm.py)]

## Hipotenusa (Relación del Tema 2 - Ejercicio 6)
*Pedir  los  catetos  de  un  triángulo  rectángulo  y  e  imprimir  su  hipotenusa  (Teorema  de Pitágoras: 𝑎^2 +𝑏^2 =𝑐^2). Para calcular la raíz cuadrada recordar que hay que importar math (`import math`) y llamar a `math.sqrt(valor)`, o también usando `valor**0.5`*

También es un ejercicio cuyo objetivo es practicar expresiones aritméticas. Solo tenga en cuenta:
* Que debe usar paréntesis para imponer en el orden que quieres hacer las operaciones
* La raiz cuadrada la puede tanto con `**0.5` como con `math.sqrt`. En la solución se muestran ambas alternativas.

[[Ver Código](t2e08.hipotenusa.py)]
