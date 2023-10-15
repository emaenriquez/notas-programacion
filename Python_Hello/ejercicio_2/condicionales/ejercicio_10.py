# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza = input('usted quiere una pizza vegetariana o una no vegetariana')
ingrediente_vegetarianos = list(['mozzarella','tomate'])
ingrediente_no_vegetarianos = list(['mozzarella','tomate'])

if pizza == 'vegetariana':
    ingrediente = input('que igrediente desea solo puede uno nomas: Pimiento y tofu ')
    ingrediente_vegetarianos.append(ingrediente)
    print(f'sus ingredientes son {ingrediente_vegetarianos}')
elif pizza == 'no vegetariana':
    ingrediente = input('que igrediente desea solo puede uno nomas: Peperoni, Jamón y Salmón ')
    ingrediente_no_vegetarianos.append(ingrediente)
    print(f'sus ingredientes son {ingrediente_no_vegetarianos}')
