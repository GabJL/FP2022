def palabra_mas_larga(t: str) -> str:
    palabras: list = t.split()
    mayor = palabras[0]

    for p in palabras:
        if len(p) > len(mayor):
            mayor = p

    return p


t: str = "Esto es un texto largo para probar el ejercicio 2 de la práctica de Fundamentos de la Programación"
print(f"La palabra más larga es {palabra_mas_larga(t)}")