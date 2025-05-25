import os
os.system("cls")

Sucursal=input("Introduzca el Nombre de la Sucursal: ")
Venta1=int(input("Introduzca el Precio de la 1ra venta: "))
Venta2=int(input("Introduzca el Precio de la 2da venta: "))
Venta3=int(input("Introduzca el Precio de la 3ra venta: "))
Texto1="La sucursal "
Texto2=" ha hecho tres ventas de "
Total=Venta1+Venta2+Venta3
print (Texto1+Sucursal+Texto2+f"{Venta1}, {Venta2} y {Venta3} pesos, "
       + f" dando un total de {Total} Pesos")
print("De que otra forma podría ser la salida impresa???")