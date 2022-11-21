# ***** INTERFACES GRÁFICAS *****
# ¿Qué son? Ventanas a través de las cuales el usuario interactúa con los programas, funciona como intermediario entre el programa y el usuario. Todas las aplicaciones que usamos tienen una interfaz para su fácil manejo.

# Formado por conjunto de gráficos: Ventanas, Botones, Menúes, Casillas de verificación.

# Librerías para front: Tkinter (viene por default con python), Wxpython, Pyqt y Pygtk.

# Estructura de ventana con Tkinter:
# 1. Ventana
# 2. Organizador o contenedor
# 3. Elementos y widgets

################################################

# Construyendo la raíz

# 1) Se importa la biblioteca tkinter con el * para acceder a todos sus métodos
from tkinter import *

# 2) Crearemos una variable que comúnmente la llamamos por lo que representa la "raiz" de una aplicación llamando a la clase tk
raiz=Tk()

# Le colocamos un titulo 
# raiz.title("Ventana de prueba")

# Podemos cambiarle las dimensiones o fijarla para que nadie la pueda cambiar con el siguiente método.
# raiz.resizable(True,True)

# Le podemos asignar cualquier imagen como ícono pasandola al formato ico y corriendola con el siguiente método. 
# raiz.iconbitmap("delfin.ico")

# Para fijar el tamaño de la ventana.
# raiz.geometry("650x350")

# Podemos cambiar el color de fondo de la ventana con el método config()
# raiz.config(bg="green")

# 3) Usamos el método mainloop() para que la venatna pueda estar en ejecución debe estar en una especie de bucle infinito de continua ejecución.
# raiz.mainloop()

## Cambiando la extensión del archivo en .pyw la convertimos en una aplicación que directamente nos abrira la ventana creada, sin el editor de código.

# Para acceder a la documentación de la librería tkinter: https://docs.python.org/3/library/tkinter.html

###############################################
# Para construir el framework:

# Llamamos al metodo frame, creado así tenemos dos cosas sueltas el raíz y el frame por separado, debemos vincularlos para que esté dentro de la raíz.
# miFrame=Frame()

# Para vincularlo con la raíz recurriremos al método pack() indicando la ubicación derecha y al sur.
# miFrame.pack(side="right", ancho="s")

# Para verlo reflejado debemos anular el geometry (para que el frame no tome el tamaño de la raíz) y darle el tamaño al frame
# miFrame.config(bg="red")
# Llamamos al metodo frame, creado así tenemos dos cosas sueltas el raíz y el frame por separado, debemos vincularlos para que esté dentro de la raíz.

# miFrame.config(width="650", height="350")
# Para cambiar el borde y el ancho
# miFrame.config(bd=35)
# miFrame.config(relief="groove")
# Para cambiar el cursos a una mano
# miFrame.config(cursor="hand2")
# raiz.mainloop()

###############################################

# Dentro del frame agregaremos widgets, empezando por un instrumento para mostrar texto o imágenes

# LABELS: tiene la finalidad de mostrar textos, no se puede interactuar con estos porque son etiquetas. La sintaxis es la siguiente:
#   Variablelabel=Label(contenedor,opciones)
# El contenedor padre especifica donde va a estar ubicado el label que puede ser un frame, una raíz, etc.)
# Las opciones son varias: text, anchor, bg, bitmap, bd, font, fg, width, height, entre otros.

# raiz.title("Foto de perro")
# raiz.geometry("568x516")

# raiz.config(bg="blue")
# miFrame=Frame(raiz, width=500, height=400)
# miFrame.pack()
# miFrame.config(bg="red")
# # miLabel=Label(miFrame, text="Hola alumnos de Sistemas")
# # miLabel.place(x=100, y=200)

# ## Para agregar una imagen:
# imagen=PhotoImage(file="perro.png")
# fondo=Label(miFrame, image=imagen).place(x=100,y=100)


###############################################
# Otro elemento muy usado son los cuadros de texto. Tiene como finalidad el ingreso de textos, se cliquea sobre el y permite escribir.

# Sintaxis: Varablelabel=Entry(contenedor, opciones)
# En cuanto al contenedor es lo mismo que los anteriores, se determina el contenedor padre. Sobre las opciones hay varias para apilcar, tambien disponibles en la documentación web.

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

# Se incorpora cuadro de texto e indicamos coordenadas de ubicación.
# cuadroTexto=Entry(miFrame)
# cuadroTexto.place(x=100,y=100)

# Para combinar la etiqueta "label" con un cuadro de texto y darle formato de formulario, como que el label nos indica qué debemos escribir en el mismo. 
# Para esto debemos hacer coincidir para que uno quede al lado del otro en la misma línea.
# nombreLabel=Label(miFrame, text="Nombre: ")
# nombreLabel.place(x=120, y=100)

# Sin embargo con la ubicación colocada se superpone contra el cuadro de texto, para esto usaremos otro widget: grid(). Este método construye una guilla o tabla con filas y columnas. Lo utilizaremos para dividir nuestra interfase gráfica en casillas y en cada una de ellas ubicaremos elementos a nuestro gusto bien alineados. Este método lleva dos parámetros, uno para la fila (row) y otro para las columnas (column).

