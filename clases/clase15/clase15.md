# Clase 15 (9 de noviembre de 2022)

En esta clase hemos repasado el tipo string. Luego se mostraron algunas operaciones interesantes sobre string, haciendo especial hincapié en `split`

## Ejercicio de examen

*Desarrollar una función `def verParéntesis(texto)` que reciba un texto que representa una expresión matemática y confirme o no que los paréntesis están equilibados. Para ello, lleve un contador que se incrementa en 1 si encuentra un ’(’ y lo decrementa en 1 si encuenta un ’)’. Si al recorrer el texto, ese contador alguna vez vale negativo o al acabar no es 0, quiere decir que no está equilibrado (y la función devolverá False). En otro caso, la expresión es correcta y devolverá True. Probar con:*

```
s = ’(2+(3 - x) *4) /(3+ y)’
print (f"{ verPar é ntesis (s)}: {s}") # True
s = ’2+(3 -x) /3+ y)’
print (f"{ verPar é ntesis (s)}: {s}") # False
s = ’(’
print (f"{ verPar é ntesis (s)}: {s}") # False
```
[[Ver código](t6e00.paréntesis.py)]

## Ejercicio corto: De texto a lista

*Hacer una función que separe los números de una cadena como: "3.4 8.21 9.01 -34" y nos devuelva una lista de valores numéricos*

[[Ver código](t6e01.pasar_a_lista.py)]

## Ejercicio corto: Conversor de fechas
*Hacer una función que separe en los distintos números una fecha dada en formato estándar: "2021-11-22", y devuelva la misma fecha como cadena en formato español: "22/11/2021"*

[[Ver código](t6e02.convertir_fecha.py)]

## Ejercicio corto: Conversor de fechas-hora
*Dada la fecha hora con formato estándar así: "2021-11-22T12:30:01" devolver la cadena: "22/11/2021 12h 30m 01s"*

[[Ver código](t6e03.convertir_fecha_hora.py)]

