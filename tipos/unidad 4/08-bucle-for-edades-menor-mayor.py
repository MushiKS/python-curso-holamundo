#BUCLE FOR EJEMPLO 2
import os
os.system("cls")
#iniciamos los contadores y acumulador en 0
cont = 0
mayor = 0
menor = 0
suma = 0
acumulador = 0
# comienzo del ciclo se repite 4 veces
#ciclo determinado

for i in range(4):
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = int(input("edad: "))
    # acumulo las edades
    acumulador = acumulador + edad
# cuento la cantidad de mayores y menores que 30
    if edad >= 30:
        # cuenta las personas mayores que 30
        mayor = mayor + 1
        categoria = "mayor de 30 años"
    else:
        # cuenta las personas menores a 30
        menor = menor + 1
        categoria = "menor de 30 años"
    # MUESTREO DE CADA UNO DE LOS DATOS
    print("MUESTREO DE DATOS")
    print(nombre + " " + apellido + " " + f"{edad} y su categoria es {categoria}")
    #se cierra el ciclo
print("MUESTREO DE RESULTADOS")
print(f"la suma de las edades es: {acumulador}")
print(f"la cantidad de mayores es: {mayor}")
print(f"la cantidad de menores es: {menor}")
print("fin del programa")