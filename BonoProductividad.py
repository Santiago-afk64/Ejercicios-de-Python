sueldo_base = float(input("Ingrese el sueldo base: "))
productividad = float(input("Ingrese el porcentaje de productividad: "))

if productividad >= 90:
    porcentaje = 0.20
else:
    if productividad >= 70:
        porcentaje = 0.10
    else:
        if productividad >= 50:
            porcentaje = 0.05
        else:
            porcentaje = 0

bono = sueldo_base * porcentaje
total = sueldo_base + bono

print("Bono: $", bono)
print("Total a pagar: $", total)