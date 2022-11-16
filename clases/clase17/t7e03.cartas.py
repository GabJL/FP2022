from random import randint


def generar_carta() -> dict:
    palos: list = ["oros", "copas", "espadas", "bastos"]
    carta: dict = {
        "valor": randint(1, 10),
        "palo": palos[randint(0, 3)]
    }

    return carta


def escribir_carta(carta: dict) -> None:
    print(f"{carta['valor']} de {carta['palo']}")


def son_iguales(c1: dict, c2: dict) -> bool:
    return c1['valor'] == c2['valor'] and c1['palo'] == c2['palo']


def es_inferior(c1: dict, c2: dict) -> bool:
    return c1['valor'] < c2['valor'] or (c1['valor'] == c2['valor'] and c1['palo'] < c2['palo'])


# programa principal
carta1: dict = generar_carta()
carta2: dict = generar_carta()
while son_iguales(carta1, carta2):
    carta2 = generar_carta()

print("Tu carta es: ", end="")
escribir_carta(carta1)

respuesta: str = input("¿Crees que tu carta es la mayor (si/no)? ")
if (respuesta == "si" and es_inferior(carta2, carta1)) or (respuesta == "no" and es_inferior(carta1, carta2)):
    print("Acertaste!")
else:
    print("Fallaste")

print("La carta del ordenador era: ", end="")
escribir_carta(carta2)
