m: int = int(input("Dime el valor de m: "))
n: int = int(input("Dime el valor de n: "))

factorial_m: int = 1
for i in range(2, m+1):
    factorial_m *= i

factorial_n: int = 1
for i in range(2, n+1):
    factorial_n *= i

factorial_m_n: int = 1
for i in range(2, m-n+1):
    factorial_m_n *= i

combinatorio: int = factorial_m / (factorial_n * factorial_m_n)

print("El resultado es", combinatorio)