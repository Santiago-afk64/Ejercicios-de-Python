categoria = int(input("Categoría (1-4): "))
cantidad = int(input("Cantidad: "))
precio = float(input("Precio unitario: "))
descuento = 0.0
match categoria:
    case 1:
        if cantidad >= 10: 
            descuento = 0.05
    case 2:
        if cantidad >= 5: 
            descuento = 0.10
    case 3: 
        descuento = 0.03
    case 4: 
        descuento = 0.0
    case _: 
        print("Categoría inválida")
total = precio * cantidad * (1 - descuento)
if total > 100: 
    total *= 0.98
print(f"Total a pagar: ${total:.2f}")