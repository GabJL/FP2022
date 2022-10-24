def escribir_números(X: int) -> None:
    for i in range(1, X+1):
        print(i,end=" ")
    print()
    
N: int = int(input("Dime un número: "))
print("Los N primeros números son: ")
escribir_números(N)