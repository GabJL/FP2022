from utils_hangman import *


# Programa principal
borrar_pantalla()
imprimir_titulo()
secreto: str = obtener_peli()
print("Peli a adivinar:", secreto) # Cuando desarrolle el juego, comente esta línea
dibujar_hangman(MAX_FALLOS-2) # Ejemplo de uso de dibujar_hangman y la constante MAX_FALLOS