#EJERCICIO BUCLE    

import os
os.system("cls")
#calcula la tabla de multiplicar del 1 al 10 de un numero cualquiera

numero = int(input("introduzca un numero: "))
print("***** TABLA DE MULTIPLICAR ******")
# i  es como un contador interno pero arranca de 0

for i in range(10):
    print(numero,"*",i,"=",numero * i)
input()
os.system("cls")

print("**** TABLA DE MULTIPLICAR *****")
for i in range(1,11):
    print(numero,"*",i,"=",numero * i)