número: int = int(input("Dime un número: ")) # Lectura previa al bucle
pos_actual: int = 0
pos_ult_12: int = 0
#es_el_primero: bool = True
pos_primer_12: int = 0
while número != 0:
    # Hacer cosas con "número"
    pos_actual += 1
    if número == 12:
        pos_ult_12 = pos_actual
        if pos_primer_12 == 0:
            pos_primer_12 = pos_actual
        """if es_el_primero:
            pos_primer_12 = pos_actual
            es_el_primero = False"""
    número = int(input("Dime otro número: ")) # Lee un valor para la siguiente iteración

print("El último 12 está en la posición", pos_ult_12)