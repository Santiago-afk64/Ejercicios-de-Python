antiguedad = float(input("Ingrese los años de antigüedad: "))
sueldo = float(input("Ingrese el sueldo: "))
excelente = bool(input("¿La evaluación es excelente? (V o F) ").strip().upper() in ("V", "VERDADERO"))

bono = 0
if antiguedad > 2:
    bono = sueldo * 0.10
    if excelente:
        bono = bono + sueldo * 0.05
else:
    if excelente:
        bono = sueldo * 0.05

sueldo_total = sueldo + bono
print("Bono: $", bono)
print("Sueldo total: $", sueldo_total)