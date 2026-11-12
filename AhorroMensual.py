capital = float(input("Ingrese el capital inicial: "))
deposito = float(input("Ingrese el depósito mensual: "))
n = int(input("Ingrese el número de meses (N): "))
tasa = float(input("Ingrese la tasa mensual en % (ej. 1.5): "))
 
saldo = capital
 
for mes in range(1, n + 1):
    saldo = saldo + deposito
    interes = saldo * tasa / 100
    saldo = saldo + interes
    print(f"Mes {mes}: saldo = ${saldo:.2f}")