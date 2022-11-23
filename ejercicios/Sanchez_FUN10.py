# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

n = input("Ingrese un numero binario: ")
def adecimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    print (decimal)

adecimal(n)

b = int(input("Ingrese un numero entero: "))
def abinario(b):
    binario = []
    while b > 0:
        binario.append(str(b % 2))
        b //= 2
    binario.reverse()
    print(''.join(binario))

abinario(b)