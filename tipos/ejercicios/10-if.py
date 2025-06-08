# escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automatica el precio que debe cobrar a sus clientes 
#por entrar. el programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. si el cliente es menor de 4 anio puede entrar gratis. 
#si tiene 4 y 18 anios debe pagar 5 y si es mayor a 18 anios. 10

import os
os.system("cls")
#mi solucion del ejercicio
# edad = int(input("cuantos anios tenes? "))

# if edad > 18:
#     print("Tu entrada cuesta 10")
# elif edad >4:
#         print("Tu entrada cuesta 5")
# elif edad <=3:
#       print("tu entrada es gratis")
# else:
#       print("error en el ingreso de datos")

#solucion del ejercicio

edad = int(input("introduce tu edad: "))
#decision del precio en funcion de la edad

if edad < 4:
      precio = 0
elif edad <= 18:
      precio = 4
else:
      precio = 10

#mostrar precio

print("El precio de la entrada es", precio)