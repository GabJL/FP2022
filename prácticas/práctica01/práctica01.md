# Práctica 1

## Ejercicio 1: p1e01.errores.py (★★★✰✰) 

*El siguiente programa escrito en python calcula la cantidad bruta y neta a pagar por un trabajo realizado en función de las horas y días trabajados. Sin embargo, en el momento en que se intenta ejecutar se producen una serie de errores. El alumno debe localizar dichos errores y corregirlos. Para ello debe examinar los  mensajes que proporciona el sistema e interpretarlos convenientemente.*
 
 ```python
TASA: int = 25.0 
PRECIO_HORA: float = 60.0 
 
horas: int = input("Introduzca las horas por día trabajadas: ") 
dias: int = float(input(Introduzca los días trabajados: )) 
horas * días * PRECIO_HORA = total: float 
neto: float = total - TASA 
 
print("El valor total a pagar es:", TOTAL) 
print(El valor neto a pagar es: neto) 
```
*Al final debe conseguir que funcione correctamente como se muestra en el siguiente ejemplo:*
 
```
Introduzca las horas por día trabajadas: 8 
Introduzca los días trabajados: 10 
El valor total a pagar es: 4800.0 
El valor neto a pagar es: 4775.0 
```

*__OBJETIVOS:__ Ser capaz de entender los errores reportados por el intérprete y saber cómo corregirlos.*

[[Ver solución](p1e01.errores.py)]

## Ejercicio 2: p1e02.pulsaciones.py (★✰✰✰✰) 
*El máximo ritmo cardiaco depende de la edad. Hacer un programa que calcule el máximo número de pulsaciones N que una persona puede tener, usando la fórmula: N = 220 – edad. Ejemplo:*
 
```
Indique qué edad tiene: 22 
Sus pulsaciones máximas son: 198 
``` 

*__OBJETIVOS:__ Implementar un algoritmo simple que incluye lectura, escritura y expresiones aritméticas simples.*

[[Ver solución](p1e02.pulsaciones.py)]
 
## Ejercicio 3: p1e03.imc.py (★✰✰✰✰) 
*Hacer un programa que calcule el Índice de Masa Corporal IMC de una persona usando la fórmula: 𝐼𝑀𝐶 = (𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔)/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚𝑒𝑡𝑟𝑜𝑠)² . Use el operador potencia (a\*\*b = 𝑎𝑏). Ejemplo:* 
 
```
Indique su peso (en kg): 85 
Indique su altura (en metros): 1.82 
Su IMC es 25.661152034778407 
``` 

*__OBJETIVOS:__ Uso del operador potencia.*
 
[[Ver solución](p1e03.imc.py)]

## Ejercicio 4: p1e04.caida.py (★★✰✰✰) 
*Escriba un programa que calcule el tiempo 𝑡 en segundos que tarda un objeto en llegar al suelo desde una altura leída de teclado. La relación entre la altura (𝑎) y el tiempo (𝑡) sigue la siguiente forma: a = (1/2)𝑔𝑡² donde 𝑔 es una constante con valor 9,81 m/s². La salida será como sigue:*  
 
```
Indique la altura (en metros): 1345 
El tiempo es 16.5593 segundos 
``` 

*__OBJETIVOS:__ Problemas simples que requieren expresiones aritméticas sencillas.*

[[Ver solución](p1e04.caida.py)]

## Ejercicio 5: p1e05.descarga.py (★★★✰✰) 
*Realice un programa que pida al usuario la velocidad de descarga de su conexión (en Mbps, Megabits por segundo) y el tamaño del fichero que quiere descargarse (en MB, Megabytes) y nos indique cuántos segundos (sin decimales) debería tardar la descarga. Un ejemplo posible de la ejecución del programa podría ser el siguiente:*

```
Indique la velocidad de descarga (en Mbps): 12 
Indique el tamaño del fichero a descargar (en MB): 30 
El tiempo de descarga estimado es 20 segundos 
```

*__OBJETIVOS:__ Ser capaz de diseñar un algoritmo simple y pasarlo a código fuente. Conversión de tiempos.*
 
[[Ver solución](p1e05.descarga.py)]

## Ejercicio 6: p1e06.operaciones_enteras.py (★★✰✰✰) 
*Realiza un programa que pidiendo al usuario dos números escriba en pantalla  su  producto,  división  entera  y  resto  de  esa  división  entera  de  los  números.  Para  obtener  el  resto  de  la división entera tenemos los operadores % (como en r = a % b) nos devuelve el resto de la división. Por ejemplo: el resto de 7 entre 3 es 1, 7 % 3 → 1). Por otro lado, // (como en r = a // b) nos devuelve el cociente entero, la parte entera de la división. Por ejemplo, 7 // 3 → 2). Un ejemplo de ejecución del programa podría ser el siguiente:*

```
Valor de a: 14 
Valor de b: 4 
a * b = 56 
a // b = 3 
a % b = 2 
``` 

*__OBJETIVOS:__ Uso de operadores matemáticos menos habituales (// y %).*

[[Ver solución](p1e06.operaciones_enteras.py)]
