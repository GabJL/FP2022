a: int = int(input('a: '))
b: int = int(input('b: '))

if a > b:
    mcd = b
else:
    mcd = a
    
while a%mcd != 0 or b%mcd != 0:
        mcd -= 1
        
print('El máximo común divisor es', mcd)

