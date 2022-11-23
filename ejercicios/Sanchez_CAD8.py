# Escribir un programa que pregunte por consola el precio de un producto en pesos con dos decimales y muestre por pantalla el número de pesos y el número de céntimos del precio introducido.

precio=input("Ingrese precio de producto con 2 decimales: ")

print("El precio es de", precio[:precio.find('.')], 'pesos y', precio[precio.find('.')+1:], 'centavos.')