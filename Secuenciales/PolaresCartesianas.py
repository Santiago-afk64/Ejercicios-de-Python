import math

r = float(input("Radio: "))
grados = float(input("Ángulo en grados: "))

radianes = math.radians(grados)
x = r * math.cos(radianes)
y = r * math.sin(radianes)

print(f"x = {x:.4f}")
print(f"y = {y:.4f}")