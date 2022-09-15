n = int(input("Dime el alto de la figura: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print()
print("Gracias por usar nuestro programa! ")