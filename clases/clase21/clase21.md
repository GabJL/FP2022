# Clase 21: 12 de diciembre de 2021

En esta clase seguimos repasando ficheros y hacemos ejercicios de examen:

## Ejercicio 1: 
*Hacer una función (`def esc(l1: list, l2: list) -> float`) que devuelva el producto escalar de los dos vectores recibidos como parámetros, esto es: suma de los productos de los correspondientes componentes. Suponer que siempre los vectores recibidos tienen ambos la misma longitud. Probar:*

```python
print(esc([1.0, 2, 3], [3, 2, 1])) # 10.0
print(esc([0, 1.1, 0, 2], [-1, 10, 0, 2])) # 15.0
```

[[Ver Código](EC1.py)]

## Ejercicio 2:

*Hacer una función `sumaDiv(n: int) -> int` que devuelva la suma de los divisores del número entero n recibido como parámetro. Hacer otra función que nos diga si su parámetro entero es perfecto. Un número entero es perfecto cuando coincide con la suma de sus divisores. Probar:*

```python
print(esPerf(6)) # True
print(esPerf(28)) # True
print(esPerf(29)) # False
print(esPerf(496)) # True
```
[[Ver Código](EC2.py)]

## Ejercicio 3:

*Realice una función que realice una intersección de bolsas (las bolsas es un tipo parecido al conjunto, pero cada elemento puede estar varias veces). La intersección ofrece como resultado una lista donde aparezca los elementos que aparezcan en ambas listas sobre las que se aplica. Si hay repetidos, en el resultado estarán repetidos (la menor cantidad que hay en ambas listas). Probar:*

```python
print(intersección([1,2], [2,4])) # [2]
print(intersección([1,4,2], [2,4])) # [4,2]
print(intersección([1,2,2,3,5], [5,2,2,2,4])) # [2,2,5]
print(intersección([1,2], [3,4])) # []
```
[[Ver Código](EC3.py)]

## Ejercicio 4:

*Suponer que tenemos un fichero con los nombres de estudiantes y una serie de calificaciones en una cantidad dada, para todos igual, de asignaturas. Hacer una función `lee_notas(nombre_fichero: str) -> dict` que recibe el nombre de ese fichero y devuelve un diccionario del tipo: `{'Pedro Perez': [2.0, 6.0, 3.0, 8.1], 'Maria ... ': [1.0, 7.0, ...], ...}` Imprimir este diccionario para comprobar su contenido. Luego, realice otra función que nos devuelva el alumno con nota media más alta (todas las notas tienen el mismo peso). Usar como ejemplo el fichero [`notas.txt`](notas.txt) al final*

```text
ro Pérez: 2, 6, 3 ,8.1
María Rodríguez: 1, 7,7, 4
Ana Gómez: 5, 5,6, 5
```

[[Ver Código](EC4.py)]

## Ejercicio 5:

*Podemos definir un fichero multifasta como aquel que puede contener varias secuencias en formato fasta dentro. Ver ejemplo al final. Hacer una función que recibiendo el nombre de un fichero multifasta, guarde dentro de un diccionario de claves los identificadores y valores las secuencias. El diccionario del ejemplo sería: `{'Laurencia': 'TATGGTTGACATTGACCCCT', 'Glaucocystis': '…', …}` Hacer una función que devuelva tal tipo de diccionario a partir de un nombre de fichero. Hacer otra función que reciba un diccionario como el anterior y un fragmento de secuencia y devuelva una lista de los identificadores de las secuencias que tienen al menos una vez este fragmento.*

*Imprimir esta lista de identificadores como en el ejemplo:*

```python
seqs = lee_secuencias("seqs.txt ")
print(tienen_secuencia(seqs, "AAGG")) #['Glaucocystis', 'Macrocystis pyrifera']
```
*Fichero [`seq.txt:`](seq.txt)*
```
>Laurencia
TATGGTTGACATTGACCCCT
>Glaucocystis
ACTTTGGCTCCAGGAAGTAACCGGGGAA
GGCGAAGCTTCTCCGCATGGATCTTCCGTAGG
>Macrocystis pyrifera
ACTTTGGCTAAGGCCAAGTA
AATGGAGTGTGTACGATTGACGGGATGACGGACTAACAGT
```

[[Ver Código](EC5.py)]