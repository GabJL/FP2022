def freqs(s: str) -> dict:
    letras: dict = {}
    for i in s:
        if i not in letras:
            letras[i] = 1
        else:
            letras[i] += 1
    return letras


# Programa principal:
texto: str = "las gafas"

print("Las letras de", texto, "son:")
print(freqs(texto))
