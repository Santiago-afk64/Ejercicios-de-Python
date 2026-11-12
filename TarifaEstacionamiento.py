tarifa_hora = 1.50
horas = float(input("Ingrese las horas de estacionamiento: "))
nocturno = input("¿Es horario nocturno? (S/N): ").strip().upper()
 
total = horas * tarifa_hora
 
if horas > 8:
    total = total * 1.25
 
if nocturno == "S":
    total = total * 1.30
 
print(f"Total a pagar: ${total:.2f}")