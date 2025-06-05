import os
os.system("cls")
lista2 = ["Araceli", "Laura", "Juan", "Irene", "Samuel", "Jose", "Laura"]

#1 Formas de ordenar una lista

lista2.reverse()  # Invierte el orden actual de la lista (el último pasa a ser el primero)
print(lista2)
input()

lista2.sort()  # Ordena la lista en orden alfabético ascendente (de la A a la Z)
print(lista2)
input()

lista2.sort(reverse=True)  # Ordena la lista en orden alfabético descendente (de la Z a la A)
print(lista2)
input()

#2 formas de buscar un valor en una lista

a = lista2.count("Laura")  # Cuenta cuántas veces aparece "Laura" en la lista
print(a)
input()

a = lista2.count("xxxx")  # Cuenta cuántas veces aparece "xxxx" en la lista (devuelve 0 si no está)
print(a)
input()

a = lista2.index("Juan")  # Devuelve el índice (posición) de la primera aparición de "Juan"
print(a)
input()

a = lista2.index("Laura")  # Devuelve el índice de la primera aparición de "Laura"
print(a)
input()

a = lista2.index("Laura", 2, 5)  # Busca "Laura" entre los índices 2 (incluido) y 5 (excluido) y devuelve su posición
print(a)
input()