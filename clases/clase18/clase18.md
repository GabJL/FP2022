# Clase 18: 22 de noviembre de 2022

En esta clase hemos revisado el concepto y uso de diccionario y hemos practicado sobretodo el tema de lista de diccionarios.

## Ejercicio 1: Frecuencias
*Hacer una función `def freqs(s)` de recibiendo un texto s, nos devuelva un diccionario indicando cada letra que aparece en el texto cuántas veces aparece. Por ejemplo: `freqs("las gafas")` daría `{'l': 1, 'a': 3, 's': 2, ' ': 1, 'g': 1, 'f': 1}`.

[[Ver código](t7e04.frecuencias.py)]

# Ejercicio 2: Pagos
*Dados las líneas de texto del lateral. Realice las siguientes funciones:*
```python
pagos = [
"pepe: 20",
"lola: 30",
"pepe: 10",
"juan: 40",
"lola: 20",
"luis: 20",
"ana: 30",
"eva: 34"]
```
* *Recibiendo las líneas del lateral devuelva un diccionario que tenga como clave los nombres y valor, lo pagado en total.*
* *Otra que calcule el gasto medio.*
* *Finalmente, otra que imprima para cada uno si está a la par o si debe pagar/recibir y la cuánto.*

[[Ver solución](t7e05.pagos.py)]

## Ejercicio 3: Spotify

*En el fichero `songs.txt` tiene datos de las canciones más escuchadas de Spotify durante este año. De cada canción tenemos la siguiente información:*

* `'artist_names'`: *lista con los cantantes de la canción (list(str))*
* `'∂∂∂artist_names'`: *lista con los cantantes de la canción (list(str))*
* `'track_name'`: *nombre de la canción (str)*
* `'peak_rank'`: *posición más alta conseguida en el ranking semanal (int)*
* `'weeks_on_chart'`: *veces que ha estado en el ranking semanal (int)*
* `'danceability'`: *bailabilidad (float)*
* `'energy'`: *energía (float)*
* `'loudness'`: *ruidosidad (float)*
* `'speechiness'`: *cuánto se canta (cuanto más alto más palabras se dicen) (float)*
* `'liveness'`: *¿en vivo? (cuanto más alto más probabilidad hay) (float)*
* `'duration_ms'`: *duración (en milisegundos) (int)*

En la misma carpeta `songs.txt` cree un nuevo fichero llamado `info_spotify.py` y añada al inicio:

```python
from json import load

f = open("songs.txt", encoding="utf-8")
SONGS = load(f)
f.close()
```

*Ese código carga en la variable `SONGS` todas las canciones (es una lista de canciones (diccionarios con la información indicada previamente)). Ahora en este fichero puede usar los datos y, por ejemplo: `print(SONGS[0]["artist_names"]`) escribirá `['Glass Animals']` (que es el cantante de la primera canción).
Usando ese fichero, realice el código para contestar a las siguientes preguntas. Vaya copiando las respuestas en el SOCRATIVE de la clase para validar las respuestas. Si en el apartado hay varias preguntas copie las respuestas separadas con un espacio.*

1.	*¿Cuál es el título de la canción 79 del listado? (recuerde que las posiciones empiezan en 0)*
2.	*¿Cuál es el mejor puesto que ocupó en el ranking la última canción?*
3.	*¿Cuál es el segundo cantante de la segunda canción del listado?*
4.	*¿Cuántas canciones hay en el listado?*
5.	*¿Cuánto tiempo (en segundos y sin decimales) tardaríamos en escuchar todas las canciones?*
6.	*¿Cuántas canciones hay en vivo? (para considerarlas en vivo su liveness debe ser mayor de 0.6)*
7.	*¿Cuál es la energía media (con 2 decimales) de las canciones en las que participa ROSALÍA?*
8.	*¿Cuál es el título de la canción con más cantantes? ¿Cuántos cantantes participan? (En caso de que haya varias de igual número de cantantes elija la que esté antes)* 
9.	*¿Cuál es el título de la canción más corta? ¿Cuánto dura (en segundos sin decimales)? (En caso de que haya varias elija la última)* 

*Genere una lista de nombres de cantantes sin que haya repetidos.*

10.	*¿Cuántos artistas diferentes hay?*
11.	*¿Cuáles son los 10 últimos cantantes de esa lista? (genere un texto con sus nombres separados por ":-:").*

*Partiendo del listado previo, genere un diccionario donde para cada cantante (clave) indique cuántas canciones tiene (valor):*

12.	*¿Cuántas canciones hay de Imagine Dragons?*
13.	*¿Qué cantante tiene más canciones? ¿Cuántas tiene?* 


[[Ver canciones](songs.txt)]

[[Ver solución](info_spotify_completo.py)]
