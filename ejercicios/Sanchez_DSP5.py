# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.

horas = int(input("¿Cuántas horas trabajó? "))
costo = int(input("¿Qué costo tiene su hora de trabajo? "))
sueldo = horas * costo

print(f"Según los datos ingresados le corresponde ${sueldo} de sueldo")