import math

a = float(input("Cateto 1: "))
b = float(input("Cateto 2: "))

hipotenusa = math.sqrt(a**2 + b**2)
area = (a * b) / 2

print(f"Hipotenusa: {hipotenusa:.2f}")
print(f"Área: {area:.2f}")