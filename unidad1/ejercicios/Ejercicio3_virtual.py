import os
os.system("cls")

Cliente=input("Introduzca el Nombre del Cliente: ")
Precio1=int(input("Introduzca el Precio de la 1ra compra: "))
Precio2=int(input("Introduzca el Precio de la 2da compra: "))
Total=Precio1+Precio2
print ("El cliente "+Cliente+f" ha comprado dos productos por el valor de {Precio1}"
       + f" y {Precio2} pesos, totalizando una compra de {Total} Pesos")
