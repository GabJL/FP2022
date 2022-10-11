a: int = int(input('a: '))
b: int = int(input('b: '))
mcd = 1

for i in range (1, a + 1):
    if a%i == 0 and b%i == 0:
        mcd = i
        
print('El máximo común divisor es', mcd)