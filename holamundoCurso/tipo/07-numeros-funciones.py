import math

# Redondea el número al entero más cercano
print(round(1.7))  # Resultado: 2

# Devuelve el valor absoluto (sin signo) de un número
print(abs(-10))    # Resultado: 10
print(abs(55))     # Resultado: 55

# Redondea hacia arriba al entero más cercano
print(math.ceil(1.1))  # Resultado: 2

# Redondea hacia abajo al entero más cercano
print(math.floor(1.199999))  # Resultado: 1

# Verifica si el valor es NaN (Not a Number). Devuelve True si es NaN, False si es un número válido
print(math.isnan(23))  # Resultado: False
# print(math.isnan("23"))  # Esto daría error porque '23' es un string, no un número

# Eleva el primer número a la potencia del segundo (10^3)
print(math.pow(10, 3))  # Resultado: 1000.0

# Calcula la raíz cuadrada del número
print(math.sqrt(9))     # Resultado: 3.0
