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
# Bucle FOR: Para repetir una o varias líneas de código. Pueden ser determinados o indeterminados.

# Para que ejecute una acción basada en la cantidad de componentes del array
# for i in [1,2,3]:
#     print("Hola")

# Resultado en consola:
# Hola
# Hola
# Hola


# Para que imprima cada uno de los componentes en consola
# for i in ["Invierno", "Otoño", "Primavera","Verano"]:
#     print(i)

# Resultado en consola:
# Invierno
# Otoño
# Primavera
# Verano


# Para que imprima todos los componentes en una sola línea con end=" "
# for i in ["Invierno", "Otoño", "Primavera","Verano"]:
#     print(i, end=" ")

# Resultado en consola:
# Invierno Otoño Primavera Verano


# Podemos usarlo para validar un dato
# email=False
# miCorreo=input("Ingrese su dirección de correo: ")

# for i in miCorreo:
#     if(i=="@"):
#         email=True
# if email==True:
#     print("El email es correcto")
# else:
#     print("El email no es correcto")


# Blucle con range
# for i in range(5):
#     print(i)

# Resultado en consola:
# 0
# 1
# 2
# 3
# 4


# Bucle concatenando textos con el valor tomado por i
# for i in range(9):
#     print(f"Valor de la variable {i}")

# Resultado en consola:
# Valor de la variable 0
# Valor de la variable 1
# Valor de la variable 2
# Valor de la variable 3
# Valor de la variable 4
# Valor de la variable 5
# Valor de la variable 6
# Valor de la variable 7
# Valor de la variable 8


# Otra manera de usar el range es indicando el número desde el cual comenzar, el número hasta el cual llegar y los saltos de número.
# for i in range(5,60,4):
#     print(f"Valor de la variable {i}")

# Resultado en consola:
# Valor de la variable 5
# Valor de la variable 9
# Valor de la variable 13
# Valor de la variable 17
# Valor de la variable 21
# Valor de la variable 25
# Valor de la variable 29
# Valor de la variable 33
# Valor de la variable 37
# Valor de la variable 41
# Valor de la variable 45
# Valor de la variable 49
# Valor de la variable 53
# Valor de la variable 57


# Range como iterador de string: Va a pedir un mail que ingresaremos incorrectamente, con len(email) devuelve la longitud del string y con el condicional evaluaremos si alguna i equivale a "@".

# valido=False
# email=input("Introduce tu email: ")

# for i in range(len(email)):
#     if email[i]=="@":
#         valido=True
# if valido:
#     print("Email ingresado es correcto")
# else:
#     print("Email ingresado es incorrecto")

# Resultado en consola:
# Introduce tu email: juan.perez
# Email ingresado es incorrecto