import os
os.system("cls")

lista2 = ["Javier", "Laura", "Irene", "Matias", "Jose"]

#1 Formas de agregar datos

lista2.append("Juan")
print(lista2)
input()

lista2.extend(["Marcela", "Claudia"])
print(lista2)
input()

lista2.insert(0,"Ramiro")
print(lista2)
input()

#2 Formas de eliminación de datos

lista2.pop()
print(lista2)
input()
lista2.pop(3)
print(lista2)
input()
lista2.remove("Laura")
print(lista2)
input()