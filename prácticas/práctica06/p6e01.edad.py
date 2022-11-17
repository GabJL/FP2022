def escribir_vida(t: str) -> str:
    nombre, resto = t.split(":")
    nac, edad = resto.split(",")
    return f"{nombre} vivió desde {int(nac)} hasta {int(nac) + int(edad)}"


t: str = "Stan Lee: 1922, 96"
print(escribir_vida(t))
