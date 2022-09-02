# Condicionales: concatenación de operadores lógicos, incluídos "and", "or" e "in"

# Ejemplo 1:

# edad=7

# if 0<edad<100:
#     print("Edad correcta")
# else:
#     print("Edad incorrecta")

#------------------------------------------------------
# Ejemplo 2:

# sueldoGerente=int(input("Ingrese sueldo del gerente: "))
# print("Sueldo Gerente: " + str(sueldoGerente))

# sueldoDirector=int(input("Ingrese sueldo del Director: "))
# print("Sueldo Director: " + str(sueldoDirector))

# sueldoJefe=int(input("Ingrese sueldo del Jefe: "))
# print("Sueldo Jefe: " + str(sueldoJefe))

# sueldoAdmin=int(input("Ingrese sueldo del Administrativo: "))
# print("Sueldo Administrativo: " + str(sueldoAdmin))

# if sueldoAdmin<sueldoJefe<sueldoDirector<sueldoGerente:
#     print("Todo funciona correctamente")
# else:
#     print("Algo está fallando en la empresa")

#------------------------------------------------------
# Ejemplo 3 "AND" Y "OR":

# print("Programa de becas")

# distEscuela=int(input("Ingrese la distancia de su casa a la escuela en kms: "))

# cantHermanos=int(input("Ingrese la cantidad de hermanos que van a la escuela: "))

# salarioFliar=int(input("Ingrese el salario anual bruto que percibe la familia: "))

# Condición estricta: Tienen que ser todas cumplidas para que se de un caso o el otro.
# if distEscuela>40 and cantHermanos>2 and salarioFliar<=480000:
#     print("Tiene derecho a beca")
# else:
#     print("No tiene derecho a beca")


# En este caso flexibilizamos las condiciones indicando que si bien no cumple las primeras dos al tener un ingreso menor puede gozar de la beca
# if distEscuela>40 and cantHermanos>2 or salarioFliar<=480000:
#     print("Tiene derecho a beca")
# else:
#     print("No tiene derecho a beca")

#------------------------------------------------------
# Ejemplo 4 "IN":

# print("Asignaturas optativas")
# print("Opciones: Informática gráfica, Pruebas de Software, Usabilidad y Accesibilidad")

# asignatura=input("Escribe la asignatura elegida: ")

# if asignatura in ("Informática gráfica", "Pruebas de Software", "Usabilidad y accesibilidad"):
#     print("Asignatura elegida "+ asignatura)
# else:
#     print("La asignatura elegida no esta contemplada en las opciones")

#------------------------------------------------------
