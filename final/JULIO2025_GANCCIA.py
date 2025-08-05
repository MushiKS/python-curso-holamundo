# FINAL DE INTRODUCCION AL PENSAMIENTO LOGICO - GANCCIA MATIAS

# El usuario elige cuántos registros desea ingresar
cantidad = int(input("cuantos registros desea ingresar?: "))
while cantidad <= 0:
    print("La cantidad debe ser un número entero mayor que cero. Intente de nuevo.")
    cantidad = int(input("¿Cuántos registros desea ingresar?: "))
# iniciamos las listas
names = []
disciplinas = []
puntos = []
niveles = []
sanciones = []
promedios = []
promedios_sanciones = []
desempenos = []


# FUNCIONES
def promedio_puntos(lista_puntos):
    return sum(lista_puntos) / len(lista_puntos)


def promedio_sanciones(lista_sanciones):
    return sum(lista_sanciones) / len(lista_sanciones)


# creamos el for i in range para la cantidad que pone el usuario
for i in range(cantidad):
    name = input("Ingrese el nombre del equipo/participante: ").upper()
    while name == "":
        print("Dato incorrecto, vuelva a ingresar el nombre.")
        name = input("Ingrese el nombre del equipo/participante: ").upper()
    names.append(name)

    # creamos el while para la selección de disciplina, si pone uno que no es, lo vuelve a preguntar
    disciplina = input(
        "Ingrese la disciplina (FUTBOL/BASQUET/VOLEY): ").upper()
    while disciplina != "FUTBOL" and disciplina != "BASQUET" and disciplina != "VOLEY":
        print("Dato incorrecto, vuelva a ingresar la disciplina (FUTBOL/BASQUET/VOLEY)")
        disciplina = input(
            "Ingrese la disciplina (FUTBOL/BASQUET/VOLEY): ").upper()
    disciplinas.append(disciplina)
    nivel = input(
        "Ingrese el nivel del equipo (INICIAL/INTERMEDIO/AVANZADO): ").upper()
    while nivel != "INICIAL" and nivel != "INTERMEDIO" and nivel != "AVANZADO":
        print("Dato incorrecto, vuelva a ingresar el nivel (INICIAL/INTERMEDIO/AVANZADO)")
        nivel = input(
            "Ingrese el nivel del equipo (INICIAL/INTERMEDIO/AVANZADO): ").upper()
    niveles.append(nivel)
    puntos_equipo = []
    sanciones_equipo = []
    for j in range(3):
        punto = input(
            f"Ingrese los puntos obtenidos en el partido {j+1} (0-100): ")
        while not punto.isdigit() or not (0 <= int(punto) <= 100):
            print("Debe ingresar un número entre 0 y 100.")
            punto = input(
                f"Ingrese los puntos obtenidos en el partido {j+1} (0-100): ")
        puntos_equipo.append(int(punto))

        sancion = input(
            f"Ingrese las sanciones recibidas en el partido {j+1} (>=0): ")
        while not sancion.isdigit() or int(sancion) < 0:
            print("Debe ingresar un número entero mayor o igual a 0.")
            sancion = input(
                f"Ingrese las sanciones recibidas en el partido {j+1} (>=0): ")
        sanciones_equipo.append(int(sancion))

    puntos.append(puntos_equipo)
    sanciones.append(sanciones_equipo)
    promedio = promedio_puntos(puntos_equipo)
    promedios.append(promedio)

    promedio_sancion = promedio_sanciones(sanciones_equipo)
    promedios_sanciones.append(promedio_sancion)

for i in range(cantidad):
    nivel = niveles[i]
    promedio = promedios[i]
    sancion_promedio = promedios_sanciones[i]

    if nivel == "INICIAL":
        if promedio <= 50 and sancion_promedio <= 6:
            desempeno = "BAJO"
        else:
            desempeno = "MEDIO"
    elif nivel == "INTERMEDIO":
        if promedio > 80 and sancion_promedio < 4:
            desempeno = "MUY BUENO"
        else:
            desempeno = "BUENO"
    elif nivel == "AVANZADO":
        if promedio > 90 and sancion_promedio == 0:
            desempeno = "EXCELENTE"
        else:
            desempeno = "DESTACADO"

    desempenos.append(desempeno)

