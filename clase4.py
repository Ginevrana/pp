# PROGRAMACIÓN ORIENTADA A OBJETOS

# Dentro del paradigma de programación encontramos dos grandes grupos:

# Programación orientada a procedimientos: Son antiguos, surgieron en los 60. Los lenguajes de este grupo son Fortran, Cobol, Baseic, entre otros.
# - Tiene unidades de código muy extensas en aplicaciones complejas, resulta difícil descifrar para otros programadores en caso de actualización o corrección.
# - Poco reutilizable.
# - Ante una falla en una línea de código el programa se detiene.

# Programación orientada a objetos: Son modernos. Los lenguajes de este grupo son Java, C++, Visual.net, python, entre otros. Consiste en trasladar la naturaleza de los objetos de la vida real al código de la programación. 
# Los objetos tienen:
# - Un estado
# - Un comportamiento
# - Unas propiedades
# Estos lenguajes permiten:
# - Modularizar (trozos, partes, módulos, clases)
# - Son reutilizables (herencia)
# - Tratamiento de excepciones (si existe alguna falla en el código, el programa continuará en su ejecución)
# - Encapsulamiento (cada componente no tiene nada que ver con el resto y su funcionamiento interno es autónomo, está "protegido" del resto para que nadie pueda acceder ni manipularlo)

# Vocabulario:
# -> Clase: Modelo donde se redactan las características comunes de un grupo de objetos
# -> Objeto: para acceder a sus propiedades y comportamiento usaremos la nomenclatura del punto: "nombreDelObjeto.propiedad/comportamiento=valor"
# -> Ejemplar de clase -> Instancia de clase -> Ejemplarizar una clase -> Instanciar una clase (Sería un objeto o ejemplar perteneciente a una clase. Instancia = Ejemplar)
# -> Modularización: cuando realizamos una aplicación compleja es normal que esté compuesta por varias clases, donde si uno de estos componentes deja de funcionar no implica que el programa deje de funcionar ya que el resto de los componentes seguiría funcionando.
# -> Herencia

# class Coche():
#     # Propiedades
#     largoChasis=250
#     anchoChasis=120
#     ruedas=4
#     enmarcha=False

#     # Comportamiento
#     # Creamos un método mediante la palabra reservada def, el editor mostrará las dos cosas que podemos hacer: una función o un método agregándole una s
#     # La diferencia entre uno y otro es que el método es una función especial que pertenece a la clase donde está anidada, mientras que la función no pertenece a ninguna clase.
#     def arrancar(self,arrancamos):
#         self.enmarcha=arrancamos

#         if(self.enmarcha):
#             return "El coche está en marcha"
#         else:
#             return "El coche está parado"
        

#     def estado(self):
#         print("El coche tiene", self.ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de", self.largoChasis)
# ¿Cómo podemos establecer o cambiar el comportamiento que tiene este objeto?
# miCoche=Coche()

# print("El largo del coche es:", miCoche.largoChasis)
# print("El auto tiene", miCoche.ruedas, "ruedas")
# print(miCoche.arrancar(True))
# miCoche.estado()
# # Respuesta por consola:
# # 250
# # El auto tiene  4 ruedas

# #-------------------------------------------------
# # miCoche.arrancar()
# # print(miCoche.estado())

# # Respuesta por consola:
# # 250
# # El auto tiene 4 ruedas
# # El coche está en marcha

# #-------------------------------------------------
# # Si comentamos el comportamiento arrancar saldrá el siguiente resultado en consola
# # 250
# # El auto tiene 4 ruedas
# # El coche está parado

# #-------------------------------------------------
# print("********* A partir de acá creamos un segundo objeto *********")

# otroCoche = Coche()

# print("El largo del coche es:", otroCoche.largoChasis)
# print("El coche tiene", otroCoche.ruedas, "ruedas")
# print(otroCoche.arrancar(False))
# otroCoche.estado()
# Resultado por consola:
# 250
# El auto tiene 4 ruedas
# El coche está en marcha
# ********* A partir de acá creamos un segundo objeto *********
# El largo del coche es: 250
# El coche tiene 4 ruedas
# El coche está parado

# Modificamos el método original:
#     def arrancar(self):
#         self.enmarcha=True
# Para que no solo arranque sino para que informe cuál es su estado.

# Resultado por consola con las modificaciones:
# El largo del coche es: 250
# El auto tiene 4 ruedas
# El coche está en marcha
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250   
# ********* A partir de acá creamos un segundo objeto *********
# El largo del coche es: 250
# El coche tiene 4 ruedas
# El coche está parado
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250  

#-------------------------------------------------

# Al usar POO las características comunes de los objetos forman parte de lo que se llama un estado inicial o por defecto.

# ¿Cómo especificamos cuál es el estado inicial que tendrán los objetos pertenecientes a una clase? Con lo que se denomina un CONTRUCTOR. 
# Este es un método especial que le brinda el estado inicial a los objetos y cual será ese estado de los que pertenezcan a una clase.

from msilib import change_sequence


class Coche():

    # Constructor:
    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        # Encapsulamiento de propiedad
        self.__ruedas=4
        self.enmarcha=False

    # Método 1:
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        # Condiciona arranque si no pasa el chequeo inicial
        if(self.enmarcha):
            chequeo=self.chequeo_interno(

            )
        if(self.enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.enmarcha and chequeo==False):
            return "Algo salió mal en el chequeo, no se puede encender el coche."
        else:
            return "El coche está parado"

    # Método 2:
    def estado(self):
        # Encapsulamiento de propiedad ruedas
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de", self.largoChasis)

    # Se agrega Método 3 que condiciona arranque si no pasa el chequeo inicial:
    def chequeo_interno(self):
        print("Realizando chequeo interno")
        self.nafta="Ok"
        self.lubricante="Ok"
        self.puertas="Abiertas"

        if(self.nafta=="Ok" and self.lubricante=="Ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False

# Instancia 1
miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("********* A partir de acá creamos un segundo objeto *********")

# Instancia 2
otroCoche = Coche()
# Acá estamos cambiando una de las propiedades de la clase inicial, lo cual no nos tendría que permitir pero veremos en consola que sale
otroCoche.ruedas=2

print(otroCoche.arrancar(False))
otroCoche.estado()

# Resultado en consola:
# El largo del coche es: 250
# El auto tiene 4 ruedas
# El coche está en marcha
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250   
# ********* A partir de acá creamos un segundo objeto *********
# El largo del coche es: 250
# El coche tiene 2 ruedas
# El coche está parado
# El coche tiene 2 ruedas. Un ancho de 120 y un largo de 250 


# Para proteger la clase inicial hay qeu encapsular o proteger la propiedad para que no se pueda modificar desde fuera de la clase agregando dos guiones bajos la descripción del estado, asi: self.__propiedad. Veamos que sale ahora por consola:
# El coche está en marcha
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250   
# ********* A partir de acá creamos un segundo objeto *********
# El coche está parado
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250  

#-------------------------------------------------
# Se agrega un método de chequeo interno condicionando el arranque y nos da esto por consola:
# Realizando chequeo interno
# El coche está en marcha
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250   
# ********* A partir de acá creamos un segundo objeto *********
# El coche está parado
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250 

# Cambiamos el estado de las puertas de Cerradas a Abiertas a ver que respuesta nos trae por consola:
# Realizando chequeo interno
# Algo salió mal en el chequeo, no se puede encender el coche. 
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250   
# ********* A partir de acá creamos un segundo objeto *********
# El coche está parado
# El coche tiene 4 ruedas. Un ancho de 120 y un largo de 250 