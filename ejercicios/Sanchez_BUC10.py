# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num = int(input("Ingrese un N° entero: "))
div = 2

while num % div !=0:
    div += 1

if div == num:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")