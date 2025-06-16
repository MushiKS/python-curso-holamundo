import os
os.system("cls")
#id: 1-2-3
#se van generando a medida
#que los profesores se van inscribiendo 
#repetir el ciclo 3 veces
#apellido mayuscula-nombre propio
#edades permitidas entre 30 y 60
# area de información : ADM - NAT - TEC
#codigo de localidad: C/N/R/P
#Codigo de seminario: . A/B/C/D/E
#Tipo de Modalidad: P/V/M  
#Cantidad de encuentros: valores entre 1 y 5
#Tipo de Pago: E/T



#id: 1-2-3 se van generando a medida que los profesores se van inscribiendo 
for i in range(3):
    print("INGRESO DE DATOS")
    id= i + 1
    ape = input("Ingrese su apellido: ").upper()
    nom = input("Ingrese su nombre: ").capitalize()
    edad = int(input("Ingrese su edad entre 30 y 60 años: "))
    while edad < 30 or edad > 60:
        print("Edad incorrecta - vuelve a ingresar")
        edad = int(input("Ingrese su edad entre 30 y 60 años: "))

    #Área: ADM, NAT, TEC
    area = input("ingrese una area de información: ADM - NAT - TEC: ").upper()
    while area!="ADM" and area!="NAT" and area!="TEC":
        print("Datos incorrectos, vuelve a ingresar")
        area = input("ingrese una area de información: ADM - NAT - TEC: ").upper()

        #Localidad: C, N, R, P
    loc = input("Ingrese su codigo de localidad: C/N/R/P ").upper()
    while loc!="C" and loc!="N" and loc!="R" and loc!="P":
         print("Dato incorrecto, vuelva a ingresar")
         loc = input("Ingrese su codigo de localidad: C/N/R/P ").upper()


    #Seminario: A, B, C, D, E
    codS = input("Ingrese su codigo de seminario: A-B-C-D-E ").upper()
    while codS!="A" and codS!="B" and codS!="C" and codS!="D" and codS!="E":
        print("Dato incorrecto, vuelva a ingresar A-B-C-D-E")
        codS = input("Ingrese su codigo de seminario: A-B-C-D-E ").upper()


    #Modalidad: P, V, M 
    tm = input("Ingrese tipo de modalidad: P/V/M ").upper()
    while tm!="P" and tm!="V" and tm!="M":
        print("Dato incorrecto, vuelva a ingresar: P/V/M")
        tm = input("Ingrese tipo de modalidad: P/V/M ").upper()

    #Cantidad de encuentros entre 1 y 5 
    cant = int(input("Ingrese cantidad de encuentros entre 1 y 5: "))
    while cant<1 or cant>5:
        print("Dato incorrecto, vuelva ingresar entre 1-5")
        cant = int(input("Ingrese cantidad de encuentros entre 1 y 5: "))


    #Tipo de pago: E, T
    tp = input("Ingrese el tipo de pago E/T ").upper()
    while tp!="E" and tp!="T":
        print("Dato incorrecto, vuelva a ingresar. E/T")
        tp = input("Ingrese el tipo de pago E/T ").upper()

#ACA DESARROLLAMOS LA PARTE 2 DE LA ACTIVIDAD INTEGRADORA


print("MUESTREO DE DATOS")
print()
print("*ID: ",id,"*NOMBRE: ",nom,"*APELLIDO: ",ape)
print("*EDAD: ",edad,"*LOCALIDAD",loc,)
print("AREA DE FORMACION: ",area)
print("SEMINARIO: ",codS,"*MODALIDAD: ",tm)
print("CANTIDAD DE ENCUENTROS",cant)
print("FORMA DE PAGO: ",tp)
print("**************")
print()
os.system("cls")

