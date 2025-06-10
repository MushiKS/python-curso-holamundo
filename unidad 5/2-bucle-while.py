import os
os.system("cls")

print("*** CALCULO DE DOS NUMEROS **")
num1 = int(input("introduzca el 1er numero: "))  # Pide el primer número al usuario
num2 = int(input("introduzca el 2er numero: "))  # Pide el segundo número al usuario

op = 0  # Inicializa la variable de opción

# Bucle para validar que la opción esté entre 1 y 4
while op < 1 or op > 4:
    print("1 - suma")
    print("2 - resta")
    print("3 - multiplicacion")
    print("4 - division")
    op = int(input("introduzca una opción: "))

# Realiza la operación seleccionada
if op == 1:
    print("resultado: ", num1 + num2)         # Suma
elif op == 2:
    print("resultado: ", num1 - num2)         # Resta
elif op == 3:
    print("resultado: ", num1 * num2)         # Multiplicación
else:
    print("resultado: ", num1 / num2)         # División