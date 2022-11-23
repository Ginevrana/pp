# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 360.000 $ mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad= int(input("Ingrese su edad: "))
sueldo=int(input("Ingrese su ingreso mensual: "))

if edad>16 and sueldo>360000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")