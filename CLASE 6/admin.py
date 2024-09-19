import pymongo
import os

# Establecer la conexión con la base de datos
miConexion = pymongo.MongoClient("mongodb+srv://Muriel:123454321@cluster0.evyojh5.mongodb.net/Tienda?retryWrites=true&w=majority&appName=Cluster0")
baseDatos = miConexion["Tienda"]
print(baseDatos.list_collection_names())


# Crear objeto a la colección producto
productos = baseDatos["Productos"]
print(type(productos))


# Función para agregar producto
def agregar():
    "agregar producto"
    while True:
        try:
            codigo = int(input("Ingrese código del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            precio = int(input("Ingrese precio del producto: "))
            categoria = input("Ingrese categoría del producto: ")
            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "categoria": categoria
            }
            resultado = productos.insert_one(producto)
            if resultado.acknowledged:
                print("Producto agregado correctamente")
            break  # Salir del bucle si todo fue exitoso
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar un número entero para el código y el precio.")
        except pymongo.errors.PyMongoError as error:
            print(str(error))


# Función para consultar producto por código
def consultarPorCodigo():
    try:
        os.system("cls" if os.name == 'nt' else 'clear')
        codigoAConsultar = int(input("Ingrese código del producto a consultar: "))
        consulta = {"codigo": codigoAConsultar}
        producto = productos.find_one(consulta)
        if producto:
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoría: {producto['categoria']}")
        else:
            print("No se encontró el producto")
    except pymongo.errors.PyMongoError as error:
        print(str(error))



# Función para listar todos los productos
def listar():
    try:
        os.system("cls" if os.name == 'nt' else 'clear')
        total_productos = productos.count_documents({})
        if total_productos > 0:
            listarProductos = productos.find()
            for p in listarProductos:
                print(f"Código: {p['codigo']}")
                print(f"Nombre: {p['nombre']}")
                print(f"Precio: {p['precio']}")
                print(f"Categoría: {p['categoria']}")
                print("*" * 50)
        else:
            print("No hay productos")
    except pymongo.errors.PyMongoError as error:
        print(str(error))



# Función para actualizar un producto
def actualizar():
    try:
        os.system("cls" if os.name == 'nt' else 'clear')
        codigoProducto = int(input("Ingrese el código del producto a actualizar: "))
        nuevoPrecio = int(input("Ingrese el nuevo precio del producto: "))
        consulta = {"codigo": codigoProducto}
        datosActualizar = {"$set": {"precio": nuevoPrecio}}
        resultado = productos.update_one(consulta, datosActualizar)
        if resultado.modified_count > 0:
            print("Producto actualizado correctamente")
        else:
            print("No se pudo actualizar el producto o no existe el código del producto")
    except pymongo.errors.PyMongoError as error:
        print(str(error))

# Función para eliminar un producto
def eliminar():
    try:
        os.system("cls" if os.name == 'nt' else 'clear')
        codigoProducto = int(input("Ingrese el código del producto a eliminar: "))
        consulta = {"codigo": codigoProducto}
        resultado = productos.delete_one(consulta)
        if resultado.deleted_count > 0:
            print("Producto eliminado correctamente")
        else:
            print("El producto no existe")
    except pymongo.errors.PyMongoError as error:
        print(str(error))



# Función para agregar varios productos
def agregarMany():
    try:
        os.system("cls" if os.name == 'nt' else 'clear')
        cantidad = int(input("¿Cuántos productos desea agregar? "))
        productos_lista = []
        for _ in range(cantidad):
            codigo = int(input("Ingrese código del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            precio = int(input("Ingrese precio del producto: "))
            categoria = input("Ingrese categoría del producto: ")
            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "categoria": categoria
            }
            productos_lista.append(producto)

        resultado = productos.insert_many(productos_lista)
        if resultado.acknowledged:
            print(f"Productos agregados correctamente: {resultado.inserted_ids}")
    except pymongo.errors.PyMongoError as error:
        print(str(error))

# Función de menú principal
def Menu():
    while True:
        os.system("cls" if os.name == 'nt' else 'clear')
        print("\nMenú de opciones")
        print("1. Agregar producto")
        print("2. Buscar producto por código")
        print("3. Eliminar producto")
        print("4. Listar todos los productos")
        print("5. Actualizar producto")
        print("6. Agregar varios productos")
        print("7. Salir")
        opcion = int(input("Ingrese opción del 1-7: "))
        if opcion == 1:
            agregar()
        elif opcion == 2:
            consultarPorCodigo()
        elif opcion == 3:
            eliminar()
        elif opcion == 4:
            listar()
        elif opcion == 5:
            actualizar()
        elif opcion == 6:
            agregarMany()
        elif opcion == 7:
            print("Salir")
            break
        else:
            print("Opción fuera del rango")
        input("Presione Enter para continuar")

# Ejecutar el menú
Menu()
