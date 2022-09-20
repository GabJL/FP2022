import math

cateto1: float = float(input("Cateto 1: "))
cateto2: float = float(input("Cateto 2: "))

hipotenusa: float = math.sqrt(cateto1**2 + cateto2**2)
# También vale:
# hipotenusa = (cateto1**2 + cateto2**2)**0.5

print("Hipotenusa: ", hipotenusa)