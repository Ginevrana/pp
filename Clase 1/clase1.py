# >>> La línea que aparece demarcada con ese símbolo desde donde está marcado para escribir código se llama PROMPT

# print ("Hola a todos") // Es una INSTRUCCIÓN

# Podemos cargar una variable con un valor y al llamarla aparecerá lo que hayamos cargado dentro al darle enter.

# En el caso de querer dividir el contenido de una variable en dos líneas ponemos una barra invertida y continuamos con la línea de abajo así:
# xvariable = ¡Mi nombre es \
# Enrique!
# El resultado es el mismo que declarandolo todo en una misma línea

# Si creamos una variable mensaje y el contenido le ponemos triple comillas cada vez que haga un salto de línea la instrucción la respetará. Por ejemplo:
# mensaje = """ Esto
# es un mensaje con
# tres saltos de línea """

# Funciones: se componen por una declaración, cuerpo y llamada de la función. Se definen de la siguiente manera:
# def suma(n1,n2):
#   print(n1+n2)

# Condicionales: son flujos de ejecución de un programa y constan de la siguiente sintaxis:
# def evaluacion(xnota):
#   valoracion="aprobado"    
#   if xnota<5:
#       valoracion="reprobado"
#   return valoracion

# print("Programa de evaluación de notas de alumnos")
# nota_alumno=input("Ingrese la nota del alumno a evaluar: ")

# def evaluacion(nota):
#     valoracion="El alumno está aprobado"
#     if nota<5:
#         valoracion="El alumo está reprobado"
#     return valoracion

# print(evaluacion(int(nota_alumno)))

#------------------------------------------------

# print("Verificación de acceso")
# edad_user=int(input("Introduce tu edad por favor: "))

# if edad_user<18:
#     print("No puede pasar")
# elif edad_user>100:
#     print("Edad incorrecta")
# else:
#     print("Puede pasar")

# print("El programa ha terminado")

#------------------------------------------------

# Ejercicio 1: Crea un programa que pida dos números por teclado. El programa tendrá una función llamada "DevuelveMax" encargada de devolver el número más alto de los dos introducidos.

# n1=int(input("Introduce el primer número: "))
# n2=int(input("Introduce el segundo número: "))

# def devuelveMax(n1,n2):
#     if n1<n2:
#         print(n2)
#     elif n1>n2:
#         print(n1)
#     else:
#         print("Son iguales")

# print("El número más alto de los dos ingresados es: ")

# devuelveMax(n1,n2)

#------------------------------------------------

# Ejercicio 2: Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.

n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))
n3=int(input("Introduce el tercer número: "))

media=(n1+n2+n3)/3

print("La media aritmética es: ")
print(media)