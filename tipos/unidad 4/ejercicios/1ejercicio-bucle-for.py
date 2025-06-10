#Ingresar un numero y determinar si es negativo, postivo o neutro. contar los positivos, negativos y neutros
#Mostrar datos y resultados

import os
os.system("cls")

negativo = 0
positivo = 0
neutro = 0

for i in range(5):
    numero = int(input("numero: "))
    if numero>0:
        positivo = positivo + 1
        print("es positivo")
    elif numero==0:
        neutro = neutro + 1
        print("es neutro")
    else:
        negativo = negativo + 1
        print("es negativo")
        
print(f"Cantidad de positivos: {positivo}")
print(f"Cantidad de negativos: {negativo}")
print(f"Cantidad de neutros: {neutro}")