# CONTADOR DE DEPORTE
futbol = disciplinas.count("FUTBOL")
basquet = disciplinas.count("BASQUET")
voley = disciplinas.count("VOLEY")


partidos_inicial = niveles.count("INICIAL") * 3
partidos_intermedio = niveles.count("INTERMEDIO") * 3
partidos_avanzado = niveles.count("AVANZADO") * 3

bajo = desempenos.count("BAJO")
medio = desempenos.count("MEDIO")
bueno = desempenos.count("BUENO")
muy_bueno = desempenos.count("MUY BUENO")
destacado = desempenos.count("DESTACADO")
excelente = desempenos.count("EXCELENTE")


# Promedios por disciplina
total_futbol = total_basquet = total_voley = 0
cont_futbol = cont_basquet = cont_voley = 0
total_sanc_futbol = total_sanc_basquet = total_sanc_voley = 0


for i in range(cantidad):
    if disciplinas[i] == "FUTBOL":
        total_futbol += promedios[i]
        cont_futbol += 1
        total_sanc_futbol += promedios_sanciones[i]
    elif disciplinas[i] == "BASQUET":
        total_basquet += promedios[i]
        cont_basquet += 1
        total_sanc_basquet += promedios_sanciones[i]
    elif disciplinas[i] == "VOLEY":
        total_voley += promedios[i]
        cont_voley += 1
        total_sanc_voley += promedios_sanciones[i]


if cont_futbol > 0:
    prom_futbol = total_futbol / cont_futbol
else:
    prom_futbol = 0

if cont_basquet > 0:
    prom_basquet = total_basquet / cont_basquet
else:
    prom_basquet = 0

if cont_voley > 0:
    prom_voley = total_voley / cont_voley
else:
    prom_voley = 0


if cont_futbol > 0:
    prom_sanc_futbol = total_sanc_futbol / cont_futbol
else:
    prom_sanc_futbol = 0

if cont_basquet > 0:
    prom_sanc_basquet = total_sanc_basquet / cont_basquet
else:
    prom_sanc_basquet = 0

if cont_voley > 0:
    prom_sanc_voley = total_sanc_voley / cont_voley
else:
    prom_sanc_voley = 0


# Equipo con menor promedio
min_prom = min(promedios)
indice_min = promedios.index(min_prom)
equipo_min = names[indice_min]

# Más de 80 y menos de 50
mas_80 = sum(1 for p in promedios if p > 80)
menos_50 = sum(1 for p in promedios if p < 50)

# Muestreo de resultados
print("\n--- Estadísticas generales ---")
print(
    f"Equipos por deporte: FUTBOL={futbol}, BASQUET={basquet}, VOLEY={voley}")
print(
    f"Partidos por nivel: INICIAL={partidos_inicial}, INTERMEDIO={partidos_intermedio}, AVANZADO={partidos_avanzado}")
print(
    f"Equipos por desempeño: BAJO={bajo}, MEDIO={medio}, BUENO={bueno}, MUY BUENO={muy_bueno}, DESTACADO={destacado}, EXCELENTE={excelente}")
print(
    f"Promedios de puntos por deporte: FUTBOL={prom_futbol}, BASQUET={prom_basquet}, VOLEY={prom_voley}")
print(
    f"Promedios de sanciones por deporte: FUTBOL={prom_sanc_futbol}, BASQUET={prom_sanc_basquet}, VOLEY={prom_sanc_voley}")
print(f"Equipos con más de 80 puntos: {mas_80}")
print(f"Equipos con menos de 50 puntos: {menos_50}")
print(f"Equipo con menor promedio de puntos: {equipo_min} ({min_prom})")
