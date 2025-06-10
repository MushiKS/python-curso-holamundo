import os 
os.system("cls")

print("-- DATOS DEL COMPRADOR --")
nombre = input("nombre: ")
ciudad = input("ciudad: ")
edad = int(input("edad: "))

#calculo del descuento
#si el cliente es de cordoba, rosario o mendoza, tiene 20% de descuento 
#si no vive en esas ciudades pero tiene entre 18 y 26 anios, tiene 20% de descuento
#si no esta en ninguno de esos casos tiene 0% de descuento

if ciudad == "cordoba" or ciudad == "rosario" or ciudad == "mendoza":
    descuento = 20
elif edad >=18 and edad<=26:
    descuento = 20
else:
    descuento = 0

print ("el sr/a" +nombre+f" tiene un descuento de {descuento}%")