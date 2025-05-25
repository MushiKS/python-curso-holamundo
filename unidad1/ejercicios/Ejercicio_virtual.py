#Ingresar dos edades, sumarlas. Mostrar datos y resultados.
import os
#módulo de funciones limpieza de pantalla
os.system("cls")
Edad1=int(input("Ingrese la primer edad: "))
Edad2=int(input("Ingrese la segunda edad: "))
Suma=Edad1+Edad2
Resta=Edad1-Edad2
Multi=Edad1*Edad2
Divi=Edad1/Edad2
Divi2=Edad1//Edad2
print("La primer edad es: ",Edad1)
print("La segunda edad es: ",Edad2)
#F de Format
print("SUMA: ",Suma)
print("RESTA: ",Resta)
print("PRODUCTO: ",Multi)
print("DIVISIÓN: ",Divi)
print("DIVISIÓN: ",Divi2)
