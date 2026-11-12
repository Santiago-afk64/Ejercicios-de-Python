D = float(input("Depósito mensual: "))
i = float(input("Tasa mensual (decimal): "))
n = int(input("Número de meses: "))

total_depositado = D * n
vf = D * (((1 + i) ** n - 1) / i)

print(f"Total depositado: {total_depositado:.2f}")
print(f"Valor futuro: {vf:.2f}")