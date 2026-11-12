numero = int(input("Ingrese un número de tres dígitos: "))
 
if 100 <= numero <= 999:
    copia = numero
    suma = 0
 
    while copia > 0:
        digito = copia % 10
        suma += digito ** 3
        copia = copia // 10
 
    if suma == numero:
        print(f"{numero} es un número de Armstrong")
    else:
        print(f"{numero} no es un número de Armstrong")
else:
    print("El número debe tener exactamente tres dígitos")