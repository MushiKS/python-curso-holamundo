# Este programa convierte una temperatura dada engrados
# Celsius a dos escalas diferentes:Fahrenheit y Kelvin.


# PIDE EL USUARIO QUE INGRESE UNA TEMPERATURA EN GRADOS CELSIUS

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))


# REALIZA LAS SIGUIENTES CONVERSIONES:

# CELSIUS A FAHRENEIT (GRADOS CELSIUS * 9/5) + 32
fahrenheit = temperatura * 9/5 + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}")


# CELSIUS A KELVIN: GRADOS CELSIUS +273.15
# MUESTRA LAS TEMPERATURAS CONVERTIDAS EN AMBAS ESCALAS
