## Módulos
## Programación estructurada en modulos que se llaman y pueden ser usados en varios programas
## Para reutilizar el código. Divide la aplicación en pequeñas partes, no en una mega aplicación.

## Ejemplo - Archivo funciones matemáticas
##def sumar(n1,n2):
##    print("El resultado de la suma es ", n1+n2)
##
##def restar(n1,n2):
##    print("El resultado de la suma es ", n1-n2)
##
##def multiplicar(n1,n2):
##    print("El resultado de la suma es ", n1*n2)

## Archivo uso de funciones
##import funciones_matematicas
##
##funciones_matematicas.sumar(235,987)
##funciones_matematicas.restar(235,98)
##funciones_matematicas.multiplicacion(235,987)

## Otra manera de hacerlo

##from funciones_matematicas import *

##sumar(654,987)

##------------------------------------------------------------------------------
'''
Paquetes
Son directorios donde se almacenan módulos interrelacionados entre sí, para reorganizar y reutilizar los módulos. Se crea una carpeta con la particularidad para que funcione como paquete en su interior tiene un archivo con el nombre __init__.py (como los constructores)

Para crear un ejemplo:
    1- Creamos una carpeta
    2- Dentro creamos un archivo con __init__.py (dentro queda vacío, es para marcar que estamos trabajando con un directorio)
    3- Aquí iremos guardando todos los módulos que tengan relación entre sí
    4- Creamos un archivo con funciones
    5- En otro archivo creamos un archivo que importe las funciones, de la siguiente manera:
    "from carpeta.archivo import funcion"
    Si queremos llamar todas las funciones en lugar de indicar una función particular ponemos un asterisco (*)
    6- Python tambien crea una carpeta _pycache_

Importante: Si creamos otra carpeta en la cual insertamos el mismo archivo indicador/bandera de que allí hay programación de python, lo cual permite llamar funciones de distintas carpetas (requiriendolas de las distintas ubicaciones)

-----------------------
Archivos Externos
Permite la permanencia de datos para que no se pierdan al cerrar el programa. Ahora empezaremos a trabajar procesar y guardar información.
Para que los datos no se pierdan podemos trabajar con archivos externos o trabajar con db.
Con los primeros tenemos archivos binarios y textos planos. El segundo implica gestores de base de datos como mysql, access, oracle, etc.

Las fases necesarias para guardar información son:
    Creación
    Apertura
    Manipulación
    Cierre

Herramientas principales para trabajar con streams:
    - Módulo Io: son categorías generales y varios respaldos de almacenamiento, se pueden usar para cada una de ellas. Un objeto concreto perteneciendo a cualquiera de estas categorías se llama un file object. Otros términos comunes son stream y file-like object.
    Independientemente de su categoría, cada objeto stream también tendrá varias capacidades: puede ser solamente para lectura, escritura o lectura y escritura. Tambien permite arbitrariamente el acceso aleatorio o solamente acceso secuencial.
    Todos los streams son cuidadosos del tipo de datos que se les provee. Por ejemplo dando un objeto de clase str al meétodo write() de un stream binario lanzará un TypeError.
    • E/S: texto. Espera y produce objetos de clase str. Esto significa que cuando el respaldo de almacenamiento está compuesto de forma nativa de bytes, la codificación y descodificación de datos está hecho de forma transparente tanto como traducción opcional de caracteres de nueva línea específicos de la plataforma.
    La manera más facil de crear un stream de tipo texto es con el método open(), con la opción de especificar una codificación: f=("myfile.txt","r", encoding="utf-8")
    Streams de texto en memoria tambien estan disponibles como objetos de tipo stringIO
    • E/S: binario. Tambien conocido como buffered, espera objetos tipo bytes y produce objetos tipo bytes. Puede ser usada para todos tipos de datos sin texto, y tambien cuando se desea control manual sobre el manejo de dato textual.
    La manera más fácil para crear un stream binario es con el método open() con 'b' en el modo de la cadena de caracteres:
    f=("myfile.jpg","rb")
    Los streams binarios en memoria también están disponeibles como objetos tipo bytesIO
    f=io.bytesio(b"some initial binary data: \x00\x01")
    El API de stream binario está descrito con detalle en la documentación de BufferedIOBase
    • E/S: sin formato. (completar con apunte)
    Fuente: https://docs.python.org/es/3.9/library/io.html

Pasos para importar método open:
    1- Creamos un nuevo programa manejos_archivo.py
    2- Importamos método open así:
        --- from io import open ----
    3- Ahora creamos el archivo externo con el método open() que nos va a pedir dos argumentos:
        -El nombre del archivo
        - El modo como lo vamos a abrir, modo lectura, escritura, append para agregar información a un archivo que ya existe
    4- Vamos a elegir el modo escritura así:
        archivo_texto =open("archivo1.txt","w")
    5- Si lo guardamos y ejecutamos vemos que no nos dice nada pero si vamos a mirar la carpeta veremos que el archivo fue creado.
    6- Generamos variable oracion y le asignamos una frase que vamos a guardar en el archivo
        oracion= "Hermoso día para aprender Python \n en el día de hoy"
    7- Una vez creado vacío le cargamos información, e indicamos que incluya la frase con el método write. Finalmente cerramos:
        archivo_texto.write(oracion)
        archivo_texto.close()

    Resumen: Creación y apertura de archivo - manipulación - cierre

    8- Para verlo, abrimos el archivo en modo lectura y lo volvemos a cerrar, formato similar al de escritura:
        archivo_texto=open("archivo1.txt","r")
        texto=archivo_texto.read()
        archivo_texto.close()
        print(texto)

También podemos encontrar otros métodos como:
    • readlines(): lee linea a linea literal ignorando formatos agregados. Ejemplo:
        from io import open
        archivo_texto=poen("archivo1.txt","r")
        lineas_texto=archivo_texto.readlines()
        archivo_texto=close()
        print(lineas_texto)

        ** Respuesta en consola **
        ['Hermoso día para aprender Python\n','en el día de hoy']

    • append(): cambiando la r por una a para agregar contenido al final del archivo. Ejemplo:
        from io import open
        archivo_texto=open("archivo1.txt","a")
        archivo_texto.write("\n evidentemente siempre es una buena ocasión para aprender")
        archivo_texto.close()

        -> Se corre el programa y cuando lo cambiemos a un formato de lectura (punto 8) y abrimos el archivo con el readlines() nos quedará el siguiente mensaje:
            archivo_texto=open("archivo1.txt","r")
            lineas_texto=archivo_texto.readlines()
            lineas_texto.close()

            print(lineas_texto[0]) // Hermoso día para aprender Python
            print(lineas_texto[1]) // en el día de hoy
            print(lineas_texto[2]) // evidentemente siempre es una buena ocasión para aprender
    • seek(): para posicionar el puntero en algún lugar del archivo, nos pide un parámetro que va a ser el número de caracter donde queremos que se posicione el puntero. 
    En la instrucción print() en combinación con el read() python lee el texto y se posiciona al final del archivo. Si volviera a repetir la misma instrucción, el resultado va a ser nulo porque no encuentra nada después del fin de archivo.
    Usando el método seek(0) posicionamos el puntero de nuevo al principio y vuelve a mostrarnos el texto. Código:
        from io import open
        archivo_texto=open("archivo1.txt", "r")
        archivo_texto.seek(18)
    Ahora si ponemos el puntero en otra posición, elegimos la posición 18 nos mostrará hasta allí con el read(), de la siguiente manera:
        from io import open
        archivo_texto=open("archivo1.txt", "r")
        print(archivo_texto.read(18))
        archivo_texto.close()
        // Respuesta por consola:
            Hermoso día para a
    Si queremos situarnos a la mitad del texto usamos la función len, la usaremos para saber la cantidad de caracteres que tiene el texto y dividirlo a la mitad, de la siguiente manera:
        from io import open
        archivo_texto=open("archivo1.txt", "r")
        archivo_texto.seek(len(archivo_texto.read())/2)
        print(archivo_texto.read())
        archivo_texto.close()
        // Respuesta por consola:
            evidentemente siempre es una buena ocasión para aprender
    • r+, con esta operación podremos abrir y escribir un archivo de la siguiente manera:
        from io import open
        archivo_texto=open("archivo1.txt","r+")
        archivo_texto.write("Comienzo del texto")
        // Respuesta por consola:
            Comienzo del texto aprender Python 
            en el día de hoy 
            evidentemente siempre es una buena ocasión para aprender.
        Como no indicamos nada al cursor cuando lo abrimos se posiciona al principio del archivo y reemplaza lo que había originalmente. Podremos manipular los archivos de texto por líneas, agregando a mitad de este documento la variable de la siguiente manera:
        from io import open
        archivo_texto=open("archivo1.txt","r+")
        lista_texto=archivo_texto.readlines();
        lista_texto[1]="Esta línea la incluimos desde el exterior \n"
        archivo_texto.seek(0)
        archivo_texto.writelines(lista_texto)
        archivo_texto.close()
        // Respuesta por consola:
            Comienzo del texto aprender Python
            Esta linea la incluimos desde el exterior
            evidentemente siempre es una buena ocasión para aprender
        ----------------------------------------------------------------------------------------------------------
        ** SERIALIZACIÓN **
        ¿Qué es? Consiste en guardar un archivo externo (colección, diccionario, objeto) codificado en código binario.
        ¿Para qué? El objetivo es facilitar la distribución si queremos guardarlo en un dispositivo de almacenamiento externo o una base de datos. 
        ¿Cómo? Para esto usamos la biblioteca de Python Pickle, la cual tiene una serie de métodos: Dump(), para el volcado de datos al archivo binario externo y Load(), para la carga de dlos datos al archivo binario externo.

        Ejemplo:
        Crearemos una lista de nombres en un archivo binario y luegvo la rescataremos:
        1- Importaremos la biblioteca pickle que tiene los métodos necesarios para poder serializar
            import pickle
        2- Creamos una lista con 4 nombres
            lista_nombres=["juan","Pedro","Maria","Elena"]
        3- Creamos un archivo externo al que llamaremos Lista_nombre y como segundo argumento debe tener acceso de esritura binaria "wb"
            archivo_binario=open("lista_nombres","wb")
        4- Ahora escribiremos la lista en el archivo externo que creamos en el punto anterior usando el método dump de la biblioteca pickle con dos argumentos: el nombre de la lista que tenemos en memoria y el nombre del archivo donde lo vamos a imprimir.
            pickle.dump("lista_nombres", "wb")
        5- Cerramos con el método close()
            archivo_binario.close
        6- Limpiamos la memoria con la función del()
            del(archivo_binario)
        7- Si corremos el programa veremos el archivo creado. 
        8- Dejamos la importación de la biblioteca pickle para usar sus métodos y comentamos lo demas (el archivo ya fue creado, no necesitamos crearlo nuevamente.).
        9- Creamos un archivo temporal en memoria con el método open, accedemos al archivo guardado en el disco, el primer parámetro que le doy al método es el nombre del archivo "lista_nombres" y como segundo el permiso con el que debe abrirlos es de lectura en formato binario:
            archivo=open("lista_nombres", "rb")
        10- Esa información que acabamos de abrir, la guardamos en una variable que la llamaremos lista, decimos que de la biblioteca utilice el método load() para leer la información que tenemos guardada en memoria en el archivo temporal.
            lista=pickle.load(archivo)
        11- Para ver lo que habíamos guardado usaremos un print() de la lista en memoria, guardamos las modificaciones y lo ejecutamos nuevamente y veremos el contenido de la lista de nombres guardada.
            print(lista)

        Para la serialización de objetos usaremos el código que teniamos de objetos tipo vehículos. De nuevo, se importa la biblioteca pickle, creamos tres objetos de vehículos dentro de la colección automóviles. 
            automoviles=[auto1,auto2,auto3]
        Creamos una variable que la llamamos archivo y crearemos un archivo llamado losautomoviles y el permiso con el que vamos a abrirlo que va a ser escritura de bytes "wb".
            archivo=open("losautomoviles","wb")
        Para escribir la información es el archivo, utilizamos el método dump de la librería con el nombre de la colección donde tenemos los objetos y por otro lado el nombre del archivo donde lo vamos a guardar.
            pickle.dump(automoviles, archivo) 
        Ahora estamos en condiciones de cerrar este archivo y limpiarlo de la memoria.
            archivo.close()
            del(archivo)
        Lo abrimos en modo lectura binaria. Procedemos a leerlo y cargarlo en una variable:
            archivoApertura=open("losautomoviles","rb")
            misAutos=pickle.load(archivoApertura)
        Lo cerramos nuevamente y corremos lo guardado en misAutos, recorriéndolo con un bucle for y el print muestra el estado:
            archivoApertura.close()
            for i in misAutos:
                print(i.estado())
'''


