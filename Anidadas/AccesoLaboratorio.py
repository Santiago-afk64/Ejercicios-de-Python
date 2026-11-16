estudiante = bool(input("¿Es estudiante de la UTPL? (V o F) ").strip().upper() in ("V", "VERDADERO"))

if estudiante:
    print("¿Tiene el carné vigente? (V o F)")
    tiene_carne = bool(input().strip().upper() in ("V", "VERDADERO"))
    if tiene_carne:
        print("Acceso permitido")
    else:
        print("Acceso denegado: carné no vigente")
else:
    print("¿Tiene autorización especial del docente? (V o F)")
    tiene_autorizacion = bool(input().strip().upper() in ("V", "VERDADERO"))
    if tiene_autorizacion:
        print("Ingreso temporal")
    else:
        print("Acceso denegado")