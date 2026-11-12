n = int(input("Ingrese el valor de N: "))
 
suma = 0.0
for i in range(1, n + 1):
    suma += 1 / i
 
print(f"La suma de la serie hasta N = {n} es: {suma:.4f}")