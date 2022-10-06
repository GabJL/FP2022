N: int = int(input("Dime el límite: "))

for i in range(1, N+1, 1):
  if i%2 == 0 or i%3 == 0:
    print(i,"->",i*i)
