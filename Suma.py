suma = 0
n = int(input("Ingrese un número (0 para terminar): "))

while n != 0:
    suma += n
    n = int(input("Ingrese otro número (0 para terminar): "))

print("La suma final es:", suma)