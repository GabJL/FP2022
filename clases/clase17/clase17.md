# Clase 17: 16 de noviembre de 2022

En esta clase se introdujo el concepto de diccionario y cómo trabajar con ellos.

## Ejercicio 1: Libros
*Nos interesa hacer un programa para manejar libros. De cada libro queremos: título, autor, precio, número de páginas y editorial.*

* *Cree una variable `libro1` con los siguientes valores: El Marciano de Andy Weir, editorial Nova, edición rústica (2014) con 407 páginas y 20,50 € de precio (quizás no necesite todos los datos).*
* *Suponiendo que lee de teclado: `Dune # Frank Herbert # Debolsillo (Pengun Ed.) 784 11.35` almacene los valores de forma apropiada en otra variable llamada `libro2`.*
* *Muestre el título y número de páginas del libro que tiene más páginas de los dos.*
* *Aplique un descuento de un 5% al libro más caro.*

[[Ver código](t7e01.libros.py)]

## Ejercicio 2: Ciudades
*Dadas las siguientes ciudades:*
```python
ciudades = {
	"Madrid": 		3266126,
	"Barcelona":		1636762,
	"Valencia": 		794288,
	"Sevilla": 		688592,
	"Zaragoza": 		674997,
	"Málaga": 		574654,
	"Murcia": 		453258,
	"Palma de Mallorca":	416065,    
	"Las Palmas de Gran Canarias": 379925,
	"Bilbao": 		346843
}
```
*Realice un programa que indique la población media.*

[[Ver código](t7e02.ciudades.py)]

## Ejercicio 3: Cartas
*Sabiendo que una carta tiene valor (1 a 10) y palo (oros, espadas, copas y bastos), realice las siguientes funciones:*
* *Una que genere una carta aleatoria (use `randint` de `random`)*
* *Otra que muestre por pantalla una carta*
* *Una función que nos diga si dos cartas son iguales*
* *Una función que reciba dos cartas y nos devuelva un valor booleano indicando si la primera carta es inferior a la segunda (es menor que otra si su valor es inferior o si es igual pero la figura es menor según el orden lexicográfico).*
* *El programa principal generará una carta para el usuario y otra para el ordenador (deben ser diferentes). Le mostrará su carta al usuario y éste debe apostar si su carta será la mayor o la menor. El ordenador mostrará su carta y si el usuario acertó con su apuesta.*

[[Ver código](t7e03.cartas.py)]
