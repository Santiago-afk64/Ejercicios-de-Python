val_compra = float(input("Ingrese el monto de la compra"))

if val_compra >= 200:
    Descuento = val_compra * 0.15
elif val_compra >= 100:
    Descuento = val_compra * 0.1
else:
    Descuento = val_compra * 0.05

Total = val_compra - Descuento

print(f"Pago con descuento:{Descuento:.2f}") 
print(f"Total a pagar:{Total:.2f}") 