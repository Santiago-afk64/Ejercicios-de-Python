promedio = float(input("Ingrese el promedio del estudiante (0-10): "))
p_asistencia = float(input("Ingrese el porcentaje de asistencia (0-100): "))
 
if promedio >= 9 and p_asistencia >= 90:
    print("Estudiante con rendimiento Excelente")
else:
    if promedio >= 7 and p_asistencia >= 80:
        print("Estudiante con rendimiento Bueno")
    else:
        if promedio >= 6 and p_asistencia >= 70:
            print("Estudiante con rendimiento Regular")
        else:
            print("Estudiante con rendimiento Deficiente")