# Cuadros de texto
# cuadroNombre=Entry(miFrame)
# cuadroNombre.grid(row=0,column=1, padx=10, pady=10)

# cuadroApellido=Entry(miFrame)
# cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

# cuadroDomicilio=Entry(miFrame)
# cuadroDomicilio.grid(row=2,column=1, padx=10, pady=10)

# Etiquetas, alineadas a la izquierda (west) y determinando que estarán separados por 10 pixeles con el padx y pady
# nombreLabel=Label(miFrame, text="Nombre: ")
# nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# apellidoLabel=Label(miFrame, text="Apellido: ")
# apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

# domicilioLabel=Label(miFrame, text="Domicilio: ")
# domicilioLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

# Otro ejemplo podría ser crear una ventana para inicio de sesión. Para esto precisaremos que la contraseña quede oculta, de la siguiente manera:

# cuadroUsuario=Entry(miFrame)
# cuadroUsuario.grid(row=0,column=1, padx=10, pady=10)

# cuadroContraseña=Entry(miFrame)
# cuadroContraseña.grid(row=1,column=1, padx=10, pady=10)
# cuadroContraseña.config(show="*")

# usuarioLabel=Label(miFrame,text="Usuario: ")
# usuarioLabel.grid(row=0, column=0,sticky="w",padx=10,pady=10)

# contraseñaLabel=Label(miFrame,text="Contraseña: ")
# contraseñaLabel.grid(row=1, column=0,sticky="w",padx=10,pady=10)

###############################################
# Otro widget usado es el Text(). Con este método podremos ingresar textos largos en una interfáz gráfica, construyendo el clásico cuadro de comentarios donde se pueden escribir muchos caracteres. 

# Función creada para que aparezca nuestro nombre cuandio pulsemos enviar.
miNombre=StringVar()

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

cuadroDomicilio=Entry(miFrame)
cuadroDomicilio.grid(row=2,column=1, padx=10, pady=10)

textoComentario=Text(miFrame,width=16, height=5)
textoComentario.grid(row=3, column=1, padx=10, pady=10)

# Para poder agregar una barra de navegación vertical llamaremos al siguiente método
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
# Lo posicionaremos en una columna más a la derecha del texto y le daremos un tamaño que se adapte al text con el sticky "nsew"
scrollVert.grid(row=3,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

domicilioLabel=Label(miFrame, text="Domicilio: ")
domicilioLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

# Por último contaremos con el widget del botón: Button(), usado para colocar código dentro de la programación y así ejecutar acciones en nuestra aplicación. 

def codigoBoton():
    miNombre.set("Enrique")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()

# Ademas le asignamos al cuadroNombre el textvariable=miNombre

# Al pulsar el botón enviar, lo que sea que ingresemos es modificado por el nombre Enrique.

# raiz.mainloop()

################################################
# CREAMOS CALCULADORA
miFrame=Frame(raiz)
miFrame.pack()

# Visor
numeroVisor=StringVar()
visor=Entry(miFrame, textvariable=numeroVisor)
visor.grid(row=1, column=1,padx=10,pady=10,columnspan=4)
visor.config(background="black",fg="green",justify="right")

# Digitación números en el teclado, creamos además una variable global que va a almacenar la operación a realizar.
def numeroPulsado(num):
    global operacion
    # Agregamos en la función la variable global operacion donde evaluaremos con un condicional si la operación es diferente de una cadena vacía muestre el valor del parámetro y si no lo pulsó que concatene el número. Para lograr que sume hay que declarar la variable resultado deforma también global, donde se va a ir almacenando la suma de los valores ingresados y esto lo va a hacer el método suma. 
    if operacion!="":
        numeroVisor.set(num)
        operacion=""
    else:
        numeroVisor.set(numeroVisor.get()+num)

# Función suma
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeroVisor.set(resultado)

# Función total
def total():
    global resultado
    numeroVisor.set(resultado+int(numeroVisor))

# Primer fila
boton7=Button(miFrame,text="7",width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame,text="8",width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame,text="9",width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2, column=4)

# Segunda fila
boton4=Button(miFrame,text="4",width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame,text="5",width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame,text="6",width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame,text="*",width=3)
botonMult.grid(row=3, column=4)

# Tercer fila
boton1=Button(miFrame,text="1",width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame,text="2",width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame,text="3",width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRes=Button(miFrame,text="-",width=3)
botonRes.grid(row=4, column=4)

# Cuarta fila
boton0=Button(miFrame,text="0",width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame,text=",",width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame,text="=",width=3, command=lambda:total())
botonIgual.grid(row=5, column=3)
# Se agrega en el botón el command que llama a la función suma para que al seleccionar este botón desaparezca del visor el número digitado y se comience a ver el nuevo para sumar. 
botonSum=Button(miFrame,text="+",width=3, command=lambda:suma(numeroVisor.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()