#VERDADERA. EN PYTHON LOS BUCLES WHILE SE UTILIZAN PRINCIPALMENTE CUANDO EL NUMERO DE ITERACIONES NECESARIAS
#EL CICLO WHILE DE PYTHON HACE QUE SE EJECUTE UN BLOQUE DE CODIGO REPETIDAMENTE MIENTRAS UNA CONDICION SEA
#NO VIENE DETERMINADO DE ANTEMANO

import os
os.system("cls")
#clave de corte while
respuesta = "si"
cont = 0
suma = 0
mayor = 0
menor = 0
while respuesta == "si":
    name = input("nombre: ")
    edad = int(input("edad: "))
    cont = cont + 1
    suma = suma + edad
    if edad>= 21:
        mayor = mayor + 1
    else:
        menor = menor + 1
    print("MUESTREO DE DATOS INGRESADOS")
    print("su nombre es:",name,"su edad es ",edad,"anios")
    respuesta = input("desea seguir ingresando si/no:")
print("sos libre del bucle while")