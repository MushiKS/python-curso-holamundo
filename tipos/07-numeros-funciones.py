import math # Importa el módulo 'math' para usar funciones matemáticas avanzadas

print(round(1.3))  # Redondea 1.3 al entero más cercano (resultado: 1)
print(round(1.7))  # Redondea 1.7 al entero más cercano (resultado: 2)
print(round(1.5))  # Redondea 1.5 al entero más cercano (resultado: 2, porque Python redondea hacia el par más cercano)
print(abs(-77))    # Devuelve el valor absoluto de -77 (resultado: 77)
print(abs(55))     # Devuelve el valor absoluto de 55 (resultado: 55)

print(math.ceil(1.1))      # Redondea 1.1 hacia arriba al entero más cercano (resultado: 2)
print(math.floor(1.99999)) # Redondea 1.99999 hacia abajo al entero más cercano (resultado: 1)
print(math.isnan(23))      # Verifica si 23 es "NaN" (Not a Number), resultado: False
print(math.isnan("23"))  # Esto daría error porque "23" es un string, no un número
print(math.pow(10, 3))     # Eleva 10 a la potencia 3 (resultado: 1000.0)
print(math.sqrt(9))        # Calcula la raíz cuadrada de 9 (resultado: 3.0)