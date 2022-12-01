# Práctica 7: Diccionarios

## Ejercicio de casa: Fútbol

*Vamos a desarrollar un único ejercicio (p7e01.futbol.py) con varios apartados. Se va a leer de un fichero los resultados de los partidos de fútbol de La Liga 22/23 jugados hasta la fecha y obtendremos diferentes resultados de tratarlo.*

*__Lectura del fichero:__*

*En el campus virtual se facilita el fichero [futbol.txt](futbol.txt) que tiene el siguiente contenido (se muestran las primeras líneas):*
```
    1. Athletic Club de Bilbao - RCD Mallorca: 0 0
    1. FC Barcelona - Rayo Vallecano: 0 0
    1. Real Betis Balompié - Elche CF: 3 0
    1. RC Celta - RCD Espanyol: 2 2
    1. Cádiz CF - Real Sociedad de Fútbol: 0 1
    1. CA Osasuna - Sevilla FC: 2 1
       ...
```
Es decir, son un conjunto de líneas, cada una de las cuales representa un partido y tiene el siguiente formato:

```
Jornada. Equipo_local – Equipo_visitante : goles_local goles_visitante
```

*__Apartado A (★★★★✰)__ Desarrollar una función `def obtener_partido(p: str) -> dict` que reciba una cadena de caracteres `s` con el formato anterior y nos devuelva un diccionario con los datos separados. Por ejemplo `obtener_partido("1. Real Betis Balompié - Elche CF: 3 0")` devolvería el diccionario `{"jornada": 1, "local": "Real Betis Balompié", "visitante": "Elche CF", "goles_local": 3, "goles_visitante": 0}`. Observe que los campos jornada, goles_locales y goles_visitante deben ser números naturales y local y visitante serán textos. Use `split()`.*

*__OBJETIVOS__: Realizar funciones y uso avanzado del `split`.*

*__Apartado B (★★✰✰✰)__ Desarrollar una función `def leer_fichero(s: str) -> list` que reciba el nombre del fichero en `s` y lee el fichero con el formato anteriormente descrito. Como resultado debe devolver una lista de partidos. El esquema para leer un fichero es el siguiente:*

```python
# Abrir el fichero s con codificación "utf-8"
# Crear lista vacía
# Para cada línea del fichero 
	# Obtener un partido a partir de la línea del fichero
	# Añadir el partido a la lista
# Cerrar fichero
```
*__OBJETIVOS:__ Leer un fichero y generar una lista de diccionarios*

*__Apartado C (★✰✰✰✰)__ En la parte del programa principal, llame de forma apropiada a leer_partidopara obtener los datos del partido  y  muestre  por  pantalla  cuántos  partidos  se  leyeron  con  el  siguiente  formato: `Se  han  cargado XXX partidos correctamente`donde `XXX`(deberían ser 140) serán los partidos que se han leído del fichero.*

*__OBJETIVOS:__ Uso de funciones.* 

*__Operaciones sencillas:__*

*__Apartado D (★★★✰✰)__ Desarrolle una función `def partidos_equipo(lista: list, equipo: str) -> None`que reciba el nombre de un equipo y nos  muestre  por  pantalla  los  partidos  en  los  intervino  dicho  equipo. Cada  partido  debe  mostrarse  con  el  formato mostrado en este ejemplo:*
```
Cádiz CF 0 - 1 Real Sociedad de Fútbol
```

*En el programa principal llame a la función con un equipo fijo (el que prefiera).*

*__OBJETIVOS:__ Mostrar datos filtrados de un listado.*

*__Apartado E (★★✰✰✰)__ Hacer función `def goles_equipo(lista: list, equipo: str) -> (int, int)`que nos devuelva cuantos goles ha marcado (goles a favor) y cuántos ha recibido (goles en contra) del equipo que pasan como parámetro. En el programa principal llame a esta función de forma apropiada. Por ejemplo, para `goles_equipo(l, "Cádiz CF")`devolvería `9` a favor y `26` en contra.*

*__OBJETIVOS:__ Cálculos sobre datos que cumplen cierta condición.*

*__Operaciones avanzadas:__*

*__Apartado F (★★★★★)__ Desarrollar una función que partiendo del listado de partidos devuelva un diccionario que tenga como clave el nombre de un equipo y como valor tendrá cuántos puntos ha conseguido. Un equipo consigue 3 puntos si gana un partido, 1 punto se lo empata y no consigue puntos si pierde. El contenido de ese diccionario debería contener: `{'Athletic Club de Bilbao': 24, 'RCD Mallorca': 19, 'FC Barcelona': 37, 'Rayo Vallecano': 22, 'Real Betis Balompié': 24, ...}`*

*__OBJETIVOS:__ Generación de un diccionario a partir de una lista.*

*__Apartado  G  (★★★★✰)__ Implemente  otra  función  que,  recibiendo  el  diccionario  previamente  generado,  nos  indique quién va en el primer puesto de la liga (el que tenga más puntos). Con los datos del fichero, el líder es `FC Barcelona`.*

*__OBJETIVOS:__ Mayor de un diccionario.*

*__Apartado H (★★★✰✰)__ Realizar otra función que, recibiendo el diccionario previamente generado y el nombre de un equipo, nos indique cuál es su puesto en la clasificación (su puesto viene determinado por cuántos equipos tienen más puntos que él, puede suponer que está delante de todos los que tiene sus mismos puntos). Por ejemplo, como posición del `Cádiz CF`debería devolver `18`.*

*__OBJETIVOS:__ Contar cuántos cumplen cierta propiedad.*

[[Ver solución](p7e01.futbol.py)]

