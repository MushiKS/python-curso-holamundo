import os
os.system("cls")

lista = ["Araceli","Laura","Juan","Irene","Samuel","Jose","Laura"]

# Recorrer la lista mostrando cada elemento (for-each)
print("Recorrer lista")
for lis in lista:
    print(lis)

# Recorrer la lista usando índices (for con range)
# range(0, 7) genera los números del 0 al 6 (7 elementos)
print("recorrer la lista otra vez")
for i in range(0,7):
    print(lista[i])