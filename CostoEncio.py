peso_real = float(input("Peso real (kg): "))
largo = float(input("Largo (cm): "))
ancho = float(input("Ancho (cm): "))
alto = float(input("Alto (cm): "))

peso_vol = (largo * ancho * alto) / 5000
peso_cobrar = max(peso_real, peso_vol)
costo = peso_cobrar * 2.50

print(f"Peso volumétrico: {peso_vol:.2f} kg")
print(f"Peso a cobrar: {peso_cobrar:.2f} kg")
print(f"Costo total: ${costo:.2f}")