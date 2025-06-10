#ingresar edad y deporte. segun la edad determinar la categoria: mostrar datos y resultados
# <=13 es infatiles
# <=15 es cadetes
# <=18 juveniles
# otro> es mayores
import os
os.system("cls")

edad = int(input("edad: "))
deporte = input("ingrese su deporte: ")

if edad <= 13:
    categoria = "infatiles"
elif edad <= 15:
    categoria = "cadetes"
elif edad <= 18:
    categoria = "juveniles"
elif edad > 18:
    categoria = "mayores"


print(f"El chico está en la categoría de {categoria} con la edad de {edad}")