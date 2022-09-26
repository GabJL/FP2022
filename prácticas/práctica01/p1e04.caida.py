import math

G: float = 9.81

altura: float = float(input("Indique la altura (en metros): "))

tiempo: float = math.sqrt((2*altura)/G)

print("El tiempo es", tiempo, "segundos")