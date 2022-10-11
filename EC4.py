n:int = int(input("Dime un número: "))
suma:int = 0

for i in range(1,n):
    if n%i==0:
        suma=suma+i
        
if suma==n:
    print("Es perfecto")
else:
    print("No es perfecto")