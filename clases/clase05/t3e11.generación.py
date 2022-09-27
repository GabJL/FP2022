año: int = int(input("Dime tu año de nacimiento: "))

if año < 1946:
  print("Caso no considerado")
elif año < 1962:
  print("Baby Boomer")
elif año < 1981:
  print("Generación X")
elif año < 1997:
  print("Generación Y (millenials)")
elif año < 2011:
  print("Generación Z")
else:
  print("Generación T (táctil)")