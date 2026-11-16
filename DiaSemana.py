nombre = ""
tipo = ""

print("Ingrese un número del 1 al 7")
dia = int(input())

if dia == 1:
    nombre = "Lunes"
    tipo = "Día de clases"
elif dia == 2:
    nombre = "Martes"
    tipo = "Día de clases"
elif dia == 3:
    nombre = "Miércoles"
    tipo = "Día de clases"
elif dia == 4:
    nombre = "Jueves"
    tipo = "Día de clases"
elif dia == 5:
    nombre = "Viernes"
    tipo = "Día de clases"
elif dia == 6:
    nombre = "Sábado"
    tipo = "Fin de semana"
elif dia == 7:
    nombre = "Domingo"
    tipo = "Fin de semana"
else:
    nombre = "Inválido"
    tipo = "Número fuera de rango (1 a 7)"

print("Día:", nombre)
print("Tipo:", tipo)