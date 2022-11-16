ciudades: dict = {
    "Madrid": 3266126,
    "Barcelona": 1636762,
    "Valencia": 794288,
    "Sevilla": 688592,
    "Zaragoza": 674997,
    "Málaga": 574654,
    "Murcia": 453258,
    "Palma de Mallorca": 416065,
    "Las Palmas de Gran Canarias": 379925,
    "Bilbao": 346843
}

# Version 1
suma_claves = 0
for k in ciudades:
    suma_claves += ciudades[k]

# Version 2
suma_valores1 = 0
for k, v in ciudades.items():
    suma_valores1 += v

# Version 3
suma_valores2 = 0
for v in ciudades.values():
    suma_valores2 += v

print(suma_claves / len(ciudades), suma_valores1 / len(ciudades), suma_valores2 / len(ciudades))
