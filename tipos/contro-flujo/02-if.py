edad = 70  # Declaramos una variable 'edad' con un valor de 70

# Estructura condicional para evaluar la edad
if edad > 65:  
    # Si la edad es mayor a 65, se ejecuta este bloque
    print("Puede ver la pelicula con super descuento")
elif edad > 54:  
    # Si la edad no es mayor a 65 pero es mayor a 54, se ejecuta este bloque
    print("puedes ver la pelicula con descuento")
elif edad > 17:  
    # Si la edad no es mayor a 54 pero es mayor a 17, se ejecuta este bloque
    print("puedes ver la pelicula")
else:  
    # Si ninguna de las condiciones anteriores se cumple, se ejecuta este bloque
    print("No puedes entrar")

print("Listo")  # Este mensaje se imprime siempre, independientemente de las condiciones