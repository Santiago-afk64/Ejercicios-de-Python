potencia = float(input("Ingrese la potencia: "))
tarifa = float(input("Ingrese la tarifa: "))
horas_diarias = int(input("Ingrese las horas diarias: "))

consumo_mensual = (potencia / 1000) * horas_diarias * 30
costo_total = consumo_mensual * tarifa

print("El consumo mensual es:", consumo_mensual)
print("El costo total es:", costo_total)