# Importa el módulo os para poder usar funciones del sistema operativo
import os
# Limpia la terminal (en Windows usa 'cls')
os.system("cls")

# Define una variable string con espacios y mayúsculas/minúsculas
animal = "  ChanCHito feliz  "

# Convierte todo el texto a mayúsculas
print(animal.upper())  # Resultado: '  CHANCHITO FELIZ  '

# Convierte todo el texto a minúsculas
print(animal.lower())  # Resultado: '  chanchito feliz  '

# Elimina espacios al inicio y final, y pone la primera letra en mayúscula
print(animal.strip().capitalize())  # Resultado: 'Chanchito feliz'

# Pone en mayúscula la primera letra de cada palabra
print(animal.title())  # Resultado: '  Chanchito Feliz  '

# Elimina los espacios solo del final de la cadena
print(animal.rstrip())  # Resultado: '  ChanCHito feliz'

# Busca la subcadena 'CH' y devuelve la posición donde la encuentra (distingue mayúsculas/minúsculas)
print(animal.find("CH"))  # Resultado: 6 (empieza a contar desde 0)
print(animal.replace("nCH", "j"))
print("nCH" in animal)
print("nCH" not in animal)
