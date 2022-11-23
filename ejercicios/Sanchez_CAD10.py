# Escribir un programa que pregunte por consola por los productos de una canasta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos = input("Introducí productos de la canasta de compra separados por comas: ")

print(productos.replace(',', '\n'))