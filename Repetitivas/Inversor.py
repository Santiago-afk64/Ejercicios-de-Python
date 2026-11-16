numero = int(input("Ingrese un número entero positivo: "))
 
if numero > 0:
    copia = numero
    invertido = 0
 
    while copia > 0:
        digito = copia % 10
        invertido = invertido * 10 + digito
        copia = copia // 10
 
    print(f"Número invertido: {invertido}")
else:
    print("Debe ingresar un número entero positivo")