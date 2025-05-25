import os
#módulo de funciones limpieza de pantalla
os.system("cls")
print("**BIENVENIDOS A UN NUEVO PROGRAMITA **")
print("** HOY VAMOS A HACER ALGUNOS CALCULOS **")
print("Ingresar dos precios y sumarlos")
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
#calculando la suma de ambos
s=num1+num2
#calcular la resta
r=num1-num2
#calcular la multiplicacion
m=num1*num2
#calcular la división
d=num1/num2
#calcula la potencia
p=num1**num2
#calcular el resto o modulo
re=num1%num2
print("Los numeros ingresados son ",num1,num2)
print("SUMA: ",s," RESTA: ",r," MULTIPLICACION: ",m," DIVISION: ",d)
print("POTENCIA: ",p," RESTO: ",re)
tecla=input("Ingrese una tecla para continuar....")


