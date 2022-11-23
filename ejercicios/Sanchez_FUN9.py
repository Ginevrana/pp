# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo

n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))

def max(n1,n2):
    resto =0
    while(n2>0):
        resto=n2
        n2=n1%n2
        n1=resto
    print(n1)

def min(n1,n2):
    if n1>n2:
        mayor=n1
    else:
        mayor=n2
    while(mayor%n1!=0) or (mayor%n2!=0):
        mayor +=1
    print(mayor)

max(n1,n2)
min(n1,n2)