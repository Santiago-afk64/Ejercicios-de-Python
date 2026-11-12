numero = int(input("Ingrese un número decimal entero positivo: "))
 
if numero < 0:
        print("Error: el número debe ser positivo")
else:
    if numero == 0:
            hexa = "0"
    else:
        hexa = ""
        cociente = numero
 
        while cociente > 0:
            residuo = cociente % 16
 
            if residuo < 10:
                digito = str(residuo)
            elif residuo == 10:
                digito = "A"
            elif residuo == 11:
                digito = "B"
            elif residuo == 12:
                digito = "C"
            elif residuo == 13:
                digito = "D"
            elif residuo == 14:
                digito = "E"
            else:
                digito = "F"
 
            hexa = digito + hexa
            cociente = cociente // 16
 
    print(f"{numero} en hexadecimal es: {hexa}")