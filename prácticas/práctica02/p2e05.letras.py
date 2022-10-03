letra: str = input("Escritura una letra: ")

letra = letra.lower()

print("El carácter", letra, end="")
if letra >= "0" and letra <= "9":
    print(" es un número")
elif letra >= "a" and letra <= "z":
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print(" es una vocal")
    else:
        print(" es una consonante")
else:
    print(" es un símbolo")