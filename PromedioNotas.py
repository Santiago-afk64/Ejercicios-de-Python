n = int(input("Ingrese la cantidad de notas: "))
while n <= 0:
    print("La cantidad de notas debe ser mayor que 0")
    n = int(input("Ingrese la cantidad de notas: "))

suma = 0.0
for i in range(1, n + 1):
    nota = float(input(f"Ingrese la nota {i} (0 a 10): "))
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10")
        nota = float(input(f"Ingrese la nota {i} (0 a 10): "))
    suma += nota

promedio = suma / n
print("El promedio de las notas es:", promedio)