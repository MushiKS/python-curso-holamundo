#Ingresar codigo del producto, detalle del producto, precio del producto y cantidad llevada.
#Según la cantidad, determinar el descuento. Calcular el total a pagar. Mostrar datos y resultados.
# <=5 es 5%, <=10 es 10%, <=25 es 25%, <=40 es 35%, >40 es 50%

import os
os.system("cls")

codigo = input("Ingrese el código del producto: ")
detalle = input("Ingrese el detalle del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad llevada: "))

# Determinar el descuento
if cantidad <= 5:
    descuento = 0.05
elif cantidad <= 10:
    descuento = 0.10
elif cantidad <= 25:
    descuento = 0.25
elif cantidad <= 40:
    descuento = 0.35
else:
    descuento = 0.50

subtotal = precio * cantidad
monto_descuento = subtotal * descuento
total = subtotal - monto_descuento

print("\n--- DATOS Y RESULTADOS ---")
print(f"Código: {codigo}")
print(f"Detalle: {detalle}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Descuento aplicado: {descuento*100}%")
print(f"Subtotal: {subtotal}")
print(f"Monto de descuento: {monto_descuento}")
print(f"Total a pagar: {total}")