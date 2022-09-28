# # Herencia
# # Se trata de trasladar el comportamiento de la herencia entre objetos a código de programación
# # Clase padre (superclase) -> Subclase

# # Reutilización de código en casos de objetos similares: para no tener que crear de cero en cada objeto características y comportamientos que comparten, se toman los parámetros en común y se insertan en una clase que se llamará clase padre o superclase

# class Vehiculos():
#     # Características
#     def __init__(self, marca, modelo):
#         self.marca=marca
#         self.modelo=modelo
#         self.enmarcha=False
#         self.acelera=False
#         self.frena=False

#     # Métodos de comportamientos
#     def arrancar(self):
#         self.enmarcha=True

#     def acelerar(self):
#         self.acelera=True
    
#     def frenar(self):
#         self.frena=True

#     def estado(self):
#         print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)


# La clase vehículos la damos por terminada y ya estamos en condiciones de crear un objeto que herede la clase vehículos, todas sus propiedades y métodos.

# class Moto(Vehiculos):
#     pass

# miMoto=Moto("Honda","CBR")
# miMoto.estado()

# Resultado por consola:
# Marca:  Honda 
# Modelo:  CBR       
# En Marcha:  False  
# Acelerando:  False 
# Frenado:  False    

#---------------------------------
# Agregamos un comportamiento que no podemos hacer con otro vehículo
# class Moto(Vehiculos):
#     willy=""
#     def willy(self):
#         self.willy="Voy haciendo Willy"
        
#         # En este punto no veremos el método propio y tampoco lo puedo agregar en el metodo estado porque está declarado por fuera de la clase vehículos. La forma de visualizarlo es sobre escribiendo el método de estado dentro de la clase moto. Este segundo método invalida el primero y acá agrega el ultimo para visualizarlo

#     def estado(self):
#         print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "\nWilly: ", self.willy)

# miMoto=Moto("Honda","CBR")
# miMoto.willy()
# miMoto.estado()

# Resultado por consola:
# Marca:  Honda 
# Modelo:  CBR
# En Marcha:  False
# Acelerando:  False        
# Frenado:  False
# Willy:  Voy haciendo Willy


#-------------------------------------------------------------------
# Creamos otra clase con otro método interno
# class Utilitario(Vehiculos):
#     def carga(self,cargar):
#         self.cargado=cargar
#         if(self.cargado):
#             return "El utilitario está cargado"
#         else:
#             return "El utilitario está vacío"
        
# miUtilitario=Utilitario("Renault", "Kangoo")
# miUtilitario.arrancar()
# miUtilitario.estado()
# print(miUtilitario.carga(True))

# # Respuesta por consola:
# # Marca:  Honda 
# # Modelo:  CBR
# # En Marcha:  False
# # Acelerando:  False        
# # Frenado:  False
# # Willy:  Voy haciendo Willy
# # Marca:  Renault
# # Modelo:  Kangoo
# # En Marcha:  True
# # Acelerando:  False
# # Frenado:  False
# # El utilitario está cargado

#--------------------------------------------

# Crearemos un programa que tendrá en principio dos clases, una persona y la otra empleados:

# class Persona():
    # def __init__(self,nombre,edad,domicilio):
    #     self.nombre=nombre
    #     self.edad=edad
    #     self.domicilio=domicilio

    # def descripcion(self):
    #     print("Nombre:",self.nombre, "\nEdad:", self.edad,"\nDomicilio:",self.domicilio)

# class Empleado(Persona):
   #  def __init__(self, salario, antiguedad, nombre_empleado,edad_empleado,domicilio_empleado):
        # Esto quiere decir que vamos a llamar al constructor de la clase padre
        # super(). __init__(nombre_empleado,edad_empleado,domicilio_empleado)
        
        # self.salario=salario
        # self.antiguedad=antiguedad

    # def descripcion(self):
    #     # Tenemos que agregar un método descripción en la clase empleados involucrando la clase padre
    #     super().descripcion()
    #     print("Salario:",self.salario,"\nAntiguedad:",self.antiguedad)


# pedro=Persona("Pedro", 45, "Paraguay 2122")
# pedro.descripcion()

# Respuesta por consola:
# Nombre: Pedro 
# Edad: 45
# Domicilio: Paraguay 2122

# juan=Empleado(150000,20,"Juan",25,"Santa Fé 4581")
# juan.descripcion()

# Respuesta por consola:
# Nombre: Juan
# Edad: 25
# Domicilio: Santa Fé 4581
# Salario: 150000
# Antiguedad: 20

#--------------------------------------------

# Principio de sustitución: Cuando tenemos herencia un objeto de la subclase siempre será un objeto de la superclase (un empleado es una persona)
# Para comprobarlo Python nos ofrece una función para comprobar isinstance() que nos informa si un objeto es instancia de una clase determinada, muy útil cuando trabajemos con programas más complejos.

# print(isinstance(juan,Empleado)) # Nos devuelve la siguiente respuesta:
# Nombre: Juan
# Edad: 25
# Domicilio: Santa Fé 4581
# Salario: 150000
# Antiguedad: 20
# True


