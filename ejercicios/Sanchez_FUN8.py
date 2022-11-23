# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación estandard

lista = (1,5,8,7,65,48)

def media(a):
    for i in lista:
        print(i**2)
media(lista)

def estadistica(a):
    dict = {}
    dict['media'] = sum(a)/len(a)
    dict['varianza'] = sum(media(a))/len(a)-dict['media']**2
    dict['desviacion tipica'] = dict['varianza']**0.5
    print(dict)

estadistica(lista)