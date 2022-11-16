libro1: dict = {
    "título": "El Marciano",
    "autor": "Andy Weir",
    "editorial": "Nova",
    "páginas": 407,
    "precio": 20.5
}

print("El autor del libro es", libro1['autor'])

libro2: dict = {}

info: str = "Dune # Frank Herbert # Debolsillo (Pengun Ed.) 784 11.35"
título, autor, resto = info.split("#")

libro2["título"] = título.strip()
libro2["autor"] = autor.strip()

datos: list = resto.split()
libro2["páginas"] = int(datos[-2])
libro2["precio"] = float(datos[-1])
libro2["editorial"] = " ".join(datos[:-2])
print(libro2)

libro3: dict = {
    "título": título.strip(),
    "autor": autor.strip(),
    "páginas": int(datos[-2]),
}

if libro1['páginas'] > libro2['páginas']:
    print(f"El libro {libro1['título']} tiene {libro1['páginas']} páginas")
else:
    print(f"El libro {libro2['título']} tiene {libro2['páginas']} páginas")

if libro1['precio'] > libro2['precio']:
    libro1['precio'] = libro1['precio']*0.95
    print(libro1)
else:
    libro2['precio'] = libro2['precio']*0.95
    print(libro2)

