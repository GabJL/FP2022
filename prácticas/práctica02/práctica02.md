# Práctica 2

# p2e01.paridad.py – Par (★✰✰✰✰) 
*Realice un programa que lea un número de teclado y nos diga si es par o impar como el siguiente ejemplo:*

```
Introduzca un número: 7 
El 7 es un número impar 
```

*__OBJETIVOS:__ Uso de la sentencia de selección binaria*

[[Ver solución](p2e01.paridad.py)]

# p2e02.imc_v2.py – No estoy gordo, soy de constitución fuerte (★★✰✰✰) 
*Construir un programa que calcule el índice de masa corporal de una persona (IMC = peso [kg] / altura2 [m]) e indique el estado en el que se encuentra esa persona en función del valor de IMC. Utilice una sentencia de selección múltiple (`if/elif/.../else`).*

| IMC |Diagnóstico | 
| --- | --- |
| < 16 | Ingreso en el Hospital |
| [16, 18) | Bajo peso |
| [18, 25) |Peso normal (Saludable) |
| [25, 35) | Sobrepeso |
| >= 35 | Obesidad |
 
*__OBJETIVOS:__ Ser capaz de utilizar de forma apropiada la sentencia de selección múltiple. Ser capaz de simplificar las condiciones atendiendo a las condiciones de los ifs previos.*

[[Ver solución](p2e02.imc_v2.py)]

# p2e03.mayor.py – El más grande (★★✰✰✰) 
*Hacer un programa que pida tres números y diga el mayor de los tres. Por ejemplo:*
 
```
Indique un número: 8 
Indique otro número: 14 
Indique otro número: 1 
El mayor número es el 14 
``` 

*__OBJETIVOS:__  Pensar  una  solución  con  sentencias  de  selección  (existen  múltiples  alternativas)  y  ser  capaz  de implementarla.*
 
*__RETO (★★★✰✰):__ (Opcional) Sin cambiar el comportamiento (el usuario que lo utiliza no debe notar nada), cambie el código para que use a lo máximo dos variables (posiblemente una que lea los valores de uno en uno y otra que almacene el mayor hasta el momento)*
 
[[Ver solución](p2e03.mayor.py)]

# p2e04.ordenar.py – “El orden es importante” Marie Kondo (★★★✰✰) 
*Realice un programa que pida tres valores y los imprima de forma ordenada. Ejemplo:*

```
Indique un número: 8 
Indique otro número: 14 
Indique otro número: 1 
Los números ordenados son: 1 8 14 
``` 

*__OBJETIVOS:__  Pensar  una  solución  con  sentencias  de  selección  (existen  múltiples  alternativas)  y  ser  capaz  de implementarla.*
 
[[Ver solución](p2e04.ordenar.py)]

# p2e05.letras.py - char mander (★★★★✰) 
*Realice un programa que lea una letra minúscula y nos diga si el valor leído es una letra (vocal o consonante), un número o un símbolo, tal como se muestran en los siguientes ejemplos.*

*Primero haga una versión que distinga entre letra, número y símbolo, y una vez resuelto esa parte incorpore, como segunda versión, la distinción entre vocal o consonante si era una letra.*

```
 Escriba una letra: b 
 El carácter b es una consonante 
 
 Escriba una letra: 0 
 El carácter 0 es un número 
 
 Escriba una letra: ! 
 El carácter ! es un símbolo 
```

*__OBJETIVOS:__ Trabajo con letras y uso de sentencias de selección múltiples o anidadas.*
 
*__NOTAS:__*
* *Recuerde que puede comparar letras: letra == “a” o letra <= “z”.* 
* *Un orden adecuado los posibles casos puede ayudar a simplificar el ejercicio.*
 
*__RETO  (★★★★✰):__  (Opcional)  Modifique  el  código  de  forma  que  su  código  permita  tanto  mayúsculas  como minúsculas. Python ofrece los métodos `lower()` y `upper()` que permite convertir un texto a minúscula o mayúsculas, respectivamente (si la letra ya está en formato requerido o es otro tipo de símbolo, lo devuelve sin modificar). Por ejemplo, convertir en minúscula sería: `letra = letra_original.lower().`*

[[Ver solución](p2e05.letras.py)]