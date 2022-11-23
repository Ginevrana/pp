# Escribir un programa que pregunte al usuario una cantidad de dinero a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Cantidad a invertir: "))
interes = float(input("Porcentaje anual del interés: "))
tiempo = float(input("Cantidad de años de inversión: "))

operacion = inversion*(1+interes/100)**tiempo

print(f"El capital total obtenido es de {operacion}")