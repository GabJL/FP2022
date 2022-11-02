def convertir_temperatura(cent: float) -> (float, float):
    kelvin: float = cent + 273.15
    farenheit: float = cent*9/5 +32
    return kelvin, farenheit

# Programa principal
grados_cent: float = float(input("Dame los grados centígrados: "))
grados_k, grados_f = convertir_temperatura(grados_cent)
print("Los grados kelvin son:", grados_k, "y los farenheit son:", grados_f)