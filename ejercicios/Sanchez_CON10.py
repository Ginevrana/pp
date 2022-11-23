# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#• Ingredientes vegetarianos: Pimiento y tofu.
#• Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pedido = input("¿Quiere pizza vegetariana? s/n: ").lower()

if pedido == "s":
    veg=int(input("Ingrese el N° de uno de los siguientes ingredientes vegetarianos: 1.Pimiento o 2.Tofu. Opción elegida: "))
    if veg ==1:
        print("Su pizza es vegetariana. Incluye mozzarella, tomate y pimiento.")
    else: 
        print("Su pizza es vegetariana. Incluye mozzarella, tomate y tofu.")
else:
    noveg=int(input("Ingrese el N° de uno de los siguientes ingredientes no vegetarianos: 1.Peperoni, 2.Jamón y 3.Salmón. Opción elegida: "))
    if noveg ==1:
        print("Su pizza NO es vegetariana. Incluye mozzarella, tomate y Peperoni.")
    elif noveg ==2:
        print("Su pizza NO es vegetariana. Incluye mozzarella, tomate y Jamón.")
    elif noveg==3:
        print("Su pizza NO es vegetariana. Incluye mozzarella, tomate y Salmón.")
