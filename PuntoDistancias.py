import math

x1 = float(input("Ingrese valor x1: "))
y1 = float(input("Ingrese valor y1: "))
x2 = float(input("Ingrese valor x2: "))
y2 = float(input("Ingrese valor y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
punto_medio_x = (x1 + x2) / 2
punto_medio_y = (y1 + y2) / 2

print("La distancia de los dos puntos es:", distancia)
print("Las coordenadas del punto medio son: (", punto_medio_x, ",", punto_medio_y, ")")