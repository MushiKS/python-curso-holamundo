import os 
os.system("cls")

#1 Concatenacion de listas

lista1 = [1, 2, 3]
lista2 = [45, 99, 218]
lista3 = lista1 + lista2
print (lista3)
input()
lista4 = ["Javier","Laura","Irene","Matias","jose"]
lista3 = lista1 + lista4
print(lista3)
input()


#2 valor maximo y minimo

a = max(lista1)  # Devuelve el valor máximo de la lista lista1 (en este caso, el número más grande)
print(a)
input()

a = min(lista2)  # Devuelve el valor mínimo de la lista lista2 (en este caso, el número más pequeño)
print(a)
input()

#3 contar cantidad total de elementos

a = len(lista2)  # Devuelve la cantidad de elementos que tiene la lista lista2
print(a)
input()

a = len(lista3)  # Devuelve la cantidad de elementos que tiene la lista lista3
print(a)