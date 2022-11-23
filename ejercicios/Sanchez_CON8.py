# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 20.400$ multiplicada por la puntuación del nivel.
# Escribir un programa que lea la puntuación del empleado e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el empleado

puntaje=float(input("Ingrese puntaje de empleado: "))
dinero=20400

if puntaje<0.4:
    print("Nivel de rendimiento: Inaceptable. No recibe beneficio")
elif puntaje >=0.4 and puntaje<0.6:
    print(f"Nivel de rendimiento: Aceptable. Recibe beneficio de ${dinero}")
elif puntaje >=0.6:
    print(f"Nivel de rendimiento: Meritorio. Recibe beneficio de ${dinero*2}")
