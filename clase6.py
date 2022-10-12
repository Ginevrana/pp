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
        from io import open
    3- Ahora creamos el archivo externo con el método open() que nos va a pedir dos argumentos:
        -El nombre del archivo
        - El modo como lo vamos a abrir, modo lectura, escritura, append para agregar información a un archivo que ya existe
    4- Vamos a elegir el modo escritura así:
        archivo_texto =open("archivo1.txt","w")
    5- Si lo guardamos y ejecutamos vemos que no nos dice nada pero si vamos a mirar la carpeta veremos que el archivo fue creado.
'''


