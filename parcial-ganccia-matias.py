#los nervios me ganaron, para la proxima estare mas preparado 
import os
os.system("cls")

# Nº de transacción: Se genera automáticamente: 100 – 200 – 300 ….
# Apellido: todo en mayúscula  
# Tipo de socio: P/S/C. Mayúscula


trans = 100

ape = input("ingrese su apellido: ").upper()
socio = input("Que tipo de socio es: P/S/C: ")
while socio!="P" and socio!="S" and socio!="C":
    print("Dato incorrecto, vuelva ingresar datos P/S/C")
    socio = input("Que tipo de socio es: P/S/C").upper()
if socio=="P":
    cuota= 8250
    pregunta = input("Deseas pedir prestamo o consulta? P/C: ").upper()
    if pregunta=="P":
        prestamo = ("Que libro necesitas de prestamos? ")
        book = input("Ingrese el libro que busca: ").upper()
        tl = input("Que tipo de libro es? F/T/D").upper()
        fp = input("Forma de pago? E/T")
elif socio=="S":
    cuota = 8850
    print("solo puedes hacer consultas")
    socioS = input("Cual es su consulta?")
else:
    cuota=8150
    ("Cual es su consulta?")
print("Su tarjeta de socio es ",socio," y su cuota pagar es ",cuota)

valor = (input("Como desea pagar su cuota? efectivo o tarjeta "))
if valor =="efectivo":
    pagar = (cuota * 100) / 3
    print("debes pagar el total de ",pagar)