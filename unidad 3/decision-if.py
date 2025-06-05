import os
os.system("cls")
print("**CARGA DE DATOS - PROMOCIONES **")
name = input("Ingrese su nombre")
materia = input("Ingrese su materia")
notaParcial = int(input("Ingrese su nota: "))

# >=7 promoción
# >=5 regular
# >=3 libre 4-3
# <3 insuficiente 2-1

if notaParcial >= 7:
    condicion = "promocion"
    final = "no"
    nota = notaParcial
elif notaParcial >=5:
    condicion = "regular"
    final = "coloquio"
    nota = notaParcial
elif notaParcial >=3:
    condicion = "libre"
    final = "si"
    nota = notaParcial
else:
    condicion = "insuficiente"
    final = "recursa"
    nota = notaParcial

print("El alumno se llama ",name, "y la materia que cursa es: ",materia)
print("Su condición es:",condicion,"y su final es ", final)
print("La nota del estudiante es: ", nota)