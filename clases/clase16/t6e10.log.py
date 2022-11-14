# Funciones
def separar(texto: str) -> (str, str, str, str):
    fecha, resto = texto.split("]")
    fecha: str = fecha[1:]
    lista: list = resto.split(":")
    programa: str = lista[0].strip()
    tipo: str = lista[1].strip()
    mensaje: str = ":".join(lista[2:]).strip()
    return fecha, programa, tipo, mensaje


# Programa principal
t1: str = "[Sat Nov 27 11:33:59 2021] init: ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/drive"
t2: str = "[Sat Nov 27 11:33:59 2021] init: ERROR: ConfigInitializeCommon - Failed to mount /usr/lib/wsl/lib"

print(separar(t1))
print(separar(t2))