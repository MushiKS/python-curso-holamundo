print("Bienvenidos a la calculadora ultimate")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div, y resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("Ingrese la operación: ")
    if op.lower() == "salir":
       break