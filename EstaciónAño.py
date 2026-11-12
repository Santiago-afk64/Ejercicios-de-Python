mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Error: fecha fuera de rango")
else:
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Verano")
    else:
        if (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            print("Otoño")
        else:
            if (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
                print("Invierno")
            else:
                print("Primavera")