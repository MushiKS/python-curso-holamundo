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

# MAS COMPACTO EL WHILE PARA VALIDAR OPCIONES
# while area not in ("ADM", "NAT", "TEC"):


#INICIALIZAMOS VARIABLES DE TIPO CONTADOR
cipo,nqn,generalR,plot = 0,0,0,0
a,b,c,d,e=0,0,0,0,0
ad,nr,te=0,0,0
p,v,m=0,0,0
ef,ta=0,0
acuimpTotal=0
acuEfectivo=0
acuTarjeta=0
acuTotal=0
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
    a=a+1
elif codS =="B":
    sem = "LIDERAZGO SIGLO XXI"
    imp = 8900
    b=b+1
elif codS =="C":
    sem = "ADMINISTRACION DE LOS RECURSOS HUMANOS"
    imp = 10500
    c=c+1
elif codS =="D":
    sem = "NUEVAS TECNOLOGIA DE SOFTWARE"
    imp = 11000
    d=d+1
else:
    sem = "INFORMATICA EN LA NUBE"
    imp = 14900
    e=e+1

#GENERAMOS EL AREA DE FORMACION TENIENDO EN CUENTA EL CODIGO DE FORMACION

if area =="ADM":
    form ="ADMINISTRATIVAS"
    ad=ad+1
elif area =="NAT":
    form ="NATURALES Y RENOVABLES"
    nr=nr+1
else:
    form ="TECNOLOGIA"
    te=te+1

#GENERAMOS LA LOCALIDAD SEGUN EL CODIGO DE LOCALIDAD
if loc =="C":
    localidad="CIPOLLETTI"
    cipo = cipo+1
elif loc =="N":
    localidad="NEUQUEN"
    nqn= nqn+1
elif loc=="R":
    localidad="General Roca"
    generalR = generalR+1
else:
    localidad="PLOTITER"
    plot= plot+1

#GENERAMOS LA MODALIDAD Y EL LUGAR SEGUN EL CODIGO DE TIPO DE MODALIDAD
if tm=="P":
    modalidad = "PRESENCIAL"
    lugar = "AULA MAGNA"
    p=p+1
elif tm=="V":
    modalidad = "VIRTUAL"
    lugar = "ZOOM"
    v=v+1
else:
    modalidad = "MIXTO"
    lugar = "MAGNA+ZOOM"
    m=m+1

#CALCULAR EL IMPORTE TOTAL
imptotal = imp*cant
if tp=="E":
    pago="EFECTIVO"
    desc= 5/100
    rec=0
    ef=ef+1
else:
    pago="TARJETA"
    rec= 10/100
    desc=0
    ta=ta+1
total=imptotal -(imptotal*desc)+(imptotal*rec)

#ACA HAGO LOS ACUMULADORES
acuimpTotal = acuimpTotal + imptotal
acuEfectivo = acuEfectivo+(imptotal*desc)
acuTarjeta = acuTarjeta+(imptotal*rec)
acuTotal = acuTotal+total

#ACA VIENE EL MUESTREO DE DATOS

print("MUESTREO DE DATOS")
print()
print("*ID: ",id,"*NOMBRE: ",nom,"*APELLIDO: ",ape)
print("*EDAD: ",edad,"*CODIGO DE LOCALIDAD: ",loc,"LOCALIDAD: ",localidad)
print("*CODIGO DE FORMACION: ",area,"AREA DE FORMACION: ",form)
print("*CODIGO DE SEMINARIO: ",codS,"SEMINARIO: ",sem,"IMPORTE: ",imp)
print("*CODIGO DE MODALIDAD: ",tm,"*MODALIDAD: ",modalidad,"LUGAR: ",lugar)
print("*CANTIDAD DE ENCUENTROS: ",cant)
print("*FORMA DE PAGO: ",tp,"PAGO EN: ",pago)
print("Total a pagar: ",total)
print("**************")
print()

