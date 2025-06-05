# Bucle anidado: dos 'for' uno dentro del otro
# El externo recorre j = 0, 1, 2
# El interno recorre k = 0, 1 para cada valor de j

for j in range(3):
    for k in range(2):
        print(f"{j}, {k}") # Se imprime la combinación de j y k
        