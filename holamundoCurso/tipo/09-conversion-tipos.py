x = input("")
# int()
# str()
# float()
# bool()

# Ejemplos de conversión a booleano, cada uno en una línea
print("bool(0) =", bool(0))           # False
print("bool(1) =", bool(1))           # True
print("bool(-1) =", bool(-1))         # True
print('bool("") =', bool(""))         # False
print("bool('texto') =", bool("texto")) # True
print("bool(None) =", bool(None))     # False
print("bool([]) =", bool([]))         # False
print("bool([1]) =", bool([1]))       # True
print("bool({}) =", bool({}))         # False
print("bool({'a':1}) =", bool({"a":1})) # True

# Explicación:
# 0, "", None, [], {} son considerados False
# Cualquier otro valor (números distintos de cero, cadenas no vacías, listas o diccionarios con elementos) es True
