dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
valida = False
dias_mes = 0

if mes >= 1 and mes <= 12 and año > 0:
    if mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias_mes = 30
        else:
            dias_mes = 31

    if dia >= 1 and dia <= dias_mes:
            valida = True

    if valida:
        print("La fecha es válida")
    else:
        print("La fecha no es válida")