# Pedimos/leemos los datos (convirtiéndolos de forma oportuna)
gradC: float = float(input("Que temperatura hace: "))

# Convertimos los grados
gradF: float = 1.8*gradC + 32

# Escribimos el resultado
print("En grados Farenheit son", gradF)