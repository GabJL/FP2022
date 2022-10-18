# Clase 10: 18 de octubre de 2021

En esta clase se introdujo la necesidad de dividir el código en pequeños trozos para facilitar su escritura y su reutilización. También vimos cómo se hacen y se usan funciones en python. Como ejemplo para ilustrar todo esto vimos el cálculo de un número combinatorio

## Ejemplo: Números combinatorios

La idea es hacer el cálculo de un número combinatorio que es la división entre m! y n!\*(m-n)! Como se observa se necesitan calcular 3 veces el factorial de diferentes valores y entonces crear una trozo de código que lo calcule y lo podamos reutilizar facilita mucho realizar el programa.

[[Ver código sin funciones](t4e01.combinatorio1.py)]

[[Ver código con funciones](t4e02.combinatorio2.py)]

## Primos en un rango

Para mostrar las ventajas del uso funciones a la hora de simplificar el código, se hizo el ejercicio 3 de la práctica 4 donde se pide mostrar los números primos en un rango.

[[Solución sin funciones](t4e03.primos1.py)]

[[Solución con funciones](t4e04.primos2.py)]

## Cilindro 

*Realice dos funciones, una que calcule el área a partir del radio del círculo y otra que calcule su longitud.*

*Realice una función que calcule el área de un rectángulo.*

*Realice otra función que calcule el área del cilindro a partir de su radio y su altura. El área de un cilindro es la suma de sus componentes, es decir, es 2 veces área de la base (círculo) más el área del rectángulo.*

*Realice el programa principal que lea el radio y la altura del cilindro y nos muestre su área.*

[[Solución](t4e05.cilindro.py)]