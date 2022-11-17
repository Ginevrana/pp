## Archivos de datos
## Vamos a generar un archivo de personas. En una primera instancia en forma de lista guardaremos un conjunto de personas y las recuperamos para mostrarlas:

## Importar biblioteca pickle
import pickle

class Persona:
## Definimos una clase persona, que va a tener un constructor init, recibirá 6 parámetros, que se los va a asignar a una serie de campos del constructor.
    def __init__(self, apellido, nombre, tipo_doc, nro_doc, genero, edad):
        self.apellido=apellido
        self.nombre=nombre
        self.tipo_doc=tipo_doc
        self.nro_doc=nro_doc
        self.genero=genero
        self.edad=edad
        print("Se ha ingresado una persona nueva con el nombre de: ", self.apellido, ",", self.nombre)

## Usaremos el método str de python, que convierte en cadena de texto la información de un objeto, nos lo informará en el return aplicándole un formato a la información ingresada
    def __str__(self):
        return "{}{}{}{}{}{}".format(self.apellido, self.nombre, self.tipo_doc, self.nro_doc, self.genero, self.edad)

## Creamos otra clase ListaPersonas que nos servirá para guardarlas y leerlas, con la lista.
# class ListaPersonas: 
#     personas=[]

## El método agregar personas va a permitir agregar al final de la lista cada nuevo integrante que incorporemos a la lista contenida en el parámetro p
    # def agregarPersonas(self,p):
    #     self.personas.append(p)

## Otro que me muestre toda la información guardada en esa lista, con un bucle for apra recorrerla y mostrar el contenido.
#     def mostrarPersonas(self):
#         for p in self.personas:
#             print(p)

# ## Al final nos informará con un print cada vez que haya ingresado una persona a la lista.
# miLista=ListaPersonas()

# ## Ahora debemos guardar la lista en un archivo en el disco. 
# ## Agregamos personas a la lista asignando a cada registro a la variable p y usando el método agregarPersonas los incorporamos a la lista.
# p=Persona("Perez", "Sergio", "DNI", 42325874, "Masculino", 25)
# miLista.agregarPersonas(p)
# p=Persona("Gomez", "Alejandro", "DNI", 20124823, "Masculino", 50)
# miLista.agregarPersonas(p)
# p=Persona("Martinez", "María", "DNI", 18245725, "Femenino", 58)
# miLista.agregarPersonas(p)
# p=Persona("Gonzalez", "Claudia", "DNI", 28487258, "Femenino", 49)
# miLista.agregarPersonas(p)

# ## También llamamos al método mostrar personas para visualizar que estamos haciendo bien el trabajo y lo ejecutamos para probarlo:
# miLista.mostrarPersonas()

'''
RESPUESTA EN TERMINAL: 

Se ha ingresado una persona nueva con el nombre de:  Perez , Sergio
Se ha ingresado una persona nueva con el nombre de:  Gomez , Alejandro 
Se ha ingresado una persona nueva con el nombre de:  Martinez , María  
Se ha ingresado una persona nueva con el nombre de:  Gonzalez , Claudia
PerezSergioDNI42325874Masculino25
GomezAlejandroDNI20124823Masculino50
MartinezMaríaDNI18245725Femenino58
GonzalezClaudiaDNI28487258Femenino49
'''

class ListaPersonas: 
    personas=[]

## A continuación las modificaciones para lograr nuestro archivo externo. 
## Primero creo un constructor en listaPersonas que recibe el parámetro implícito self. Creamos una variable a la cual llamo lista de personas que se va a encargar de crear el archivo externo que lo llamaremos personas_ext que lo abrimos para agregar información binaria con "ab+"

    def __init__(self):
        listaDePersonas=open("Personas_ext","ab+")
## Debemos posicionar el cursos al principio del archivo porqe si tiene información cargada no nos la va a mostrar y para ello usaremos la función seek(0)
        listaDePersonas.seek(0)
        try:
## Para visualizar la información almacenada usamos la lista de personas con la librería pickle con el método load y que nos cargue listaDePersonas, después de un print para que el usuario pueda leerlo, si se ha cargado algo o no, con el mensaje ponemos que se cargaron x cantidad de personas con el formato correspondiente usando el método len para ver cuántas personas tengo cargadas.
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del archivo externo".format(len(self.personas)))
## Debemos poder ver las personas cargadas dentro de la lista de personas, pero si el archivo se encuentra vacío nos daría un error y para salvar esa instancia debemos meterlo dentro de un try, que intente realizar esa instrucción.
        except:
            print("El archivo está vacío")
## Por último cierro listaDePersonas y lo borro de la memoria.
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,p):
        self.personas.append(p)
## Nos queda llamar al método y lo hacemos desde la función agregarPersonas
        self.guardarPersonasEnArchivoExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

## Tenemos que agregar otro método que nos guarde la información en el archivo externo. Lo llamo guardarPersonasEnArchivoExterno, si bien el nombre es claro deja en claro qué hace este método.
    def guardarPersonasEnArchivoExterno(self):
## Usamos la listaDePersonas creada para hacer una escritura de información en el archivo. Abrimos el archivo creado que se llama Personas_ext y en modo de wb "escritura binaria"
        listaDePersonas=open("Personas_ext","wb")
## La librería pickle con el método dump realiza la grabación de nuestra lista de personas de lo que tenemos almacenado en listaDePersonas
        pickle.dump(self.personas,listaDePersonas)
## Una vez hecha la acción la cerramos y borramos de la memoria.        
        listaDePersonas.close()
        del(listaDePersonas)

## Creo una variable la que llamo persona y le damos los parámetros de esa clase persona. Lo corremos y nos muestra que el archivo esta vacío quiere decir que ejecuté el except del try, que agrego a Perez y nos muestra la información completa que tiene el archivo por el método mostrarInfoArchivoExterno que agregamos
    def mostrarInfoArchivoExterno(self):
        print("La información del archivo de personas exernos es la siguiente: ")
        for p in self.personas:
            print(p)

## Instanciamos con la clase listaPersonas
miLista=ListaPersonas()

p=Persona("Perez", "Sergio", "DNI", 42325874, "Masculino", 25)
miLista.agregarPersonas(p)
miLista.mostrarInfoArchivoExterno()

'''
RESPUESTA EN CONSOLA:
El archivo está vacío
Se ha ingresado una persona nueva con el nombre de:  Perez , Sergio
La información del archivo de personas exernos es la siguiente:    
PerezSergioDNI42325874Masculino25
'''
## Nos crea el archivo Personas_ext. Si quiero agregar otra persona instanciará la otra porción de código del try:

persona=Persona("Martinez","Maria", "DNI", 18245725, "Femenino", 58)
miLista.agregarPersonas(persona)
miLista.mostrarInfoArchivoExterno()

'''
RESPUESTA POR CONSOLA:
Se cargaron 2 personas del archivo externo
Se ha ingresado una persona nueva con el nombre de:  Perez , Sergio
La información del archivo de personas exernos es la siguiente:
PerezSergioDNI42325874Masculino25
MartinezMariaDNI18245725Femenino58
Se ha ingresado una persona nueva con el nombre de:  Martinez , Maria
La información del archivo de personas exernos es la siguiente:
PerezSergioDNI42325874Masculino25
MartinezMariaDNI18245725Femenino58
'''