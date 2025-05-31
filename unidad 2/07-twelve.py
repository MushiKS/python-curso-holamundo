import os 
os.system("cls")

#los lados de un triangulo equilatero miden 4cm
#calcular su area y su perimetro. mostrar datos y resultados

from math import sqrt

lados = 4
mitadtriangulo = 2
perimetro = (lados * 3)
h = sqrt(lados * 3)
area = (lados * h) / 2

print("la altura es:", h)
print("El perimetro es: ", perimetro)
print("El area es: ", area)