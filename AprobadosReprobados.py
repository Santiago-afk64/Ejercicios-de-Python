cant_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

aprobados = 0
reprobados = 0
i = 1

while i <= cant_estudiantes:
    nota = float(input(f"Ingrese la calificación del estudiante {i}: "))
    if nota >= 7:
        print("Aprobado")
        aprobados += 1
    else:
        print("Reprobado")
        reprobados += 1
    i += 1

print("Total aprobados:", aprobados)
print("Total reprobados:", reprobados)