año: int = int(input("Año: "))

if (año%4 == 0 and año%100 != 0) or año%400 == 0:
  print("Bisiesto")
else:
  print("No bisiesto")