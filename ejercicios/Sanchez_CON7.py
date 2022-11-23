# Los tramos impositivos para la declaración de la renta en un determinado país. Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

sueldo=int(input("Ingrese su ingreso anual: "))

if sueldo<100000:
    print("Tiene que tributar 5%")
elif sueldo >= 100000 and sueldo<200000:
    print("Tiene que tributar 15%")
elif sueldo >= 200000 and sueldo<350000:
    print("Tiene que tributar 20%")
elif sueldo >= 350000 and sueldo<600000:
    print("Tiene que tributar 30%")
elif sueldo >= 600000:
    print("Tiene que tributar 45%")