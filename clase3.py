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