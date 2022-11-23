# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
lista = (1,5,8,7,65,48)

def media(a):
    promedio=round(sum(a)/len(a),2)
    print(f"La media de {a}, es: {promedio}")

media(lista)