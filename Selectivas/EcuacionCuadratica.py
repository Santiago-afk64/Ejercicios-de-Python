a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
 
if a == 0:
    print("No es una ecuación cuadrática (a no puede ser 0)")
else:
    discriminante = b ** 2 - 4 * a * c
 
    if discriminante > 0:
        print("Tiene dos soluciones reales distintas")
    else:
        if discriminante == 0:
            print("Tiene una solución real (doble)")
        else:
            print("No tiene soluciones reales")