animal = "  ChanCHito feliz  "  # Declaramos una variable con una cadena de texto que incluye espacios al inicio y al final

print(animal.upper())  # Convierte todos los caracteres de la cadena a mayúsculas
print(animal.lower())  # Convierte todos los caracteres de la cadena a minúsculas
print(animal.strip().capitalize())  # Elimina los espacios al inicio y al final, y convierte solo la primera letra de la cadena a mayúscula
print(animal.title())  # Convierte la primera letra de cada palabra a mayúscula
print(animal.strip())  # Elimina los espacios al inicio y al final de la cadena
print(animal.lstrip())  # Elimina solo los espacios al inicio de la cadena
print(animal.rstrip())  # Elimina solo los espacios al final de la cadena
print(animal.find("CH"))  # Busca la subcadena "CH" y devuelve el índice de su primera aparición (o -1 si no se encuentra)
print(animal.replace("nCH", "j"))  # Reemplaza todas las apariciones de "nCH" por "j" en la cadena
print("nCH" in animal)  # Devuelve True si "nCH" está presente en la cadena, de lo contrario False
print("nCH" not in animal)  # Devuelve True si "nCH" no está presente en la cadena, de lo contrario False