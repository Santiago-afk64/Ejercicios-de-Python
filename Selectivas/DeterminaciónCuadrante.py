x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))
 
if x == 0 and y == 0:
    print("El punto está en el origen")
else:
    if x == 0:
        print("El punto está sobre el eje Y")
    else:
        if y == 0:
            print("El punto está sobre el eje X")
        else:
            if x > 0 and y > 0:
                print("Primer cuadrante")
            else:
                if x < 0 and y > 0:
                    print("Segundo cuadrante")
                else:
                    if x < 0 and y < 0:
                        print("Tercer cuadrante")
                    else:
                        print("Cuarto cuadrante")