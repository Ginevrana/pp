# Imagina que acabas de abrir una nueva cuenta de caja de ahorros que te ofrece el 6% de interés al anual. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu caja de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la caja de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer año. Redondear cada cantidad a dos decimales.

ahorro = float(input("Cantidad de dinero depositado en caja de ahorro: "))
interes = 0.06

año1= round(ahorro*(interes+1),2)
año2= round(año1*(interes+1),2)
año3= round(año2*(interes+1),2)

print(f"El monto ganado el primer año serán: ${año1}. El segundo año será: ${año2}. Y el tercer año tendrá: ${año3}")