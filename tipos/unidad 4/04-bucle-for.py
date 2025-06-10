#EJEMPLO BUCLE FOR
import os
os.system("cls")
#iniciamos los contadores y el acumulador en 0
#comienzo del ciclo que se repite 4 veces
#ciclo determinado

for i in range(4):
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    #muestro cada uno de los datos
    print("** MUESTREO DE DATOS **")
    print(nombre+" "+apellido)
#se cierra el ciclo
print("MUESTREO DE RESULTADOS")
print("FIN DEL PROGRAMA")
