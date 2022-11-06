def letra_dni(dni: int) -> str:
    letra = "TRWAGMYFPDXBNJZSQVHLCKE"[dni % 23]
    return letra

# ------ PROGRAMA PRINCIPAL ------------------
dni: int = int(input("Introduce tu DNI (números): "))

print("Tu DNI completo es: ", dni, letra_dni(dni), sep="")