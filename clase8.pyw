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
raiz.title("Ventana de prueba")

# Podemos cambiarle las dimensiones o fijarla para que nadie la pueda cambiar con el siguiente método.
raiz.resizable(True,True)

# Le podemos asignar cualquier imagen como ícono pasandola al formato ico y corriendola con el siguiente método. 
# raiz.iconbitmap("delfin.ico")

# Para fijar el tamaño de la ventana.
raiz.geometry("650x350")

# Podemos cambiar el color de fondo de la ventana con el método config()
raiz.config(bg="green")

# 3) Usamos el método mainloop() para que la venatna pueda estar en ejecución debe estar en una especie de bucle infinito de continua ejecución.
raiz.mainloop()