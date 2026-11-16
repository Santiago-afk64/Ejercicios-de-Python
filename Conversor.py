print("---- CONVERSOR ----")
print("1. Kilómetros a metros")
print("2. Metros a centímetros")
print("3. Horas a minutos")
print("4. Salir")
print("Seleccione una opción:")
op = int(input())

if op == 1:
    print("Ingrese los kilómetros:")
    valor = float(input())
    resultado = valor * 1000
    print(valor, "km =", resultado, "m")
elif op == 2:
    print("Ingrese los metros:")
    valor = float(input())
    resultado = valor * 100
    print(valor, "m =", resultado, "cm")
elif op == 3:
    print("Ingrese las horas:")
    valor = float(input())
    resultado = valor * 60
    print(valor, "h =", resultado, "min")
elif op == 4:
    print("¡Hasta pronto!")
else:
    print("Opción inválida")