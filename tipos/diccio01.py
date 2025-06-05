#diccionario
import os
os.system("cls")

#1 creación

diccionario1 = {"FCB":"Barcelona","CHE":"Chelsea","MIL":"Milan","PSG":"Paris SG"}
print(diccionario1)
input()

#2 ver un elemento del diccionario por su clave
print(diccionario1["CHE"])
input()

#3 Agregar un elemento

diccionario1["RMA"] = "real madrid"
print(diccionario1)
input()

#4 modificar un elemento

diccionario1["RMA"] = "Real Madrid"
print(diccionario1)
input()

#5 eliminar un elemento
del diccionario1["CHE"]
print(diccionario1)
input()
