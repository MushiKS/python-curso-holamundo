#ESTRUCTURAS CONDICIONALES: IF ANIDADOS
import os
os.system("cls")

print("-- calculo de descuento --")
sede = int(input("introduce una sede (1-central 2-otras): "))
edad = int(input("introduzca la edad del cliente:" ))
#sede central: si tiene +65 20%, sino 0%
#otras sedes: si tiene +65 15%, si tiene +40 10%, sino 0%

if sede ==1:
    if edad>= 65:
        descuento = 20
    else:
        descuento = 0
else:
    if edad>=65:
        descuento = 15
    elif edad>=40:
        descuento = 10
    else:
        descuento = 0

print ("el descuento para el cliente es de: ",descuento)