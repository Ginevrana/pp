# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y

nombre= input("Ingrese su nombre: ").lower()
sexo=input("Ingrese su género (m o f): ").lower()

if sexo == "f" and nombre < "m" or sexo == "m" and nombre > "n":
    print("Grupo A")
else:
    print("Grupo B")