# Clase 9: 11 de octubre de 2022

En esta clase hicimos un ejercicio avanzando como el de los 12 y después se resolvió ejercicios de parciales de otros años

# EC1: Primer y último 12:

*Escribe un algoritmo que lea una lista de números enteros terminada en 0 y que encuentre y escriba en la pantalla al posición de la primera y última ocurrencia del número 12 dentro de la lista. Si el número 12 no está en la lista, el algoritmo debe escribir 0.*

Esto es un ejemplo de ejercicio avanzado que, salvo que se tenga experiencia, hay que ir resolviendo poco a poco:
* Primero leer hasta 0 (esto es un caso tradicional de lectura adelantada)
* Luego tenemos que ir contando las posiciones de los números que leemos:
  * En la primera lectura (la adelantada al bucle) indicamos que es la primera
  * Luego cada vez que leamos en el bucle decimos que hemos leído una mas.
* El siguiente punto es cómo saber la posición del último:
  * En el enunciado nos indica que si no existe ningún 12 devolvamos un 12, entonces se puede inicializar a 0
  * Luego cada vez que leamos un 12 debemos actualizarlo ya que ese doce leído es posterior a cualquiera que hayamos leído antes
* El último punto es cómo saber la primera posición:
  * Aquí el problema es distinguir si un 12 es el primero o no.
  * Si inicializamos el primero a 0 (por el mismo motivo que el último), eso ayuda a identificar el primero, ya que si la posición del primero es 0 (que es una posición incorrecta) quiere decir que aún no hemos leíso ningún doce y podemos actualizarlo. Luego ya la posición será diferente de 0 y no se actualizará más

[[Ver código](EC1.py)]


## EC2 (Ej 1 de Parcial 2021/2022 B)
*Hacer un programa que pide números enteros hasta el 0. El programa después debe indicar si todos los números estaban en orden, por ejemplo -3 5 5 9 0 diría True, con 0 también diría True pero con 8 7 0 diría False.*

[[Ver código](EC2.py)]

## EC3 (Ej 1 y 2 de Parcial 2020/2021)
*Hacer un programa que pida números enteros positivos al usuario hasta leer el 0. Después de esto, el programa debe escribir cuántos números divisibles por 5 se introdujeron. El programa también debe escribir cuál de ellos es el mayor divisible por 5 (si no hay múltiplos de 5 escribirá 0 como mayor).*

[[Ver código](EC3.py)]

## EC4 (Ej 5 de Parcial 2021/2022 A)
*Realice un programa que lea un número entero positivo, n, y nos indique si el número es perfecto (la suma de sus divisores propios –sin considerarse el mismo- da su propio valor). Por ejemplo 6 es perfecto ya que 6 = 1 + 2 + 3.*

[[Ver código](EC4.py)]

## EC5 (Ej 4 de Parcial 2020/2021)
*Hacer programas que pida 2 números enteros al usuario (a y b). Calcular el máximo común divisor de ambos. Para ello encontrar el menor de los dos, menor, y recorrer hacia abajo hasta encontrar el número que los divide a ambos. Si no lo hubiera terminaría en 1, que siempre divide. Por ejemplo: 15, 9 → 3; 8, 4 → 4; 3, 3 → 3*

Con for: [[Ver código](EC5_for.py)]

Con while: [[Ver código](EC5_while.py)]

### EC6 (Ej 3 de diferentes parciales)
*Hacer programas que pinte las siguientes figuras. Los . son espacios, no hay que imprimirlos, sólo están para que se puedan ‘ver’ los espacios y facilitar el contarlos:*

```
.....*.
....*.*.
...*.*.*.
..*.*.*.*.
.*.*.*.*.*.
*.*.*.*.*.*.
```

[[Ver código](EC6_a.py)]

```
*******
.*...*
..*.*
...*
```

[[Ver código](EC6_b.py)]

```
...****
..*....*
.*......*
**********
```

[[Ver código](EC6_c.py)]


