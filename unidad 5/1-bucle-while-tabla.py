import os
os.system("cls")

# Calcular la tabla de multiplicar del 1 al 10 de un número cualquiera con bucle FOR y WHILE

numero = int(input("introduzca un número: "))
print("****  TABLA DE MULTIPLICAR ****")

# Tabla de multiplicar usando FOR
for i in range(1, 11):
    print(numero * i)

# Tabla de multiplicar usando WHILE
i = 1
while i < 11:
    print(numero * i)
    i = i + 1