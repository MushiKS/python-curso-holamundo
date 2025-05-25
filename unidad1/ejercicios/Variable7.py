import os
#módulo de funciones limpieza de pantalla
os.system("cls")
# Solicitando datos de tipo numérico por pantalla
# Funcion INT que convierte el valor en número para que se pueda calcular
Precio1=int(input("Ingrese el primer precio: "))
Precio2=int(input("Ingrese el segundo precio: "))
Total=Precio1+Precio2
print(f"El primer precio es: {Precio1}")
print(f"El segundo precio es: {Precio2}")
#F de Format
print(f"El precio total es: {Total}")
print("Otra forma de mostrar")
print("El primer precio es: ",Precio1)
print("El segundo precio es: ",Precio2)
print("El precio total es: ",Total)