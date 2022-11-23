# Una panadería vende facturas a $20 cada una. Las facturas que no son del día tiene un descuento del 60%. Escribir un programa que comience leyendo cantidad de facturas vendidas que no son del día. Después el programa debe mostrar el precio habitual de una factura, el descuento que se le hace por no ser fresca y el precio final total.

factura = 20
descuento = 0.60

sind = int(input("Cantidad de facturas frescas vendidas: "))
cond = int(input("Cantidad de facturas del día anterior vendidas: "))

ventasind = sind*factura
ventacond = cond*(factura * descuento)

print(f"El precio habitual de la factura es ${factura}, el descuento que se hace por ser del día anterior es del 60%. El total de facturas con descuento vendidas es de ${ventacond}. Y sin descuento un total de ${ventasind}")

