#los alumnos de un curso se han dividido en dos grupos
# A y B de acuerdo al sexo y nombre. el grupo A esta formado por las mujeres
# con un nombre anterior a la M y a los hombres con un nombre posterior a la N y en el 
#grupo B por el resto. escribir un programa que pregunte al usuario su nombre, sexo
#y muestre por pantalla al grupo que le corresponde

sexo = input("Cual es tu genero? responder con M o F")
nombre = input("cual es tu nombre ")

if sexo == "M" and nombre.upper()[0] < "N":
    print("Entra en el grupo A")
elif sexo == "F" and nombre.upper()[0] < "M":
    print("Esta en el grupo A")
else:
    print("Estas en el grupo B")