# Clase 20: 29 de noviembre de 2021

Aunque ya en clases previas vimos cómo utilizar los ficheros, aquí lo vemos más formalmente y que alternativas tenemos para leer los ficheros.

## Ejercicio 1: Ficheros de números:
*Usando un editor de texto simple (tipo Notepad o incluso Thonny) cree un fichero con un número en cada línea. Realice un programa que lea el fichero e indique su suma.*

*Modifique el programa anterior para que nos indique su media.*

*Cree un fichero de texto donde hay muchas líneas y cada línea puede contener 1 o muchos números (separados por espacios). Realice un programa que lee el fichero y nos indique la media.*

[[Ver Código (1 número por línea)](t8e1.números1.py)]

[[Ver Código (varios número por línea)](t8e2.números2.py)]

## Ejercicio 2: Fichero de datos de series:

*Hacer un programa con una función que lea un fichero que tiene el siguiente formato:*
```
	Breaking Bad, 62, 50, Netflix
	Andor, 12, 45, Disney+
	La Casa del Dragón, 10, 55, HBOMax
	1899, 8, 50, Netflix
	The Boys, 24, 50, AmazonPrime
```
*La función debe devolverlo como lista de listas: `[ ["Breaking Bad", 62, 50, "Netflix"], ["Hawkeye", 6, 45, “Disney+"], …]`*
*La función debe devolver como lista de diccionarios: `[{"serie": "Breaking Bad", "episodios": 62, "duración": 50, "plataforma": "Netflix"}, …]`*
*En ambos casos añada un nuevo valor a cada una con la duración total. Luego, muestre el título de la más larga.

[[Ver Código (Lista)](t8e3.series_listas.py)]

[[Ver Código (Diccionario)](t8e4.series_dict.py)]
