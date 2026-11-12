num1 = int(input("Ingrese el primer número (positivo): "))
num2 = int(input("Ingrese el segundo número (positivo): "))
 
if num1 <= 0 or num2 <= 0:
    print("Error: los números deben ser positivos")
else:
    a = num1
    b = num2
 
    while b != 0:
        temp = b
        b = a % b
        a = temp
 
print(f"El MCD de {num1} y {num2} es: {a}")