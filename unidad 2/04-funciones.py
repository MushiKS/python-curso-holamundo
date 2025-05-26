import os
os.system("cls")

def promedioNotas(notas1,notas2,notas3):
    promedio=(notas1 + notas2 + notas3) / 3
    #que la función va a devolver un resultado
    return promedio

#estamos en el programa principal 
promedio1 =promedioNotas(9, 7, 8)
promedio2 =promedioNotas(7, 7, 7)
promedio3 =promedioNotas(9, 7, 10)


print("devuelve el promedio de 9, 7, 8 :", promedio1)
tecla = input("presione alguna tecla...")
print("devuelve el promedio de 7, 7, 7 :", promedio2)
tecla = input("presione alguna tecla...")
print("devuelve el promedio de 9, 7, 10 :", promedio3)