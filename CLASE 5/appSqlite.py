import sqlite3

baseDatos = "negocio.db"

miConexion = sqlite3.connect(baseDatos)

#insertar categoria

def insertarCategoria():
    try:
        nombre = "Calzado"
        cursor = miConexion.cursor()
        categoria = (nombre,)
        consulta = "INSERT INTO categoria VALUES(null, ?)"
        cursor.execute(consulta, categoria)
        miConexion.commit()
        if(cursor.rowcount==1):
            print(f"categoria insertarda {cursor.lastrowid}")
    
    except miConexion.Error as error:
        print(str(error))
        miConexion.rollback()


def listarCategoria():
    
    try:
        cursor = miConexion.cursor()
        consulta = "SELECT * FROM categoria"
        cursor.execute(consulta)
        categoria = cursor.fetchall()
        if(len(categoria)>0):
            for c in categoria:
                print(c)
        else:
            print("En el momento no hay categoría")
            
    except miConexion.Error as error:
        print(str(error))
        miConexion.rollback()  
    
    return categoria

def insertarProducto():
    try:
        cursor = miConexion.cursor()
        codigo = int(input("ingrese codigo del producto: "))
        nombre =input("nombre de Producto:")
        precio = input("precio del producto:")
        categoria = listarCategoria()
        categoria = int(input("seleccione la categoria del producto: "))
        producto=(codigo,nombre,precio,categoria)
        consulta = "insert into productos values(null,?,?,?,?)"
        cursor.execute(consulta, producto)
        miConexion.commit()
        if(cursor.rowcount==1):
            print(f"producto insertarda {cursor.lastrowid}")
        
    except miConexion.Error as error:
        miConexion.rollback()
        print(str(error))


def listar():
    try:
        cursor = miConexion.cursor()        
        consulta = "SELECT p.proCodigo, p.proPrecio, p.proPrecio, c.catNombre FROM productos p INNER JOIN categoria c on p.proCategoria = c.idCategoria"
        cursor.execute(consulta)
        productos = cursor.fetchall()
        for p in productos:
            print
        else:
            print("no hay productos registrados")
            
    except miConexion.Error as error:
        print(str(error))



def eliminar():
    try:
        cursor = miConexion.cursor()
        proCodigo = int(input("ingrese código del producto a eliminar: "))
        productoEliminar= (proCodigo,)
        consulta = "delete from productos where proCodigo=%s"
        cursor.execute(consulta.productoEliminar)
        miConexion.commit()
        if(cursor.rowcount == 1):
            print("Producto eliminado")
        else:
            print("Codigo no existe")
        cursor.close()
        
    except miConexion.Error as error:
        print(str(error))
        

#insertarCategoria()
#listarCategoria()
#insertarProducto()
#listar()
eliminar()


#ACTIVIDAD
#consultar por categoria
#actualizar
#eliminar
