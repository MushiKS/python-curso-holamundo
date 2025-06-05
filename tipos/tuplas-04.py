import os
os.system("cls")

# 1. Creación de tuplas

tupla1 = (1, 2, 3)  # Tupla de números enteros
tupla2 = ("javier", "Laura", "Irene", "Matias", "jose")  # Tupla de cadenas de texto
lista3 = ["Juan perez", 45, True]  # Lista (no tupla)

tupla3 = tuple(lista3)  # Convierte la lista en una tupla

# 2. Acceder a los datos de una tupla

print(tupla2)  # Imprime toda la tupla2
input()

print(tupla2[3])  # Imprime el elemento en la posición 3 de tupla2 ("Matias")
input()

print(tupla3[2])  # Imprime el elemento en la posición 2 de tupla3 (True)
input()

print(len(tupla1))  # Imprime la cantidad de elementos en tupla1 (3)
input()

print(len(tupla2))  # Imprime la cantidad de elementos en tupla2 (5)
input()

print(tupla3.count(45))  # Cuenta cuántas veces aparece el valor 45 en tupla3 (1 vez)
input()

# Desempaquetado de tupla: asigna cada valor de tupla3 a una variable
nombre, edad, casado = tupla3
print("El sr " + nombre + f" tiene {edad}" + " anios ")