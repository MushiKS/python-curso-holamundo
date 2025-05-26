import os
os.system("cls")
#creamos una función con parametros que pasamos por codigo

def promedioNotas(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    #muestro el resultado dentro de la función
    print(f"el promedio es: {promedio}")


print("Estamos en el programa principal")
print("llama a la función con los valores 7,8,9")
promedioNotas(7,8,9)

tecla = input("Ingrese una tecla para continuar")
print("Llama a la función con los valores 10,10,10")
promedioNotas(10,10,10)

tecla = input("Ingrese una tecla para continuar")
print("llama a la función con los valores 9,7,10")
promedioNotas(9,7,10)

tecla = input("Ingrese una tecla para continuar")
print("listo") 