# para tributar un determinado impuesto se debe ser mayor de 16 
# ano y tener ingresos iguales o superiores a 1000 mensuales
# escribir un programa que pregunte al usuario su edad
#y sus ingresos mensuales y muestre por pantalla si el usuario 
#tiene que tributar o no

edad = int(input("cuantos años tenes"))
sueldo = int(input("Cual es tu sueldo?"))

if edad > 16 and sueldo > 1000:
    input("Puede tributar sus impuestos")
else:
    input("No puede tributar impuestos")