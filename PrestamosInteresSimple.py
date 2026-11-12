capital = float(input("Capital: "))
tasa = float(input("Tasa anual (decimal): "))
meses = int(input("Plazo en meses: "))

interes = capital * tasa * (meses / 12)
cuota = (capital + interes) / meses

print(f"Interés total: {interes:.2f}")
print(f"Cuota mensual: {cuota:.2f}")
