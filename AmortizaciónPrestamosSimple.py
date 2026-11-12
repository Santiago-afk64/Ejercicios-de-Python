monto_prestamos = float(input("Ingrese el monto de prestamos: "))
tasa_mensual = float(input("Ingrese la tasa mensual: "))
n_meses = int(input("Ingrese el numero de meses: "))

interes_total = monto_prestamos * tasa_mensual * n_meses
cuota_mensual = (monto_prestamos + interes_total) / n_meses

print("El interes total es:", interes_total)
print("La cuota a pagar es:", cuota_mensual)