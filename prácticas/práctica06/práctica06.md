# Práctica 6

## p6e01.edad.py (★★✰✰✰) 
*Realice una función `def escribir_vida(t: str) -> str` que reciba una línea de teclado con el formato: `nombre: año_nac, edad_muerte` y nos devuelva el texto: `nombre vivió desde X hasta Y`. Use split para dividir la línea y forme la línea resultante usando f-strings.*

[[Ver Código](p6e01.edad.py)]

## p6e02.palabra_mas_larga.py (★★★✰✰) 
*Hacer una función def `palabra_mas_larga(t: str) -> str` que recibiendo un texto con muchas palabras (al menos una) nos devuelva la palabra más larga del texto.*

[[Ver Código](p6e02.palabra_mas_larga.py)]

## p6e03.primer_numero.py (★★★★✰) 
*Hacer una función `def primer_numero(t: str) -> int ` que reciba una cadena como la siguiente: `"Mañana a las -10.5 o a las 11-"` y que devuelva el primer número entero que encuentre en ella, en el ejemplo: `10`.*

[[Ver Código](p6e03.primer_numero.py)]

## p6e04.distancia.py (★★★★✰) 
*Hacer una función `def máxima_distancia(seq: str, nuc: str) -> int` que dada una secuencia de aminoácidos devuelva la mayor distancia entre dos posiciones del nucleótido pasara por parámetro. Resuélvalo haciendo un único recorrido por la palabra. Por ejemplo:*

*	*Para `"ATCCATTACGA"` y `"C"` devolvería 5*
*	*Para `"AA"` y `"A"` devolvería 1*
*	*Para `"A"` y `"A"` devolvería -1*
*	*Para `"CT"` y `"A"` devolvería -1*

[[Ver Código](p6e04.distancia.py)]

## p6e05.sufijo.py (★★★★★) 
*Hacer un programa que reciba dos secuencias de aminoácidos y nos indique el solapamiento entre ellas. Se define el solapamiento como el número de aminoácidos del final de la primera secuencia que son iguales que el inicio de la segunda. Algunos ejemplos son:*

* *`"AAACGTT"` y `"TTAC"` tienen solapamiento 2 (“TT"`).*
* *`"AAACGTT"` y `"CGTTTA"` tienen solapamiento 4 (“CGTT"`).*
* *`"AAACGTT"` y `"CCAAT"` tienen solapamiento 0.* 

1. Realice una función `def hay_solapamiento (a, b, n)` que devuelva si los `n` últimos aminoácidos de `a` son iguales que los `n` primeros caracteres de `b` (recuerde que si `n` es mayor que la longitud de `a` o `b` deberá devolver `False` sin hacer ninguna comprobación adicional).*
2. Utilizando la función anterior realice la función `def max_solapamiento(a, b)` que indique cuál es el máximo solapamiento que existe entre las secuencias `a` y `b`.*

*__NOTA__: Para el apartado 1) puede intentar el uso de las funciones `s.endswith()` o `s.startswith()`. En el apartado b) pruebe todos los posibles solapamientos (de `0` a `len(b)`) y quédese con el mayor. Observe que si prueba en orden opuesto (empezando en `len(b)`) el primero que encuentre será el mayor y puede ahorrar comprobar el resto.*

*__OBJETIVOS__: Diseño de programas complejos.*

[[Ver Código](p6e05.sufijo.py)]

## p6e06.ahorcado.py (★★★★★) 
*El Ahorcado es un juego de adivinanzas. El ordenador selecciona una frase (en este caso títulos de películas/series) y el jugador trata de adivinarla según lo que sugiere por letras. Si el jugador sugiere una letra que aparece en la palabra, el ordenador escribe en todas sus apariciones en sus posiciones correctas.  Si la letra sugerida no ocurre en la palabra, el otro jugador saca un elemento de la figura de hombre palo ahorcado como una marca de conteo. El juego termina cuando:* 

* *El jugador completa (adivina) la frase –gana el jugador-, o*
* *El ordenador completa el diagrama (figura del hombre ahorcado) –pierde el jugador-.*

*En el campus virtual se ofrece un código inicial para el juego (descomprima el fichero y meta todo el contenido en la misma carpeta).*

*En primer lugar, realice una función `def esta(texto, l)` que nos devuelve `True` si `l` no es una letra del abecedario o si la letra `l` aparece dentro del texto (independientemente si aparece en mayúscula o minúscula).*

*Luego desarrolle `def codificar(secreta, letras)` que genere un texto con el mismo contenido que secreta pero donde se reemplacen las letras del abecedario (a-z) con guiones bajos si no están en el texto letras. Use la función `esta()`. Por ejemplo `codificar("Star wars 1", "sa")` devolvería el texto `"S_a_ _a_s 1"`.*

*Mediante el uso de esas funciones y las facilitadas en utils_hangman.py desarrolle el juego que cumpla los siguientes pasos:*

1.	*Escriba el título*
2.	*Obtenga una película*
3.	*Obtenga la versión codificada de la película, las letras solicitadas a vacío y ponga que los fallos son 0*
4.	*Repita mientras que no haya acertado y no se hayan acabado los intentos:*
  *	*Borre la pantalla*
  *	*Dibuje el muñeco de palo apropiado a los fallos*
  *	*Pida una nueva letra*
  *	*Incorpórela a las letras solicitadas si no estaba*
  *	*Incremente los fallos si la letra no se había pedido previamente y no está en la peli a adivinar*
  *	*Genere la nueva versión codificada de la película*
5.	*Si ganó felicite al usuario*
6.	*Si no ganó: borre la pantalla y muestre el muñeco de palo ya completo*
7.	*Muestre el título de la película a adivinar*

[[Ver Código inicial](p6e06.hangman-original.py)]

[[Ver utils_hangman.py](utils_hangman.py)]

[[Ver películs](peliculas.txt)]

