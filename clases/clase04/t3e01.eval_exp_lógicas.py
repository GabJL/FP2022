# Valores
s: str = "hola"
x: int = 5
T: bool = x != 10
F: bool = x > 10

# Expresiones lógicas
print("x se evalúa a", bool(x))
print("x - 5 se evalúa a", bool(x-5))
print('s < "adios" se evalúa a', s < "adios")
print('s < "home" se evalúa a', s < "home")
print('s >= "hola!" se evalúa a', s >= "hola!")
print('s >= "Hola" se evalúa a', s >= "Hola")
print("not T se evalúa a",  not T)
print("not not F se evalúa a", not not F)
print("not (T and F) se evalúa a", not (T and F))
print("not T or not F se evalúa a", not T or not F)
print("not (not T or not T) se evalúa a", not (not T or not T))
print("not F or not (F and F) se evalúa a", not F or not (F and F))