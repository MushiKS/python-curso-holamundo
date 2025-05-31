#los tramos impositivos para la declaración de la renta en un determinado
#pais son los siguientes
import os
os.system("cls")

renta = int(input("Cual es tu renta anual?"))

if renta > 60000:
    tipoImpuestos = renta * 45 / 100
    print("tu renta corresponde a un 45%:", tipoImpuestos,"$")
elif renta > 35000 < 60000:
    tipoImpuestos = renta * 30 / 100
    print("Tu renta corresponde a un 30%:", tipoImpuestos,"$")
elif renta > 20000 < 35000:
    tipoImpuestos = renta * 20 / 100
    print("Tu renta corresponde a un 20%:", tipoImpuestos,"$")
elif renta > 10000 < 20000:
    tipoImpuestos = renta * 15 / 100
    print("Tu renta corresponde a un 15%:", tipoImpuestos,"$")
elif renta < 10000:
    tipoImpuestos = renta * 5 / 100
    print("Tu renta corresponde a un 5%:",tipoImpuestos,"$")
else:
    print("no pagas renta")