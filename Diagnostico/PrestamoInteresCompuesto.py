prestamo = float(input("Ingrese el monto del préstamo: "))
tasa = float(input("Ingrese la tasa de interés trimestral en decimal: "))
trimestres = int(input("Ingrese el número de trimestres: "))
porcentaje_abono = float(input("Ingrese el porcentaje de abono extraordinario: "))

monto_total = prestamo * (1 + tasa) ** trimestres
valor_abono = monto_total * (porcentaje_abono / 100)
monto_final = monto_total - valor_abono

print(f"Monto antes del abono: {monto_total:.2f}")
print(f"Valor del abono: {valor_abono:.2f}")
print(f"Monto final a cancelar: {monto_final:.2f}")