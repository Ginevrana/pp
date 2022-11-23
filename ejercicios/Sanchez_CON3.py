# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

n1= int(input("Ingrese numero: "))
n2=int(input("Ingrese divisor: "))

if n2 == 0:
    print("No se puede dividir por 0")
else:
    print(n1/n2)