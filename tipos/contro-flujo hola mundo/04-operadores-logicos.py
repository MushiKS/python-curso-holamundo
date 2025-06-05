# Operadores lógicos: and, or, not

gas = False
encendido = True
edad = 18

# Esta condición se cumple solo si:
# - no hay gas (not gas → True, porque gas es False)
# - el auto está encendido (True)
# - la persona tiene más de 17 años

if not gas and encendido and edad > 17:
    print("Puedes avanzar")  # Se ejecuta porque todas las condiciones son verdaderas
