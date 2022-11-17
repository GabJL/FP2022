import random

# Máximo número de fallos
MAX_FALLOS: int = 6


# "Borra" la pantalla
def borrar_pantalla() -> None:
    for i in range(80):
        print()


# Información:
def imprimir_titulo() -> None:
    banner: str = """
   _____  .__                                     .___      
  /  _  \\ |  |__   ___________   ____ _____     __| _/____  
 /  /_\\  \\|  |  \\ /  _ \\_  __ \\_/ ___\\\\__  \\   / __ |/  _ \\ 
/    |    \\   Y  (  <_> )  | \\/\\  \\___ / __ \\_/ /_/ (  <_> )
\\____|__  /___|  /\\____/|__|    \\___  >____  /\\____ |\\____/ 
        \\/     \\/                   \\/     \\/      \\/       
  """
    print(banner)
    print("Pulse una tecla para empezar...", end="")
    input()
    borrar_pantalla()


# Escribir muñeco:
def dibujar_hangman(fallos: int) -> None:
    print("  +---+")
    print("  |   |")
    print("  ", end="")
    if fallos > 0: print("0", end="")
    else: print(" ", end="")
    print("   |")
    print(" ", end="")
    if fallos > 1: print("/", end="")
    else: print(" ", end="")
    if fallos > 2: print("|", end="")
    else: print(" ", end="")
    if fallos > 3: print("\\", end="")
    else: print(" ", end="")
    print("  |")
    print(" ", end="")
    if fallos > 4: print("/", end="")
    else: print(" ", end="")
    print(" ", end="")
    if fallos > 5: print("\\", end="")
    else: print(" ", end="")
    print("  |")
    print("      |")
    print("=======")


# Devuelve una peli
def obtener_peli() -> str:
    f = open("peliculas.txt", "r")
    num: int = int(f.readline())
    aleatorio: int = random.randint(1, num)
    for i in range(aleatorio):
        peli = f.readline()
    f.close()
    return peli
