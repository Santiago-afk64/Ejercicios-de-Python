monto = float(input("Ingrese el monto de la compra: "))
frecuente = input("¿Es cliente frecuente? (S/N): ").strip().upper()
 
if monto >= 500:
    porcentaje = 15
else:
    if monto >= 300:
        porcentaje = 10
    else:
        if monto >= 100:
            porcentaje = 5
        else:
            porcentaje = 0
 
    if frecuente == "S":
        porcentaje += 5
 
descuento = monto * porcentaje / 100
total = monto - descuento
 
print(f"Descuento aplicado: {porcentaje}%")
print(f"Total a pagar: ${total:.2f}")