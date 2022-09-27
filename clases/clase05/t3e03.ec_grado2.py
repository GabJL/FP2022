a: float = float(input("Valor de a: "))
b: float = float(input("Valor de b: "))
c: float = float(input("Valor de c: "))

x1: float = (-b + (b*b - 4*a*c)**0.5)/(2*a)
x2: float = (-b - (b*b - 4*a*c)**0.5)/(2*a)

print("x1 =", x1)
print("x2 =", x2)