import os
#módulo de funciones limpieza de pantalla
os.system("cls")
#1 - Ingresar datos.
Nombre=input("Ingrese su nombre: ")
Apellido=input("Ingrese su apellido: ")
Direccion=input("Ingrese su dirección: ")
Edad=int(input("Ingrese su edad: "))
#Muestra los datos ingresados
print("** MUESTREO DE DATOS **")
print("Su nombre es: "+Nombre)
print("Su apellido es: "+Apellido)
print("Su dirección es: "+Direccion)
print("Su edad es: ",Edad)
print("** OTRA FORMA DE MOSTRAR **")
print ("HOLA "+Nombre+" "+Apellido+" "+Direccion+ " como te va?")
print(Nombre+" "+Apellido+" Vive en "+Direccion)
print("** FIN DE PROGRAMA **")

