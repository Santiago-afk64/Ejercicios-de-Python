numero = int(input("Ingrese un número decimal entero positivo: "))

cociente = numero
binario = 0
potencia = 1

if numero == 0:
        binario = 0
else:
    while cociente > 0:
        residuo = cociente % 2
        binario = binario + (residuo * potencia)
        cociente = cociente // 2
        potencia = potencia * 10

print("El numero", numero, "en binario es:", binario)