print("Ingrese la letra de calificación (A, B, C, D, F)")
letra = input()
letra = letra.upper()

if letra == "A":
    print("Rango: 9 - 10")
elif letra == "B":
    print("Rango: 8 - 8.9")
elif letra == "C":
    print("Rango: 7 - 7.9")
elif letra == "D":
    print("Rango: 6 - 6.9")
elif letra == "F":
    print("Rango: 0 - 5.9")
else:
    print("Letra no válida")