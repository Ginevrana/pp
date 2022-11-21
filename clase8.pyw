from tkinter import *
raiz=Tk()

# raiz.title("Ventana de prueba")
# raiz.resizable(True,True)

# raiz.config(bg="green")

# miFrame=Frame()

# miFrame.pack(side="right", ancho="s")

# miFrame.config(bg="red")
# miFrame.config(width="650", height="350")
# miFrame.config(bd=35)
# miFrame.config(relief="groove")
# miFrame.config(cursor="hand2")


#############################################
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

#############################################

# miFrame=Frame(raiz, width=1200, height=600)
# miFrame.pack()

# # cuadroTexto=Entry(miFrame)
# # cuadroTexto.place(x=100,y=100)

# # nombreLabel=Label(miFrame, text="Nombre: ")
# # nombreLabel.place(x=120, y=100)

# # Como así no queda bien, se usa el grid

# # cuadroNombre=Entry(miFrame)
# # cuadroNombre.grid(row=0,column=1, padx=10, pady=10)

# # cuadroApellido=Entry(miFrame)
# # cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

# # cuadroDomicilio=Entry(miFrame)
# # cuadroDomicilio.grid(row=2,column=1, padx=10, pady=10)

# # nombreLabel=Label(miFrame, text="Nombre: ")
# # nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# # apellidoLabel=Label(miFrame, text="Apellido: ")
# # apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

# # domicilioLabel=Label(miFrame, text="Domicilio: ")
# # domicilioLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

# # Para ocultar lo ingresado como por ejemplo en una casilla de contraseña se hace de la siguiente manera:

# # cuadroUsuario=Entry(miFrame)
# # cuadroUsuario.grid(row=0,column=1, padx=10, pady=10)

# # cuadroContraseña=Entry(miFrame)
# # cuadroContraseña.grid(row=1,column=1, padx=10, pady=10)
# # cuadroContraseña.config(show="*")

# # usuarioLabel=Label(miFrame,text="Usuario: ")
# # usuarioLabel.grid(row=0, column=0,sticky="w",padx=10,pady=10)

# # contraseñaLabel=Label(miFrame,text="Contraseña: ")
# # contraseñaLabel.grid(row=1, column=0,sticky="w",padx=10,pady=10)


# # Ahora agregaremos el cuadro para textos extensos:

# miNombre=StringVar()

# cuadroNombre=Entry(miFrame,textvariable=miNombre)
# cuadroNombre.grid(row=0,column=1, padx=10, pady=10)

# cuadroApellido=Entry(miFrame)
# cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

# cuadroDomicilio=Entry(miFrame)
# cuadroDomicilio.grid(row=2,column=1, padx=10, pady=10)

# textoComentario=Text(miFrame,width=16, height=5)
# textoComentario.grid(row=3, column=1, padx=10, pady=10)

# scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
# scrollVert.grid(row=3,column=2,sticky="nsew")
# textoComentario.config(yscrollcommand=scrollVert.set)


# nombreLabel=Label(miFrame, text="Nombre: ")
# nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# apellidoLabel=Label(miFrame, text="Apellido: ")
# apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

# domicilioLabel=Label(miFrame, text="Domicilio: ")
# domicilioLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

# comentarioLabel=Label(miFrame, text="Comentario: ")
# comentarioLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

# def codigoBoton():
#     miNombre.set("Enrique")

# botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
# botonEnvio.pack()

# Al pulsar el botón enviar, lo que sea que ingresemos es modificado por el nombre Enrique.


################################################
# CREAMOS CALCULADORA
miFrame=Frame(raiz)
miFrame.pack()

# Visor
numeroVisor=StringVar()
visor=Entry(miFrame, textvariable=numeroVisor)
visor.grid(row=1, column=1,padx=10,pady=10,columnspan=4)
visor.config(background="black",fg="green",justify="right")

# Digitación números en el teclado
def numeroPulsado(num):
    global operacion
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
botonIgual=Button(miFrame,text="=",width=3)
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame,text="+",width=3, command=lambda:suma(numeroVisor.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()