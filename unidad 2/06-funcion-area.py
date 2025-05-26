import os
os.system("cls")

def area_cuadrado(lado):
    ar = lado * lado
    return ar

def perimetro_cuadrado(lado1):
    p = 4 * lado1
    return p

lado= int(input("Ingrese lado del cuadrado : "))
area = area_cuadrado(lado)
perimetro = perimetro_cuadrado(lado)  # Corregido aquí
print(f"el area es: {area}")
print(f"el perimetro es: {perimetro}")