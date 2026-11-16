promedio = float(input("Ingrese el promedio del estudiante: "))
reprobadas = int(input("Ingrese el número de materias reprobadas: "))
primer_ciclo = input("¿Es estudiante de primer ciclo? (S/N): ").strip().upper()

if promedio >= 9.0 and reprobadas == 0 and primer_ciclo == "S":
    porcentaje_beca = 100
elif promedio >= 8.0 and reprobadas <= 1:
    porcentaje_beca = 70
elif promedio >= 7.0 and reprobadas <= 2:
    porcentaje_beca = 40
else:
    porcentaje_beca = 0


print(f"Porcentaje de beca: {porcentaje_beca}%")

if porcentaje_beca > 0:
    print("Solicitud de beca aprobada")
else:
    print("Solicitud de beca rechazada")