#no tiene dato ni retorno

def promedioNotas():
    #asignaciones - le digo a la variable nota1 tiene valor de 8
    print("Aca estamos dentro de la función")
    nota1 = 8
    nota2 = 10
    nota3 = 6
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"el promedio es: {promedio}")
    print("hola como estas?estamos terminando la función")
    
#llamo a la funcion sin parametros ni retorno
print("Estamos en el programa principal")
tecla = input("ingrese una tecla para continuar")
promedioNotas()
print("Volvemos a estar en el programa principal")