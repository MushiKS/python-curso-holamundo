buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break 
else:
    print("No encontre el número buscado :(")


for char in "ultimate python":
    print(char)