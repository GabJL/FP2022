# Funciones
def leeBuses(nombre_fichero: str) -> dict:
    resultado: dict ={}
    f = open(nombre_fichero, encoding="utf8")
    for linea in f:
        # Analizar linea -> obtener los datos -> nombre y paradas (list)
        nombre, paradas = linea.split(":")
        lista_paradas = paradas.split("|")
        for i in range(len(lista_paradas)):
            lista_paradas[i] = lista_paradas[i].strip()
        # Agregar esa información con el resto
        resultado[nombre] = lista_paradas
    f.close()
    return resultado
    
def busEntreParadas(dicBuses: dict, parada1: str, parada2: str) -> str:
    linea: str = ""
    nombres_lineas = list(dicBuses)
    i: int = 0
    while i < len(nombres_lineas) and linea == "":
        bus: str = nombres_lineas[i]
        if parada1 in dicBuses[bus] and parada2 in dicBuses[bus]:
            linea = bus
        i += 1
    if linea == "":
        return None
    else:
        return linea

# Programa principal
buses: dict = leeBuses("busesmalaga.txt")
# print(buses["Línea 1"])

# Paseo del Parque - Plaza Marina -> Av. de Velázquez - Azucarera : Línea A
# Córdoba -> Facultad de Ciencias : None
p1: str = "Paseo del Parque - Plaza Marina"
p2: str = "Av. de Velázquez - Azucarera"
p3: str = "Córdoba"
p4: str = "Facultad de Ciencias"
print(f"{p1} -> {p2}: {busEntreParadas(buses, p1, p2)}")
print(f"{p3} -> {p4}: {busEntreParadas(buses, p3, p4)}")
