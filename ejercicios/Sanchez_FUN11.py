# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

frase=input("Ingrese una frase: ")

def contar_palabras(frase):
    frase = frase.split()
    palabras = {}
    for i in frase:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mas_rep(palabras):
    max_pal = ''
    max_freq = 0
    for pal, freq in palabras.items():
        if freq > max_freq:
            max_pal = pal
            max_freq = freq
    print(max_pal, max_freq)


print(contar_palabras(frase))
mas_rep(contar_palabras(frase))