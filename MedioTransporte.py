print("Medio de transporte para recorrer 5 km:")
print("1. Bus urbano")
print("2. Taxi")
print("3. Bicicleta")
print("4. Caminar")
print("Seleccione una opción:")
opcion = int(input())

if opcion == 1:
    print("Tiempo estimado: 30 minutos")
    print("Económico, pero depende de paradas y tráfico.")
elif opcion == 2:
    print("Tiempo estimado: 15 minutos")
    print("Rápido y cómodo, aunque es la opción más cara.")
elif opcion == 3:
    print("Tiempo estimado: 25 minutos")
    print("Saludable y gratuito, pero Loja tiene varias pendientes.")
elif opcion == 4:
    print("Tiempo estimado: 60 minutos")
    print("Gratis y saludable, pero toma bastante tiempo.")
else:
    print("Opción inválida")