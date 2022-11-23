# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

factura = int(input("Ingresar total de factura sin IVA: "))
iva = int(input("Porcentaje de IVA (sin porcentual):"))


def calculo(n):
    if iva=="":
        iva==21
    total=n+(n*iva/100)
    print(f"Total de factura con IVA incluido: ${total}")

calculo(factura)