prec_producto = float(input("Ingrese precio del producto:"))

Descuento = prec_producto * 0.20
prec_total = prec_producto - Descuento
IVA = prec_total * 0.15
Total = prec_total + IVA

print (f"Precio con descuento: {prec_total:.2f}")
print (f"Precio a cobrar: {Total:.2f}")