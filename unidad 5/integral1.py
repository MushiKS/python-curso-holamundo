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
#GENERAMOS SEMINARIO E IMPORTE SEGUN CODIGO DE SEMINARIO

if codS =="A":
    sem = "IA EN LAS AREAS NATURALES"
    imp =  12500
elif codS =="B":
    sem = "LIDERAZGO SIGLO XXI"
    imp = 8900
elif codS =="C":
    sem = "ADMINISTRACION DE LOS RECURSOS HUMANOS"
    imp = 10500
elif codS =="C":
    sem = "NUEVAS TECNOLOGIA DE SOFTWARE"
    imp = 11000
else:
    sem = "INFORMATICA EN LA NUBE"
    imp = 14900

#GENERAMOS EL AREA DE FORMACION TENIENDO EN CUENTA EL CODIGO DE FORMACION

if area =="ADM":
    form ="ADMINISTRATIVAS"
elif area =="NAT":
    form ="NATURALES Y RENOVABLES"
else:
    form ="TECNOLOGIA"

#GENERAMOS LA LOCALIDAD SEGUN EL CODIGO DE LOCALIDAD
if loc =="C":
    localidad="CIPOLLETTI"
elif loc =="N":
    localidad="NEUQUEN"
elif loc=="R":
    localidad="General Roca"
else:
    localidad="PLOTITER"

#GENERAMOS LA MODALIDAD Y EL LUGAR SEGUN EL CODIGO DE TIPO DE MODALIDAD
if tm=="P":
    modalidad = "PRESENCIAL"
    lugar = "AULA MAGNA"
elif tm=="B":
    modalidad = "VIRTUAL"
    lugar = "ZOOM"
else:
    modalidad = "MIXTO"
    lugar = "MAGNA+ZOOM"

#CALCULAR EL IMPORTE TOTAL
imptotal = imp*cant
 

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

