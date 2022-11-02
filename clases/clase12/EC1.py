def convertir_a_kelvin(grados_cent: float) -> float:
    return grados_cent + 273.15

# Programa principal
grados: float = float(input("Dime los grados centígrados: "))
print(grados, "º centígrados son ", convertir_a_kelvin(grados), "º kelvin", sep= "")