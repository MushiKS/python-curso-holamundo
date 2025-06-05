#1 ingresar estos datos: nombre, apellido y edad de una persona
# si la edad es mayor o igual a 18 años, mostrar el nombre
# si la edad es menor a 18 años, mostrar apellido


# name = input("cual es tu nombre? ")
# apellido = input("cual es tu apellido? ")
# edad = int(input("Cual es tu edad? "))

# if edad >=18:
#     print("tu nombre es :",name)
# else:
#     print("tu apellido es ",apellido)


#2ingresar dos numeros, mostrar el mayor

# numero1 = int(input("ingresa un número: "))
# numero2 = int(input("ingresa un número: "))

# if numero1 > numero2:
#     print(numero1)
# else: 
#     print(numero2)
    
#3ingresar un numero. determinar si es positivo(>=0) o negativo

# numero1 = int(input("ingresa un número: "))

# if numero1 >=0:
#     print("tu numero es positivo")
# else:
#     print("tu numero es negativo")
    
    
# 4 ingresar dos numeros. si la suma de ambos es mayor o igual a 100. mostrar el primer numero, sino, mostrar el segundo

# numero1 = int(input("ingresa un número: "))
# numero2 = int(input("ingresa un número: "))

# suma = numero1 + numero2

# if suma >= 100:
#     print(numero1)
# else:
#     print(numero2)


# 5 ingresar apellido y el codigo de categoria. segun el codigo de categoria determinar categoria y el sueldo
# calcular  el 11% de jubilación - calcular la ley 19032 que es el 3% sobre el sueldo - calcular el total a cobrar sabiendo que es el sueldo
# ley 19032 - jubilacion
apellido = input("Cual es tu apellido? ")
categoria = input("Cual es tu codigo de categoria: ")

if categoria == "a":
    categoria_nombre = "Vendedor"
    sueldo = 750000 * 3 / 100 
    jubilacion = 750000 * 11 / 100
elif categoria == "b":
    categoria_nombre = "Administrador"
    sueldo = "820.000"
elif categoria == "c":
    categoria_nombre = "Cajero"
    sueldo = "780.000"
else:
    categoria_nombre = "ERROR 404"
    sueldo = "error"

print(f"Tu categoria es: {categoria_nombre} y tu sueldo es: {sueldo}")
