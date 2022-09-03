# Generadores: son más eficientes que funciones tradicionales ya que no necesitan de una lista cuando necesitamos un valor, se ejecuta hasta hallar el valor buscado, economizando tiempo y espacio de procesamiento.

# Cada vez que un generador almacena un valor permanece en estado pausado o stand by hasta que se solicite el siguiente. Esto es conocido como "Suspensión de estado".


# Función tradicional:

# def generaPares(limite):
#     num=1
#     miLista=[]
#     while num<limite:
#         # .append sirve para agregar al array
#         miLista.append(num*2)
#         num=num+1
#     return miLista

# print(generaPares(10))

# Resultado en consola:
# [2, 4, 6, 8, 10, 12, 14, 16, 18]


# Generador

# def generaPares(limite):
#     num=1
#     while num<limite:
#         yield num*2
#         num=num+1

# devuelvePares=generaPares(10)

# print(next(devuelvePares))
# print("Acá podría ir más código...")

# print(next(devuelvePares))
# print("Acá podría ir más código...")

# print(next(devuelvePares))
# print("Acá podría ir más código...")

# Resultado en consola:
# 2
# Acá podría ir más código...
# 4
# Acá podría ir más código...
# 6
# Acá podría ir más código...


# Instrucción yield from: simplifica el código del generador en el caso de que nos veamos necesitados de usar bucles anidados.

# Ejemplo de yield NO anidado
# def devuelveCiudades(*ciudades):
#     for elemento in ciudades:
#         yield elemento

# ciudadesDevueltas=devuelveCiudades("Miramar", "Mar del Plata", "Necochea", "Pinamar")

# print(next(ciudadesDevueltas))
# print(next(ciudadesDevueltas))

# Resultado en consola:
# Miramar
# Mar del Plata


# Ejemplo de yield anidado
# def devuelveCiudades(*ciudades):
#     for elemento in ciudades:
#         for subElemento in elemento:
#             yield subElemento

# ciudadesDevueltas=devuelveCiudades("Miramar", "Mar del Plata", "Necochea", "Pinamar")

# print(next(ciudadesDevueltas))
# print(next(ciudadesDevueltas))

# Resultado en consola:
# M
# i

#------------------------------------------------------
# Excepciones: Cuando ocurren errores durante la ejecución de una línea del programa sin importancia vital pero necesitamos que el resto del códiga siga ejecutandose hacemos las excepciones a errores que podemos preveer. 

# Para esto usamos la palabra dedicada try y except, de la siguiente manera:

# def suma(n1,n2):
#     return n1+n2

# def resta(n1,n2):
#     return n1-n2

# def multiplica(n1,n2):
#     return n1*n2

# def divide(n1,n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError:
#         print("No se puede dividir por 0")
#         return "Operación errónea"

# while True:
#     try:
#         op1=(int(input("Ingrese un primer número: ")))
#         op2=(int(input("Ingrese un segundo número: ")))
#         break
#     except ValueError:
#         print("El valor ingresado no es un número")

# operacion=input("""Ingrese la operación que desea realizar: 
# suma
# resta
# multiplica
# divide
# Indique opción deseada: """)

# if operacion=="suma":
#     print(suma(op1,op2))
# elif operacion=="resta":
#     print(resta(op1,op2))
# elif operacion=="multiplica":
#     print(multiplica(op1,op2))
# elif operacion=="divide":
#     print(divide(op1,op2))
# else:
#     print("Esa operacion no está contemplada entre las opciones")

# print("Operación ejecutada. Continuación de ejecución de la aplicación.")

# Resultado en consola:
# Ingrese un primer número: a
# El valor ingresado no es un número
# Ingrese un primer número: 3
# Ingrese un segundo número: 0
# Ingrese la operación que desea realizar: 
# suma
# resta
# multiplica
# divide
# Indique opción deseada: divide
# No se puede dividir por 0
# Operación errónea
# Operación ejecutada. Continuación de ejecución de la aplicación.


# finally: cuando necesitamos que el print final se ejecute siempre

# def divide():
#     try:
#         op1=(float(input("Ingrese el primer número: ")))
#         op2=(float(input("Ingrese el segundo número: ")))
#         print("La división es: "+str(op1/op2))
#     except ValueError:
#         print("El valor ingresado no es un número")
#     except ZeroDivisionError:
#         print("No se puede dividir por 0")
#     finally:
#         print("Cálculo finalizado.")


# raise: base para excepciones en POO

# def evaluaEdad(edad):
#     if edad<0:
#         raise TypeError("No se permiten edades negativas")
#     if edad<13:
#         return "Sos un niño"
#     elif edad<20:
#         return "Sos muy joven"
#     elif edad<35:
#         return "Sos joven"
#     elif edad<40:
#         return "Sos maduro"
#     elif edad<80:
#         return "Sos adulto"
#     elif edad<100:
#         return "A cuidarse"

# print(evaluaEdad(-15))

# Resultado en consola:
# Traceback (most recent call last):
#   File "C:\Users\Teresita\Documents\IFTS\1er año\Paradigmas de programación\Clases\clase3.py", line 181, in <module>
#     print(evaluaEdad(-15))
#   File "C:\Users\Teresita\Documents\IFTS\1er año\Paradigmas de programación\Clases\clase3.py", line 167, in evaluaEdad
#     raise TypeError("No se permiten edades negativas")
# TypeError: No se permiten edades negativas


# Para que el error no salga como en el ejemplo anterior se captura la excepción
# import math

# def calculaRaiz(n1):
#     if n1<0:
#         raise ValueError("El número ingresado no puede ser negativo")
#     else:
#         return math.sqrt(n1)

# op1=(int(input("Ingresa un número para el cálculo de la raíz cuadrada: ")))

# try:
#     print(calculaRaiz(op1))
# except ValueError as errorDeNumeroNegativo:
#     print(errorDeNumeroNegativo)

# print("Programa terminado.")

# Resultado en consola:
# Ingresa un número para el cálculo de la raíz cuadrada: -8
# El número ingresado no puede ser negativo
# Programa terminado.