import os
os.system("cls")

email = input("Ingrese dirección de email: ")

contador = 0

#recorre cada uno uno de los caracteres de una variable tipo texto 
#el bucle se repite tantas veces como caracteres tenga la variable email
    
for i in email:
    if i=="@":
        contador+= 1
    
if contador==0:
    print("la dirección no tiene arroba")
elif contador==1:
    print("la direccion tiene formato correcto")
else:
    print(f"la direccion tiene mas de un arroba,tiene {contador}")