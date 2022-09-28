operando1: float = float(input("Dime el primer operando: "))
operando2: float = float(input("Dime el segundo operando: "))
operación: str = input("Dime qué operación hacer: ")

print(operando1, operación, operando2, "=", end="")
if operación == "+":
    print(operando1 + operando2)
elif operación == "-":
    print(operando1 - operando2)
elif operación == "*":
    print(operando1 + operando2)
elif operación == "/":
    if operando2 == 0:
        print("ERROR")
    else:
        print(operando1 / operando2)
else:
    print("ERROR")
