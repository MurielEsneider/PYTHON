palabras  = ["casa", "carro", "mascota", "sapo", " carro"]

for i in range(10):
    palabra = input("ingrese una palabra:")
    palabras.append(palabra)

palabraABuscar = input("Escribe una palabra: ")

#solucion 1
   
palabraABuscar = input("Ingrese Palabra a Buscar: ")

cantidad = palabras.count(palabraABuscar)

print(f"La palabra {palabraABuscar}, se encuentra {cantidad} de veces en la list \n {palabras}")

#solucion2

cantidad = 0
for palabra in palabras:
    if palabra == palabraABuscar:
        cantidad += 1

print(f"La palabra {palabraABuscar}, se encuentra {cantidad} de veces en la list \n {palabras}")


