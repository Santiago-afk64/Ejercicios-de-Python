angulo_1 = float(input("Ingrese el angulo 1 del triangulo: "))
angulo_2 = float(input("Ingrese el angulo 2 del triangulo: "))
angulo_3 = float(input("Ingrese el angulo 3 del triangulo: "))

suma = angulo_1 + angulo_2 + angulo_3

if suma == 180 and angulo_1 > 0 and angulo_2 > 0 and angulo_3 > 0:
    if angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
        print("Triangulo rectangulo")
    else:
        if angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90:
            print("Triangulo obtusángulo")
        else:
            print("Triangulo acutángulo")
else:
    print("Error: los angulos no forman un triangulo valido")