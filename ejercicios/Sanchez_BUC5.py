# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inv = int(input("Cantidad $$ a invertir: "))
interes = int(input("Interés anual: "))
tiempo = int(input("Años de inversión: "))

for i in range(tiempo):
    inv*=1+interes/100
    print(f"Año {i+1}, Total obtenido {round(inv,2)}")