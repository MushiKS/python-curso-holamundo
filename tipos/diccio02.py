import os
os.system("cls")

#1 un diccionario puede tener diferentes tipos de valores

diccionario2 = {"Codigo":1001,"Color":"Verde","Talle":"L","Precio":1200}
print(diccionario2)
input()

#2 Copiar un diccionario a otro

diccionario3 = diccionario2.copy()
print(diccionario3)
input()

#3 Borrar un diccionario

diccionario3.clear()
print(diccionario3)
input()

#4 Ver TODAS las claves de un diccionario
print(diccionario2.keys())
input()

#5 ver TODOS los valores de un diccionario

print(diccionario2.values())
input()