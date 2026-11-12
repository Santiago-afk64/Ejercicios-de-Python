distancia = float(input("Ingrese la distancia del viaje (km): "))
consumo = float(input("Ingrese el consumo del auto (km/l): "))
precio_combustible = float(input("Ingrese el precio del combustible por litro: "))
num_peajes = int(input("Ingrese el número de peajes: "))
costo_peaje = float(input("Ingrese el costo unitario de cada peaje: "))

litros = distancia / consumo
costo_combustible = litros * precio_combustible
costo_peajes = num_peajes * costo_peaje
costo_total = costo_combustible + costo_peajes

print("Litros necesarios:", litros)
print("Costo del combustible:", costo_combustible)
print("Costo de peajes:", costo_peajes)
print("Costo Total del viaje:", costo_total)