n = int(input("Ingrese la cantidad de calificaciones (N): "))
 
if n <= 0:
        print("Error: N debe ser mayor que 0")
else:
    suma = 0.0
    aprobados = 0
    reprobados = 0
    mayor = 0.0
    menor = 0.0
 
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota {i}: "))
 
        suma += nota
 
        if i == 1:
            mayor = nota
            menor = nota
        else:
            if nota > mayor:
                mayor = nota
            if nota < menor:
                menor = nota
 
        if nota >= 7:
            aprobados += 1
        else:
            reprobados += 1
 
    promedio = suma / n
 
    print("RESUMEN")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota mayor: {mayor}")
    print(f"Nota menor: {menor}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")