# print(isinstance(juan,Persona)) # También lo haremos con Persona:
# Nombre: Juan
# Edad: 25
# Domicilio: Santa Fé 4581
# Salario: 150000
# Antiguedad: 20
# True
# True

# Si a juan le cambiamos la clase a tipo Persona, en empleado nos daría False pero como persona seguiría dandonos True

#--------------------------------------------
# Volviendo al ejemplo del programa anterior de vehiculos
# class vElectricos(Vehiculos):
#     def __init__(self, marca, modelo):
#         super(). __init__(marca,modelo)
#         self.autonomia=100
#     def cargandoEnergia(self):
#         self.cargando=True

# class BicicletaElectrica(vElectricos,Vehiculos):
#     pass

# miBici=BicicletaElectrica("Aurora","J0007")
# miBici.estado()

# Respuesta por consola:
# Marca:  Aurora
# Modelo:  J0007
# En Marcha:  False
# Acelerando:  False
# Frenado:  False

# -------------------------------------------------------
# Polimorfismo: Puede cambiar de forma dependiendo del contexto que se utilice, así también el comportamiento

# class Coche():
#     def desplazamiento(self):
#         print("Mi desplazamiento es en cuatro ruedas")


# class Moto():
#     def desplazamiento(self):
#         print("Mi desplazamiento es en dos ruedas")


# class Camion():
#     def desplazamiento(self):
#         print("Mi desplazamiento es en ocho ruedas")

# # miVehiculo=Moto()
# # miVehiculo.desplazamiento()

# # miVehiculo2=Coche()
# # miVehiculo2.desplazamiento()

# # Supongamos que necesitamos programar el comportamiento para cientos de vehículos, tendremos que reproducir lo que hemos hecho hasta ahora por la cantidad de vehículos que necesitemos
# # Para esto crearemos un método o función que va a recibir un objeto por parámetro

# def desplazamientoVehiculo(vehiculo): # Polimorfismo
#     vehiculo.desplazamiento()

# miVehiculo=Camion()

# desplazamientoVehiculo(miVehiculo)

#------------------------------------------------------
# MANIPULACIÓN DE CADENAS
# Python es un lenguaje POO y trata a las cadenas de caracteres, palabras, frases, como objetos string y como tales tienen sus propiedades y métodos

# cadena = " soy uNa cadEna de Caracteres"
# print(cadena)

# # Convierte en mayúsculas
# print(cadena.upper())

# # Convierte en minúsculas
# print(cadena.lower())


# # Convierte la primer letra en mayúscula
# print(cadena.capitalize())

# # Cuenta cuantas veces aparece una letra o cadena de caracteres
# print("Cantidad de veces que aparece la letra a:", cadena.count("a"))

# # Nos dice cual es la posición de una letra o un grupo de caracteres
# print("Posición de la letra a", cadena.find("a"))

# # Nos devuelve un booleano si el valor es numérico o no
# print("¿Es un valor numérico?", cadena.isdigit())

# # Comprueba si es alfanumérico
# print("¿Es un valor alfanumérico?",cadena.isalpha())

# # Nos devuelve la separación de las palabras usando espacios
# print(cadena.split())

# # Borra los espacios sobrantes al principio y al final de una frase
# print(cadena.strip())

# # Cambia una palabra o letra por otra
# print(cadena.replace("a","e"))

# # Lo mismo que find() pero contando desde atrás
# print(cadena.rfind("e"))

#----------------------------------------------------------------------
# Ejemplo de uso de isdigit()

# edad=input("Ingresa tu edad: ")

# while(edad.isdigit()==False):
#     print("Por favor, ingresa un valor numérico")
#     edad=input("Ingresa tu edad: ")

# if(int(edad)<18):
#     print("No podes pasar")
# else:
#     print("Podes pasar")

# edad=input("Ingresa tu edad: ")
# if(int(edad)<18):
#     print("No podes pasar")
# else:
#     print("Podes pasar")

# Respuesta de consola:
# Por favor, ingresa un valor numérico
# Ingresa tu edad: sdf
# Por favor, ingresa un valor numérico
# Ingresa tu edad: asdf
# Por favor, ingresa un valor numérico
# Ingresa tu edad: 25
# Podes pasar      
# Ingresa tu edad: 23
# Podes pasar


#-------------------------------------------
# Ejercitación: Crear un programa que pida una dirección de email por teclado. El programa debe imprimir en consola si la dirección es correcta o no en función de si tiene el símbolo "@"
# - Si tiene una la dirección es correcta
# - Si tiene más de una la dirección es errónea
# - Si no tiene ninguna la dirección es errónea
# - Si está al comienzo la dirección es errónea
# - Si está al final la dirección es errónea

correo=input("Ingrese su dirección de correo: ")
valido=False

for i in range(len(correo)):
    if correo[i]=="@":
        valido=True
    elif(int(i.count("@"))>1):
        valido=False
        break
    elif(i.find("@")==0):
        valido=False
        break
    elif(i.rfind("@")==int(len(correo))):
        valido=False
        break

if valido:
    print("Email ingresado es correcto")
else:
    print("Email ingresado es incorrecto")

