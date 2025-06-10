import os
os.system("cls")

# Inicialización de contadores y acumuladores
mayor = 0
menor = 0
adm, ven, caj = 0, 0, 0
sumaSueldo, sumaEdad = 0, 0

for i in range(3):
    nom = input("ingrese su nombre: ").lower()
    apen = input("ingrese su apellido: ").capitalize()
    edad = int(input("Ingrese su edad: "))
    # Validación de edad
    while edad < 20 or edad > 60:
        print("dato erroneo, edades entre 20 y 60 años")
        edad = int(input("vuelve a introducir tu edad: "))
    cat = input("Ingrese categoria de cargo A-B-C ").upper()
    # Validación de categoría
    while cat not in ("A", "B", "C"):
        print("dato erroneo,valores permitidos A-B-C")
        cat = input("Ingrese una categoria de cargo A-B-C ").upper()
    # Asignación de rubro y sueldo según categoría
    if cat == "A":
        rubro = "Administrativo"
        sueldo = 1500000
        adm += 1
    elif cat == "B":
        rubro = "VENTAS"
        sueldo = 1600000
        ven += 1
    else:
        rubro = "CAJERO"
        sueldo = 1800000
        caj += 1
    # Contar mayores y menores de 21
    if edad > 21:
        mayor += 1
    else:
        menor += 1
    # Acumular edades y sueldos
    sumaEdad += edad
    sumaSueldo += sueldo
    # Mostrar datos de cada persona
    print("** MUESTREO  DE DATOS **")
    print("Su nombre es:", nom, "y su apellido es", apen, "y tiene", edad, "años")
    print("su rubro es", rubro, "y sueldo es", sueldo)

# Mostrar resultados finales
print("** MUESTREO DE RESULTADOS **")
print("la cantidad de mayores es:", mayor)
print("la cantidad de menor es", menor)
print("la suma de todas las edades es", sumaEdad)
print("la suma de los sueldos es", sumaSueldo)
print("RUBRO A:", adm, "RUBRO B", ven, "RUBRO C", caj)
print("FIN DEL PROGRAMA")

#upper --> transformar todo a MAYUSCULA
#lower --> transformar todo a minuscula
#capitelize --> transformar todo al formato nombre propio (Nombre)
#ACUMULADOR - SUMADOR --> acu = acu + precio
#CONTADOR --> cantidad = cantidad + 1