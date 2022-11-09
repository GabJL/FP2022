def convertir_fecha(texto: str) -> str:
    año, mes, dia = texto.split("-")
    return dia + "/" + mes + "/" + año


# ----- PROGRAMA_PRINCIPAL -----------
fecha: str = input("Dame una fecha (formato estándar: ")
fecha_español: str = convertir_fecha(fecha)
print("La fecha", fecha, "en español sería", fecha_español)
