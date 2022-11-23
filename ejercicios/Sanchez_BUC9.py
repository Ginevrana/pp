# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

cont= input("Registre una contraseña: ").lower()
conf=input("Ingrese contraseña registrada: ").lower()

while cont != conf:
    conf=input("Ingrese contraseña registrada: ").lower()    
print("Contraseña correcta.")