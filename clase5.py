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


# # La clase vehículos la damos por terminada y ya estamos en condiciones de crear un objeto que herede la clase vehículos, todas sus propiedades y métodos.

# # class Moto(Vehiculos):
# #     pass

# # miMoto=Moto("Honda","CBR")
# # miMoto.estado()

# # Resultado por consola:
# # Marca:  Honda 
# # Modelo:  CBR       
# # En Marcha:  False  
# # Acelerando:  False 
# # Frenado:  False    

# #---------------------------------
# # Agregamos un comportamiento que no podemos hacer con otro vehículo
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

# # Resultado por consola:
# # Marca:  Honda 
# # Modelo:  CBR
# # En Marcha:  False
# # Acelerando:  False        
# # Frenado:  False
# # Willy:  Voy haciendo Willy


# #-------------------------------------------------------------------
# # Creamos otra clase con otro método interno
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

# #--------------------------------------------
# # Creamos otra clase de vehículos electricos
# class vElectricos():
#     def __init__(self):
#         self.autonomia=100
#     def cargandoEnergia(self):
#         self.cargando=True

# class BicicletaElectrica(vElectricos,Vehiculos):
#     pass

# miBici=BicicletaElectrica()

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