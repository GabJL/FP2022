n: int = int(input("Dime un número: "))

producto: int = 1
for i in range(1, n+1):
  producto *= i
  
print(n, "!= ", producto, sep="")
