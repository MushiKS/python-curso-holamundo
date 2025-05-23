nombre_curso = "Ultimate Python"
descripcion_curso = """
ultimate python
este curso contempla todos los detalles 
que necesitas aprender para encontrar
un trabajo como programador
"""

print(len(nombre_curso)) # Muestra cuántos caracteres tiene la cadena 'nombre_curso'
print(nombre_curso[0])   # Muestra el primer carácter (posición 0) de la cadena
print(nombre_curso[0:8])  # Muestra los caracteres desde la posición 0 hasta la 7 (no incluye el 8)
print(nombre_curso[9:])   # Muestra los caracteres desde la posición 9 hasta el final
print(nombre_curso[:8])   # Muestra los primeros 8 caracteres (desde el inicio hasta la posición 7)
print(nombre_curso[:])    # Muestra toda la cadena completa (desde el inicio hasta el final)

nombre = "Mati"
apellido = "Mushi"
nombre_completo = nombre + " " + apellido
print(nombre_completo)