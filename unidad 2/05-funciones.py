import os
os.system("cls")

def promedioNotas(notas1, notas2, notas3):
    print("Ahora estoy en la función")
    input()
    promedio = (notas1 + notas2 + notas3) / 3
    print("ya hizo el calculo y ahora lo retorna")
    input()
    return promedio

print("calculo de promedio de notas de alumnos")
print()
nombre1 = input("Ingrese el nombre del alumno: ")
nota1 = int(input("Ingrese la 1er nota del alumno: "))
nota2 = int(input("Ingrese la 2er nota del alumno: "))
nota3 = int(input("Ingrese la 3er nota del alumno: "))
#llamo a la función y paso las 3 notas que ingreso por teclado
#promedio1=promedioNotas(7, 8, 9)
promedio1 = promedioNotas(nota1, nota2, nota3)
print(f"El promedio de {nombre1} es {promedio1}")