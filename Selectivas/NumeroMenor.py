n1 = float(input("Ingrese el numero 1:"))
n2 = float(input("Ingrese el numero 2:"))
n3 = float(input("Ingrese el numero 3:"))

if n1 < n2 and n1 < n3:
    print(f"El numero menor es:{n1:.2f}")
elif n2 < n1 and n2 < n3: 
    print(f"El numero menor es:{n2:.2f}")
else:
    print(f"El numero menor es:{n3:.2f}")