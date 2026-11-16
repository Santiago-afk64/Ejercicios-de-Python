n = int(input("Ingrese el número de meses: "))
 
saldo = 0.0
for mes in range(1, n + 1):
    aporte = float(input(f"Ingrese el aporte del mes {mes}: "))
    saldo += aporte
    saldo *= 1.008
 
print(f"Saldo final después de {n} meses: ${saldo:.2f}")