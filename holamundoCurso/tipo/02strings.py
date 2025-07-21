# Definición de una variable tipo string
nombre_curso = "Ultimate Python"
# Definición de una variable string multilínea (triple comillas)
descripcion_curso = """
Ultimate python
este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador
"""
# Imprime el nombre del curso y la descripción
print(nombre_curso, descripcion_curso)
# Muestra la cantidad de caracteres de la variable nombre_curso
print(len(nombre_curso))
# Muestra el carácter en la posición 2 (tercer carácter, ya que se empieza desde 0)
print(nombre_curso[2])
# Muestra los caracteres desde la posición 0 hasta la 7 (no incluye la 8)
print(nombre_curso[0:8])
# Muestra los caracteres desde la posición 9 hasta el final
print(nombre_curso[9:])
# Muestra los primeros 8 caracteres
print(nombre_curso[:8])
# Muestra una cadena vacía, ya que el rango es desde 0 hasta 0
print(nombre_curso[0:0])
