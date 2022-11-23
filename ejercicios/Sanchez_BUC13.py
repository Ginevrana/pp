# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que termina.

loro = input("Todo lo que diga será repetido hasta que diga salir: ").lower()

while loro != "salir":
    print(loro)
    loro = input("Todo lo que diga será repetido hasta que diga salir: ")
