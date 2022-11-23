# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

nac = input("Ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ")

dia=nac[:nac.find("/")]
mes=nac[nac.find("/")+1:]
mescierre=mes[:mes.find('/')]
año=nac[-4:]

print(f"Nació el día {dia} del mes {mescierre} en el año {año}")