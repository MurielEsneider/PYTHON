vegetariana = ["pimiento", "tofu"]
noVegetariana = ["Peperoni", "Jamón", "Salmón"]
opcionPizza = int(input("Tipo Pizza\n1.Vegetariana\n2.NoVegetariana\n Seleccione Pizza: "))

if opcionPizza==1:
    print("Ingredientes pizza vegetariana")
    print("1.", vegetariana[0])
    print("2.", vegetariana[1])
    ingrediente = int(input("Selecione ingrediente: (1,2): "))
    ingredentesPizza= ["Tomate", "Mozarella", vegetariana[ ingrediente-1]]
    
if opcionPizza==2:
    print("Ingredientes pizza vegetariana")
    print("1.", noVegetariana[0])
    print("2.", noVegetariana[1])
    print("3.", noVegetariana[2])
    ingrediente = int(input("Selecione ingrediente: (1,2): "))
    ingredentesPizza= ["Tomate", "Mozarella", noVegetariana[ingrediente-1]]
    
print("Ingredientes de la pizza selecionada\n", ingredentesPizza)