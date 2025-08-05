n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

# Convertimos los valores ingresados a float para permitir decimales
a = float(n1)
b = float(n2)

# Suma
e = a + b
print("Suma:", e)

# Resta
print("Resta:", a - b)

# Multiplicación
print("Multiplicación:", a * b)

# División
if b != 0:
    print("División:", a / b)
else:
    print("No se puede dividir por cero.")
