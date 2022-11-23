# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función

radio = int(input("Ingrese radio del círculo para calcular área: "))
altura = int(input("Ingrese altura para calcular volumen de cilindro basado en el círculo: "))
pi=3.14

def circulo(r):
    print(f"El área del círculo es de {pi*r**2}")

def cilindro(r,h):
    area=(pi*r**2)*h
    print(f"El área del cilindro es de {area}")

circulo(radio)
cilindro(radio,altura)