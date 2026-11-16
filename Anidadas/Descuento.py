print("Ingrese el monto total")
monto = float(input())
print("Es estudiante de la UTPL? (V o F)")
respuesta = input().strip().upper()
estudiante_utpl = respuesta == "V" or respuesta == "VERDADERO"

descuento = 0
if estudiante_utpl:
    descuento = 0.20
    if monto > 30:
        descuento = descuento + 0.05
else:
    if monto > 50:
        descuento = 0.10

m_final = monto * (1 - descuento)
print("El monto a apagar es: $", m_final)
print("Descuento:", descuento * 100, "%")