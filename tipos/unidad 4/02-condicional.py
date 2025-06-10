#ESTRUCTURAS CONDICIONALES: OPERADORES ESPECIALES

import os
os.system("cls")

#Lista de ciudades

listaCiudad = ["cordoba","rosario","mendoza","san juan","chubut","salta"]
print("-- Datos del comprador --")
nombre = input("nombre: ")
ciudad = input("ciudad: ")
edad = int(input("edad: "))

#calculo del descuento
#si el cliente es de cordoba o rosario o mendoza o san justo o chubut o salta
#tiene el 20% de descuento
#si no vive en esas ciudades pero tiene entre 18 y 26 años, tiene el 20% de descuento
#si no esta en ninguno de esos casos tiene el 0% de descuento

if ciudad in listaCiudad:
    descuento = 20
elif edad >=18 and edad<=26:
    descuento = 20
else:
    descuento = 0

print ("el sr/a" +nombre+f" tiene un descuento de {descuento}%")