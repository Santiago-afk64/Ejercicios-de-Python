estudiante = input("¿Es estudiante de la UTPL? (V o F) ").strip().upper() in ("V", "VERDADERO")
horas = float(input("Ingrese las horas de permanencia: "))

tarifa = horas * 1.00
if estudiante:
    tarifa = tarifa * 0.50
    if horas > 4:
        tarifa = tarifa * 1.20
else:
    if horas > 6:
        tarifa = tarifa * 1.20

print("Monto a pagar: $", tarifa)