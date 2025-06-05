import os
os.system("cls")

print ("-- Datos del comprador --")
nombre = input("nombre: ")
ciudad = input("ciudad: ")
edad = int(input("edad: "))

#calculo del descuento
#si si el cliente es de cordoba, rosario o mendoza, tiene 20% de descuento
#si el no vive en esas ciudades pero tiene 18 y 26,tiene 20% de descuento

if ciudad == "cordoba" or ciudad == "rosario" or ciudad == "mendoza":
    descuento = 20
elif edad >=18 and edad <= 26:
    descuento = 20
else:
    descuento = 0
    
print ("El sr/a"+nombre+f" tiene un descuento de {descuento}%")