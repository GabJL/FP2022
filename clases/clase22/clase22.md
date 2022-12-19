# Clase 22: 19 de diciembre de 2021

##EC1 
*Dos números se consideran coprimos si no tienen divisores en común (salvo el 1). Realice una función que reciba dos números y devuelva un booleano indicando si son coprimos o no. Probar:*

```python
print(coprimos(7, 15)) # True
print(coprimos(7, 14)) # False
```
[Ver código](ec1%20sol.py)

##EC2 
*Hacer una función `suma_crecientes(l: list) -> list` que devuelva una lista con las sumas parciales de cada trozo creciente (o que se mantenga) de la lista que se pasa como parámetro. Probar:

```python
print(suma_crecientes([1, 3, 4, 2, 3])) # [8, 5]
print(suma_crecientes([1, 3, 4, 5])) # [13]
print(suma_crecientes([3, 2, 1])) # [3, 2, 1]
print(suma_crecientes([1, 1, 2, 3, 1, 2, 3, 2, 4])) # [7, 6, 6]
```

[Ver código](ec2%20sol.py)

##EC3 
*Dada una lista de segmentos, es decir, una lista donde cada elemento es otra lista `[a, b]` donde `a` es el origen y `b` el destino, generar otra lista con los segmentos simplificados. Los segmentos se pueden simplificar si tienen una parte en común, por ejemplo: `[5, 7]` y `[1, 6]` pueden simplificarse en `[1, 7]`. En la lista, cada segmento se puede simplificar solo con uno a lo sumo. Probar:*

```python
print(simplificar([[1,3], [2,4]])) # [[1,4]]
print(simplificar([[1,7], [9,15], [2,8]])) # [[1,8], [9,15]]
print(simplificar([[1,5], [2,4]])) # [[1,5]]
print(simplificar([[1,3], [7,9], [2,4], [6,8]])) # [[1,4], [6,9]]
```

[Ver código](ec3%20sol.py)

##EC4 
*Desarrolle un función `def leer_datos(nombre_fichero: str, equipo: str) -> dict` que lea un fichero que dispone de múltiples líneas con el formato: `Jornada: Jugador – Equipo: Goles`, tal como se muestra en el siguiente ejemplo:*

```text
2: K. Benzema – Real Madrid: 1
2: Iago Aspas – Celta: 1
2: L. Modrić – Real Madrid: 1
2: Vinicius Jr. – Real Madrid: 2
2: F. Valverde – Real Madrid: 1
2: R. Lewandowski – Barcelona: 2
2: A. Isak – Real Sociedad: 1
2: O. Dembélé – Barcelona: 1
2: Ansu Fati – Barcelona: 1
3: R. Lewandowski – Barcelona: 1
3: Pedri – Barcelona: 1
3: Joaquín Fernández – Real Valladolid: 1
3: Sergi Roberto - Barcelona: 1
3: Vinicius Jr. – Real Madrid: 1
3: Joselu – Espanyol: 1
3: K. Benzema – Real Madrid: 2
```

*Debe devolver un diccionario con cuántos goles a metido cada jugador del equipo indicado. Por ejemplo, para `leer_datos(`[“futbol.txt”](futbol.txt)`, “Real Madrid”)` devolvería `{“K. Benzema”: 3, “L. Modrić”: 1, “Vinicius Jr.”: 3}`.*

*Partiendo del código previo (si no lo sacó copie el diccionario del ejemplo previo), desarrolle una función `def máximos_goleadores(goleadores: dict) -> list` que reciba los goleadores de un equipo (diccionario) y nos devuelva una lista con los nombres de los jugadores que marcaron más goles. Note que pueden ser varios los que tengan el máximo número de goles del equipo. Para el ejemplo anterior devolvería: `[“K. Benzema”, “Vinicius Jr.”]`*

[Ver código](ec4%20sol.py)

## EC5 
*Se tiene la información de las películas del año 2017 en un fichero [cine2017.txt](cine2017.txt) de forma que detrás del título, que está en una línea, se tiene un resumen en varias líneas. La línea del título empieza por el carácter '*' y a continuación el resto de la línea es el título de la misma:*

```text
*Coco
Aspiring musician Miguel, confronted with his family’s ancestral ban on music, enters the Land of
the Dead to find his great-great-grandfather, a legendary singer
*Tres anuncios en las afueras
A mother personally challenges the local authorities to solve her daughter’s murder when they fail
to catch the culprit.
*Blade Runner 2049
A young blade runner’s discovery of a long-buried secret leads him to track down former blade
runner Rick Deckard, who’s been missing for thirty years.
*Call Me by Your Name
In Northern Italy in 1983, seventeen year-old Elio begins a relationship with visiting Oliver, his
father’s research assistant, with whom he bonds over his emerging sexuality, their Jewish heritage,
and the beguiling Italian landscape. 
*Logan
In the near future, a weary Logan cares for an ailing Professor X, somewhere on the Mexican border.
However, Logan’s attempts to hide from the world, and his legacy, are upended when a young
mutant arrives, pursued by dark forces.
*Dunkerque
Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army,
and evacuated during a fierce battle in World War II.
```

*Hacer una o varias funciones para que llamando a la función `def lee_peliculas (...)` reciba el nombre de un fichero como el que se pone de ejemplo [cine2017.txt](cine2017.txt) y nos devuelva una lista con registros (`dict`) cada uno con el `'nombre'` y la `'descripción'` de cada película que haya en el fichero. Fuera de esta función, guardar esa lista devuelta en una variable.*

*En el mismo fichero, ahora hacer una función `def busca_pelicula(…)` que reciba el listado obtenido en el problema anterior y cualquier nombre de película en el segundo parámetro. La función devolverá la descripción de la película. Si la película no estuviera, devolverá una cadena vacía. Al final de nuestro programa python llamar a la función con la lista y la película de nombre, por ejemplo, `"Coco"` primero e imprimir la descripción que se nos devuelva. Imprimir también la descripción de una película que no esté, `"Nemo"`, por ejemplo. Usar el tipo de bucle adecuado para lo que es el proceso de una búsqueda.*

[Ver código](ec5%20sol.py)
