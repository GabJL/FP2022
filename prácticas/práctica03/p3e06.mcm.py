n1: int = int(input("Diga un número: "))
n2: int = int(input("Diga otro número: "))

if n1<n2:
    mayor: int = n2
else:
    mayor: int = n1

mcm: int = mayor

while mcm % n1 !=0 or mcm % n2 !=0:
    mcm += mayor
    
print("El mcm es", mcm)
