import os
import re

os.system("cls")

#BUSQUEDA CON FINDALL PARA VER TODOS LOS CASOS

cadena= input("Introduzca un texto: ")
buscar= input("Introduzca texto a buscar: ")

print(re.findall(buscar,cadena))
print(len(re.findall(buscar, cadena)))