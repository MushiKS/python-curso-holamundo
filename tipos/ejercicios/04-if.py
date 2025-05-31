# escribir un programa que pida al usuario un numero entero
#y muestre por pantalla si es par o impar

numero = int(input("Ingresa un numero: "))

resultado = numero % 2
# if numero % 2 == 0:
if resultado == 0:
    print("el numero es par")
else:
    print("el numero es impar")