km = float(input("Ingrese cantidad de kilometros: "))
val_base = float(input("Ingrese la tarifa base: "))
noche = input("Es de noche (S/N): ")

total = val_base + 1.50 * km

if km > 10:
    total = total + total * 0.20

if noche.upper() == "S":
    total = total + total * 0.30

print("El total a pagar es: $", total)