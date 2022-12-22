# Segundo parcial (21/12/2022)

## Ejercicio 1
*Se define elemento cima de una lista como el elemento de la lista que es mayor que el que le precede y también mayor que el que le sucede en la lista (el primer elemento y último elemento de la lista no pueden ser cimas). Realice una función que reciba una lista de números y nos indique cuántas elemento cima. Probar con:*

```python
print(cima([1, 2, 1, 3, 1, 5])) # -> 2
print(cima([1, 2, 3, 4])) # -> 0
```

[[Ver Código](1.cimas.py)]

# Ejercicio 2
*Un polinomio `p(x) = anxn + an−1xn−1 + . . . + a1x + a0` se puede representar en un diccionario como `{n:an, .., 0:a0}`. Por ejemplo: `3x^2 − 2x + 5` sería `{2:3, 1:-2, 0:5}`. Hacer una función que reciba dos polinomios y los sume y devuelva el resultado: `def sumPol(a, b)` Por ejemplo para los polinomios: `3x^2 − 2` y `5x2 − x + 3` debería dar: `8x^2 − x + 1`. Nuestra función recibiría: `{2:3, 0:-2}` y `{2:5, 1:-1, 0:3}` y devolvería: `{2:8, 1:-1, 0:1}`. Probar con este ejemplo e imprimir el resultado devuelto por la función.*

[[Ver Código](2.pol.py)]

## Ejercicio 3
*Dado un fichero donde se encuentran las líneas de autobús de Málaga con sus paradas ([busesmalaga.txt](busesmalaga.txt)). El formato de cada línea de ese fichero es:*

```text
nombre_linea: parada1 | parada2 | ... | paradaN
```

*(a) Realice una función `def leeBuses(nomFich)` que lea uno de tales ficheros y lo guarde dentro de un diccionario donde la clave es el nombre de la línea y el valor es una lista de paradas.*
```python
{
"Línea 1": ["Av. de las Postas - Lorenza Correa", "Emilio Díaz", ...] ,
"Lí nea 2": ["Atarazanas", ...],
...
"Línea N4": [..., "Lope de Rueda - Sta. Isabel"]
}
```

*(b) Hacer una función que recibiendo el diccionario de autobuses y paradas y dos parámetros más con los nombres de dos paradas, encuentre una línea cualquiera de autobuses que pueda llevar de una a la otra, no importa el sentido: `def busEntreParadas(dicBuses, parada1, parada2)`. Si no estuviesen las dos paradas para ese autobús, devolver el valor `None` (no la cadena "None") Comprobar con los siguientes ejemplos:*

```text
Paseo del Parque - Plaza Marina -> Av. de Velázquez - Azucarera : Línea A
Córdoba -> Facultad de Ciencias : None
```

[[Ver Código](3.buses.py)]
