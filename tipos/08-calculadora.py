n1 = input("Ingresa primer número")
n2 = input("Ingresa segundo número")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los resultados de {n1} y {n2},
el resultado de la suma es {suma}.
el resultado de la suma es {resta}.
el resultado de la suma es {multi}.
el resultado de la suma es {div}.
"""

print(mensaje)