#Nombre y Apellido de un alumno
#Nombre de la materia - #3 notas
#Calcular la suma de las notas
#Calcular el promedio de las notas - Mostrar datos

import os
os.system("cls")
#ingreso el nombre por teclado y se guarda en la variable nom
nom=input("Ingrese su nombre: ")
#ingreso el apellido por teclado y se guarda en la variable ape
ape=input("Ingrese su apellido: ")
#ingreso la materia por teclado y la guardo en mate
mate=input("Ingrese el nombre de la materia: ")
#ingreso en tres variables 3 notas. Le coloco el int
#para que python sepa que es un numero
nota1=int(input("Ingrese su 1° nota: "))
nota2=int(input("Ingrese su 2° nota: "))
nota3=int(input("Ingrese su 3° nota: "))
#aca voy a sumar las tres notas y se va a guardar en la variable suma
suma=nota1+nota2+nota3
#aca voy a promediar las notas y voy a guardar en la variable prome
prome=suma/3
#vamos a mostrar todos los datos y resultados
print("Su nombre es: ",nom)
print("Su apellido es: ",ape)  
print("Su materia es: ",mate)
print(f"Su primer nota es: {nota1}: ")
print(f"Su segunda nota es: {nota2}: ")
print(f"Su tercer nota es {nota3} :")
print(f"La suma de las tres notas es {suma}: ")
print(f"El promedio de las tres notas es {prome}: ")
print
print("** PROGRAMA FINALIZADO CON EXITO **")
input("Ingrese una tecla para continuar...:")