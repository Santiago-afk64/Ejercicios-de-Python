temperatura = float(input("Ingrese la temperatura: "))

if temperatura < 15:
    print("Temperatura: Fria")
else:
    if temperatura <= 25:
        print("Temperatura: Templado")
    else:
        print("Temperatura: Calido")
        if temperatura > 30:
            print("Temperatura: Calor extremo")