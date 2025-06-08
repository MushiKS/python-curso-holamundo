#En una determinada empresa, sus empleados son evaluados al final de cada año
#los puntos que pueden obtener en la evaluacion comienzan con 0.0 y pueden ir aumentando
#traduciendose en mejores beneficios. los puntos que pueden conseguir los empleados pueden ser
# 0.0, 0.4, 0.6 o mas, pero no valores intermedios entre las cifras mencionadas. 
#a continuacion se muestran una tabla con los niveles correspondientes a cada puntuacion,
# la cantidad de dinero conseguida en cada nivel es de 2400 multiplicada por la puntuacion
# de nivel

# import os
# os.system("cls")
# #mi ejercicio
# puntaje = float(input("Ingrese su puntaje: " ))

# if puntaje >= 0.6:
#     dinero = 2400 * puntaje
#     obtenido = dinero
#     print("tu puntaje es meritorio, obtienes", obtenido)
# elif puntaje >= 0.4:
#     dinero = 2400 * puntaje
#     obtenido = dinero
#     print("tu puntaje es aceptable", obtenido)
# elif puntaje >= 0.1 :
#     dinero = 2400 * puntaje
#     obtenido = dinero
#     print("tu puntaje es inaceptable", obtenido)
# else:
#     print("no has obtenido nada por tu mal desempenio")


#resultado del ejercicio

bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6

puntos = float(input("introduce tu puntuacion : "))
#clasificacion de niveles de rendimiento

if puntos == inaceptable:
    nivel = "inaceptable"
elif puntos == aceptable:
    nivel = "aceptable"
elif puntos == meritorio:
    nivel = "meritorio"
else:
    nivel = ""

#Mostrar nivel de rendimiento

if nivel == "":
    print("tu puntuacion no es valida")
else:
    print("Tu nivel de rendimiento es: ",nivel )
    print("Te corresponde cobrar un ", puntos * bonificacion )