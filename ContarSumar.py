n = int(input("Ingrese el valor de N: "))
 
contador = 0
suma = 0
 
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        contador += 1
        suma += i
 
print(f"Cantidad de múltiplos de 3 o 5: {contador}")
print(f"Suma de los múltiplos: {suma}")