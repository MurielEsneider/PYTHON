#funciones
def sumar(x,y):
    return x + y

suma = sumar(5,3)

print(suma)

otrasuma = sumar (2,1)

print(otrasuma)

def mostrarDatos(nombre="María", apellido= "Luna"):
    print(nombre,apellido)
    
mostrarDatos()

mostrarDatos(nombre="Rocio")

mostrarDatos(apellido="Gutierrez")

mostrarDatos(apellido="Castro", nombre="Sebas")

def obtenerCiudad(ciudad:str) -> str:
    return ciudad

cuidad = obtenerCiudad(("Medellín"))

print(cuidad)