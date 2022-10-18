#Funciones
def factorial(N: int) -> int:
    res: int = 1
    for i in range(2, N+1):
        res *= i
    return res


# Programa principal
m: int = int(input("Dime el valor de m: "))
n: int = int(input("Dime el valor de n: "))
factorial_m: int = factorial(m)
factorial_n: int = factorial(n)
factorial_m_n: int = factorial(m-n)

combinatorio: int = factorial_m / (factorial_n * factorial_m_n)

print("El resultado es", combinatorio)
