# Escribir una función que reciba un número entero positivo y devuelva su factorial.

num = int(input("Ingresar N° positivo: "))

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    print(tmp)

factorial(num)