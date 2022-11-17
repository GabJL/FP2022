from utils_hangman import *


# En primer lugar realice una función def esta(texto, l) que nos devuelve True si l no es una letra del abecedario o si la
# letra l aparece dentro del texto (independientemente si aparece en mayúscula o minúscula).
def esta(texto: str, l: str) -> bool:
    texto = texto.lower()
    l = l.lower()

    encontrado: bool = False

    if l in texto:
        encontrado = True
    elif l < "a" or l > "z":
        encontrado = True

    return encontrado


# Luego desarrolle def codificar(secreta, letras) que genere un texto con el mismo contenido que secreta pero donde
# se reemplacen las letras del abecedario (a-z) con guiones bajos si no están en el texto letras. Use la función esta().
# Por ejemplo codificar(“Star wars 1”, “sa”) devolvería el texto “S_a_ _a_s 1”
def codificar(peli: str, letras: str):
    codificada: str = ""
    for letra in peli:
        if esta(letras, letra):
            codificada += letra
        else:
            codificada += "_"
    return codificada


# Programa principal

# 1. Escriba el título
imprimir_titulo()
# 2. Obtenga una película
secreto: str = obtener_peli()
# 3. Obtenga la versión codificada de la película, las letras solicitadas a vacío y ponga que los fallos son 0
letras: str = ""
codificada: str = codificar(secreto, letras)
fallos: int = 0
# 4. Repita mientras que no haya acertado y no se hayan acabado los intentos:
while codificada != secreto and fallos < MAX_FALLOS:
    #   a. Borre la pantalla
    borrar_pantalla()
    #   b. Dibuje el muñeco de palo apropiado a los fallos
    dibujar_hangman(fallos)
    print("Película:", codificada)
    #   c. Pida una nueva letra
    letra: str = input("Dime una letra: ")
    #   d. Incorpórela a las letras solicitadas si no estaba
    letras += letra
    #   e. Incremente los fallos si la letra no se había pedido previamente y no está en la peli a adivinar
    if not esta(secreto, letra):
        fallos += 1
    #   f. Genere la nueva versión codificada de la película
    codificada = codificar(secreto, letras)
# 5. Si ganó felicite al usuario
if codificada == secreto:
    print("Enhorabuena")
# 6. Si no ganó: borre la pantalla y muestre el muñeco de palo ya completo
else:
    print("No has acertado")
# 7. Muestre el título de la película a adivinar
print("La pelicula es:", secreto)