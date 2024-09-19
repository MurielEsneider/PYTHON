import pymongo
import os

miConexion = pymongo.MongoClient("mongodb://localhost:27017")

baseDatos = miConexion["Tienda"]
print(baseDatos.list_collection_names())

#Crear objeto a la colección producto

productos = baseDatos["Productos"]
print(type(productos))


#Tareas del crud a la base de datos

def agregar():
    "agregar produto"
    try:
        os.system("cls")
        codigo= int(input("Ingrese codigo del producto"))
        nombre= input("Ingrese nombre del producto")
        precio= int(input("Ingrese precio del producto"))
        categoria= input("Ingrese categoria del producto")
        producto={
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }
        resultado = productos.insert_one(producto)
        if (resultado.acknowledged):
            print("Producto agregar correctamente")
        
    except pymongo.errors as error:
        print(str(error))
        
        
def consultarPorCodigo():
    try:
        os.system("cls")
        codigoAConsultar = int(input("Ingrese código del producto a consultar: "))
        consulta = {"codigo": codigoAConsultar}
        producto = productos.find_one(consulta)
        if(producto):
            print(f"Código: {producto["codigo"]}")
            print(f"Nombre: {producto["nombre"]}")
            print(f"Precio: {producto["precio"]}")
            print(f"Categoria: {producto["categoria"]}")
        else:
            print("No se encontró el producto")
        
    except pymongo.errors as error:
        print(str(error))    
    
def listar():
    try:
        os.system("cls")
        total_productos = productos.count_documents({})  # Cuenta todos los documentos en la colección
        if total_productos > 0:
            listarProductos = productos.find()
            for p in listarProductos:
                print(f"Código: {p["codigo"]}")
                print(f"Nombre: {p["nombre"]}")
                print(f"Precio: {p["precio"]}")
                print(f"Categoria: {p["categoria"]}")
                print("*"*50)
        else:
            print("No hay productos")
        
    except pymongo.errors.PyMongoError as error:
        print(str(error))

def actualizar():
    try:
        os.system("cls")
        codigoProducto = int(input("ingrese el código del producto a actualizar"))
        precio = int(input(f"ingrese nuevo precio del producto a actualizar"))
        datosActualizar = {
            "precio": precio,
            "codigo": codigoProducto
        }
        consulta = {"$set": datosActualizar}
        resultado = productos.update_one(consulta)
        if(resultado.acknowledged):
            print("producto actualizado correctamente")
        else:
            print("No se pudo actualizar producto o no existe el codigo del producto")
        
        
        
        
    except pymongo.errors as error:
        print(str(error))  
        

def eliminar():
    try:
        criterio = int(input("escoja el codigo del producto a eliminar"))
        resultado = productos.delete_one(criterio)
        if(resultado.deleted_count>0):
            print("Producto eliminado correctamente")
        else: 
            print("El producto no existe")

    except pymongo.errors.PyMongoError as error:
        print(str(error))

def agregarMany():


    try:
        os.system("cls")
        cantidad=int(input("Cuántos desea agregar"))
        for i in range(cantidad):
            codigo= int(input("Ingrese codigo del producto"))
            nombre= input("Ingrese nombre del producto")
            precio= int(input("Ingrese precio del producto"))
            categoria= input("Ingrese categoria del producto")
            producto={
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "categoria": categoria
            }
        codigo= 14
        nombre= "camello"
        precio= 4525000
        categoria= "Electrodomestico"
        producto2={
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }
        resultado = productos.insert_many([producto, producto2])
        if (resultado.acknowledged):
            print(f"Producto agregar correctamente,{resultado.inserted_ids}")
        
    except pymongo.errors.PyMongoError as error:
        print(str(error))

""" def agregarMany():
        os.system("cls")
        
        producto1={
            "codigo" = 32,
            "nombre" = "camisa",
            "precio" = 
        }
        codigo= 14
        nombre= "camello"
        precio= 4525000
        categoria= "Electrodomestico"
        producto2={
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }
        resultado = productos.insert_many([producto, producto2])
        if (resultado.acknowledged):
            print(f"Producto agregar correctamente,{resultado.inserted_ids}")
        
    except pymongo.errors.PyMongoError as error:
        print(str(error))
 """


def Menu():
    while True:
        os.system("cls")
        print("\nMenu de opciones")
        print("1. agregar producto")
        print("2. buscar prodcuto por código")
        print("3. eliminar producto")
        print("4. listar todos los productos")
        print("5. actualizar producto")
        print("6. agregar varios productos")
        print("7. salir")
        opcion = int(input("Ingrese opcion del 1-7:"))
        match (opcion):
            case 1: agregar()
            case 2: consultarPorCodigo()
            case 3: eliminar()
            case 4: listar()
            case 5: actualizar()
            case 6: agregarMany()
            case 7: 
                print("salir")
                break
            case _otro: print("opcion fuera del rango")
        input("presione enter para continuar")
        
#agregar()
#consultarPorCodigo()
#listar()
#actualizar()
#eliminar()
#agregarMany() 
Menu()

