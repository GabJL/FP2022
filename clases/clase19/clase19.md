# Clase 19: 28 de noviembre de 2022

En este clase vimos cómo calcular el mínimo valor (o clave) de un diccionario. También vimos como trabajar cuando un campo de un diccionario almacena una lista. Finalmente, vimos de manera informal cómo leer un fichero y seguimos repasando cómo trabajar con una lista de diccionarios.

## Ejercicio 1: Máximo en un diccionario: 
*Dado un diccionario (con el del ejemplo) donde tenemos para una serie de meses su temperatura media, calcule cuál es la mayor temperatura media.*

```python
Málaga: dict = {"enero": 12, "febrero": 12, "marzo": 14, "abril": 16, "mayo": 19, "junio": 23, "julio": 26, "agosto": 26,"septiembre": 23, "octubre": 19, "noviembre": 15, "diciembre": 13}
Yakustk: dict = {"enero": -38, "febrero": -34, "marzo": -20, "abril": -5, "mayo": 8, "junio": 16, "julio": 20, "agosto": 15, "septiembre": 6, "octubre": -8, "noviembre": -27, "diciembre": -37}
```
[[Ver solución](t7e06.valor_may.py)]

## Ejercicio 2: Valor del máximo: 
*Modifique el anterior para obtener el nombre del mes que tiene la temperatura máxima.*

[[Ver solución](t7e07.clave_del_max.py)]

## Ejercicio 3: Diccionarios de listas: 
*La tasa de éxito de una asignatura mide el número de alumnos que superan una asignatura respecto al número de alumnos que se presentan a la asignatura. Dado un diccionario con las asignaturas como claves y que tienen como valor la tasa de éxito de los últimos años, realice un programa que escriba para cada asignatura la tasa de éxito media de esos años. Ejemplos (datos oficiales extraídos de la página de calidad de la UMA).*

```python
Salud: dict = {
  "Bioquímica estructural": [0.66, 0.61, 0.47, 0.64, 0.92, 0.92, 0.75], 
  "Cálculo": [0.55, 0.52, 0.48, 0.29, 0.29, 0.06, 0.17], 
  "Fundamentos de la programación": [0.58, 0.66, 0.53, 0.76, 0.7, 0.6, 0.49], 
  "Física I": [0.23, 0.41, 0.38, 0.45, 0.37, 0.4, 0.56], 
  "Álgebra lineal": [0.48, 0.44, 0.46, 0.54, 0.61, 0.41, 0.51]
}
```

[[Ver solución](t7e08.tasas.py)]

# Ejercicio 4 (Películas): Pasar texto a diccionario: 
*Realice una función que reciba un texto que tiene información de una película a un diccionario con esa información. El formato del texto es:*

```
título#director1, director2, …#actor1, actor2, … #género1, género2, …#año puntuación duración recaudación
```
Por ejemplo: 
```
Spider-Man: No Way Home#Jon Wa#Tom Holland, Zendaya, Benedict Cumberbatch, Jacob Batalon#Action, Adventure, Fantasy#2021 8.3 148 804.75 
```
debería devolver:
```python
{
"título": "Spider-Man: No Way Home ",
"directores": ["Jon Wa"],
"actores": ["Tom Holland", "Zendaya", "Benedict Cumberbatch", "Jacob Batalon"],
"géneros": ["Action", "Adventure", "Fantasy"],
"año": 2021, 
"puntuación": 8.3,
"duración": 148,
"recaudación": 804.75
}
```

[[Ver solución](t7e09.películas.py)]

# Ejercicio 5 (Películas): Leer fichero a lista de diccionario: 
*Lea el contenido de ["pelis.txt"](pelis.txt) y guárdelas en una lista. El esquema que usaremos es:*

```python
fichero = open(“nombre_fichero”)
lista = []
for línea in fichero:
	diccionario = decodificar_linea(línea)
	lista.append(diccionario)
fichero.close()
```

[[Ver solución](t7e09.películas.py)]

# Ejercicio 6: Películas: 
*Cree un grupo de 2 o 3 personas y conéctese a SOCRATIVE para validar sus respuestas a las siguientes preguntas:*

*1.- ¿Cuántas películas hay en el fichero?*

*2.- ¿Cuál es el último género de la sexta película en la lista? (Recuerde las listas empiezan en 0)*

*3.- ¿Cuáles son los primeros 3 actores de la sexta película en la lista? (El formato debe ser actor1, actor2, actor3)*

*4.- ¿Cuántas películas hay posterior al 2000?*

*5.- ¿Cuántas películas hay que tengan el género "Drama" entre sus géneros?*

*6.- ¿Cuál es la duración de la más larga?*

*7.- ¿Y cuál es su título?*

*8.- ¿Cuál es el título de la peli más valorada según la puntuación de IMDB?*

*9.- Según la puntuación de IMDB, ¿qué puesto ocuparía la película "Avengers: Endgame"? (Busque primero la película y obtenga su puntuación, luego mire cuántas películas hay por delante suya (tiene más puntuación)) (Tenga en cuenta que si ninguna película la superara estaría en la posición 1)*

*10.- ¿Cuántos géneros diferentes hay? (Se recomienda hacer una lista donde meta los géneros sin repetirlos).*

*11.- ¿Qué actor que ha participado en más películas? ¿y en cuantas? (La respuesta sería actor – num_pelis) (Se recomienda generar un diccionario con pares: actor:num_pelis y luego obtener el máximo).*

*Extra:*

*12.- ¿Qué actor es el más rentable?  Para esto se recomienda el siguiente proceso:*

*a)	Modifique el anterior para que en vez de ser actor: num_pelis se guarde una lista de 2 posiciones con la siguiente forma: actor: [num_pelis, recaudación_total]. Note que hay pelis que no se sabe la recaudación (aparecen con -1), ignórelas para los cálculos (no deben modificar ni num_pelis ni recaudación_total).*

*b)	Busque el que tiene una ratio recaudación/num_pelis más alto.*

[[Ver solución](t7e09.películas.py)]
