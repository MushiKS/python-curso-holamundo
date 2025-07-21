import os
os.system("cls")

# Acumuladores y contadores
# Acumulan cuotas por tipo de socio
acum_p = acum_s = acum_c = 0  
# Contadores de socios por tipo
cont_p = cont_s = cont_c = 0  
# Contadores de libros por tipo
cont_f = cont_t = cont_d = 0  
# Contadores de movimientos
cont_consulta = cont_prestamo = 0 
# Contadores de forma de pago 
cont_ef = cont_tarj = 0  
# Libros en consulta de socios premium
cont_libros_consulta_premium = 0  

# Listado de socios para muestreo
socios = []

# Puedes cambiar el rango para más socios
for trans in range(100, 400, 100):
    ape = input("Ingrese su apellido: ").upper()
    socio = input("Qué tipo de socio es: P/S/C: ").upper()
    while socio != "P" and socio != "S" and socio != "C":
        print("Dato incorrecto, vuelva a ingresar datos P/S/C")
        socio = input("Qué tipo de socio es: P/S/C: ").upper()

    # Determinar clase y cuota
    if socio == "P":
        clase = "PREMIUM"
        cuota = 8250
        cont_p += 1
    elif socio == "C":
        clase = "CLASICO"
        cuota = 8150
        cont_c += 1
    else:
        clase = "STANDARD"
        cuota = 8850
        cont_s += 1

    # Movimiento
    if socio == "P":
        mov = input("¿Desea pedir préstamo o consulta? P (PRESTAMO) / C (CONSULTA): ").upper()
        while mov != "P" and mov != "C":
            print("Dato incorrecto, solo P o C")
            mov = input("¿Desea pedir préstamo o consulta? P/C: ").upper()
    else:
        mov = input("Que solicitud necesitas hacer? consulta(C):").upper()
        while mov != "C":
            print("Solo puedes hacer consultas (C)")
            mov = input("Que solicitud necesitas hacer? consulta(C):").upper()

    # Contar movimientos
    if mov == "C":
        cont_consulta += 1
        if socio == "P":
            cont_libros_consulta_premium += 1
    else:
        cont_prestamo += 1

    name_book = input("Ingrese el nombre del libro: ").upper()

    tipo_libro = input("Ingrese el tipo del libro: F/T/D. ").upper()
    while tipo_libro != "F" and tipo_libro != "T" and tipo_libro != "D":
        print("Dato incorrecto, vuelva a ingresar F/T/D")
        tipo_libro = input("Ingrese el tipo del libro: F/T/D. ").upper()

    # Contar libros por tipo
    if tipo_libro == "F":
        cont_f += 1
    elif tipo_libro == "T":
        cont_t += 1
    else:
        cont_d += 1

    # Forma de pago
    valor = input("¿Cómo desea pagar su cuota? E (Efectivo) / T (Tarjeta): ").upper()
    while valor != "E" and valor != "T":
        print("Dato incorrecto, solo E/T")
        valor = input("¿Cómo desea pagar su cuota? E/T: ").upper()

    # Contar formas de pago
    if valor == "E":
        cont_ef += 1
        total = cuota * 0.90  # 10% de descuento
    else:
        cont_tarj += 1
        total = cuota * 1.05  # 5% de recargo

    # Acumular cuotas según tipo de socio y forma de pago
    if socio == "P":
        acum_p += total
    elif socio == "S":
        acum_s += total
    else:
        acum_c += total

    # Guardar datos para muestreo
    socios.append({"trans": trans, "ape": ape, "socio": socio, "clase": clase, "mov": mov, "libro": name_book, "tipo_libro": tipo_libro, "forma_pago": valor, "cuota": cuota, "total": total})

    # muestreo datos de cada socio 
    print(f"Clase de socio: {clase}")
    print(f"Cuota a pagar: {cuota}")
    print(f"Nombre del libro: {name_book}")
    print(f"Tipo de libro: {tipo_libro}")
    print(f"Forma de pago: {valor}")
    print(f"Total a pagar: {total}")

