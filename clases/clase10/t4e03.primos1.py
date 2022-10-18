n1: int = int(input("Dime un valor: "))
n2: int = int(input("Dime otro valor: "))

if n1 < n2:
    mayor = n2
    menor = n1
else:
    mayor = n1
    menor = n2

print("Los números primos entre", menor, "y", mayor, "son:", end=" ")
for numero in range(menor, mayor+1):
    divisores = 0
    for i in range(1, numero+1):
        if numero%i == 0:
            divisores += 1
    if divisores <= 2:
        print(numero, end= " ")
