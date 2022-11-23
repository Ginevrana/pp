# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el costo total con 8 dígitos enteros y 2 decimales.

prod=input("Ingrese producto: ")
precio=round(float(input("Ingrese su precio: ")),2)
cant=int(input("Ingrese cantidad: "))
total=round((precio*cant),2)

print(f"{prod}: valor unitario ${precio}. Valor total de {cant} unidades: ${total}")