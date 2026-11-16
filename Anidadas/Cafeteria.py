print("----Menú----")
print("1. Café....$1.50")
print("2. Jugo....$1.20")
print("3. Sandwich....$2.50")
print("4. Salir")
op = int(input())

if op == 1:
    print("El precio es: $1.50")
elif op == 2:
    print("El precio es: $1.20")
elif op == 3:
    print("El precio es: $2.50")
elif op == 4:
    print("Hasta luego :D")
else:
    print("Error: opcion no valida")