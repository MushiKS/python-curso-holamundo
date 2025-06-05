buscar = 10
# Recorremos los números del 0 al 4 (range(5) genera [0, 1, 2, 3, 4])

for numero in range(5):
    print(numero) # Imprime cada número del 0 al 4

# Si encontramos el número que estamos buscando, se muestra y salimos del bucle

    if numero == buscar:
        print("Encontrado", buscar)
        break 
else:
    # Este bloque solo se ejecuta si el for termina SIN hacer 'break'
    # Como nunca se encuentra el número 10 en range(5), se ejecuta el else
    print("No encontre el número buscado :(")

# Este bucle imprime cada letra de la cadena "ultimate python"
for char in "ultimate python":
    print(char)  # Se imprime una letra por línea