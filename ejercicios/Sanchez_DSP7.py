peso=float(input("Ingrese su peso: "))
estatura=float(input("Ingrese su estatura: "))

imc=round(float(peso/(estatura*estatura)),2)

print(f"Tu índice de masa corporal es {imc}")