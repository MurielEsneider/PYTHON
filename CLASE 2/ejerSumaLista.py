def sumaLista(listaNumeros)->int:
    suma = 0 
    for numero in listaNumeros:
        suma += numero
    return suma

numeros = [2,6,5,5,19]

sumaNumeros = sumaLista(numeros)

print(sumaNumeros)


