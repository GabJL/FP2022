# Clase 15: 14 de noviembre de 2022

## Ejercicio 1

*Hacer una función que separe en los distintos números una fecha dada en formato estándar: "2021-11-22", y devuelva la misma fecha como cadena en formato español: "22/11/2021". Use f-string para generar la respuesta.*

[[Ver código](t6e04.fechas_fstring1.py)]

## Ejercicio 2

*Dada la fecha-hora con formato estándar así:  "2021-11-22T12:30:01" devolver la cadena: "22/11/2021 12h 30m 01s". Use f-string para generar la respuesta.*

[[Ver código](t6e05.fechas_fstring2.py)]

## Ejercicio 3

*Realice una función que nos diga si una cadena contiene solo letras entre la “a” y “z” (sin utilizar la función s.isalpha())*

[[Ver código](t6e06.solo_letras.py)]

## Ejercicio 4

*Realice una función que reciba un texto y nos devuelva la cantidad de palabras que tiene.*

[[Ver código](t6e07.cantidad_palabras.py)]

## Ejercicio 5

*Realice una función que reciba un texto y nos devuelva un texto donde las palabras estén separadas entre sí por “ – “ (espacio, guion, espacio).*

[[Ver código](t6e08.listado_palabras.py)]

## Ejercicio 6

*Realice una función que reciba un texto y nos devuelva un listado con la longitud de las palabras que tiene.*

[[Ver código](t6e09.longitud_palabras.py)]

## Ejercicio 7

*Un robot médico ha empezado a fallar y estamos examinando sus ficheros de log donde informa de todas las situaciones anómalas ocurridas y las líneas ofrecidas son del tipo:*

```
[Sat Nov 27 11:33:59 2021] init: ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/drive
[Sat Nov 27 11:33:59 2021] init: ERROR: ConfigInitializeCommon - Failed to mount /usr/lib/wsl/lib

```
*Como puede observar el formato es `“[fecha] programa: tipo_de_mensaje: mensaje”` (observe que el mensaje puede tener internamente dos puntos). Haz una función que nos devuelva la fecha, el programa, el tipo de error y mensaje por separado.*

[[Ver código](t6e10.log.py)]

## Ejercicio 8

*Lea una línea con las notas de un alumno con el siguiente formato: "alumno: c1 c2 fi". Realice una función que reciba ese texto y nos devuelva dos valores: el nombre del alumno y su nota final (puede usar funciones auxiliares). Para calcular la nota final del alumno, wf = (10 - 0.15*c1 - 0.25*c2)/10 y después sumar todas las notas ponderadas: f*wf + 0.15*c1 + 0.25*c2.*

[[Ver código](t6e11.nota_final.py)]

## Ejercicio 9

*Función `suma_numeros_encontrados()` que recibe  como parámetro una cadena caracteres con números pero que pueden estar separados por  cualquier otro carácter y devuelve la suma de todos  ellos. Así, por ejemplo, si recibe "Debe 10€ de café y 20€ de la habitación y algo (¿30€?) de propina" devuelve el número 60.*

[[Ver código](t6e12.suma_num_en_texto.py)]

