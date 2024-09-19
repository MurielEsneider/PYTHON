import pymysql as mysql

user = "root"
password ="CTPI2024*"
baseDatos ="TIENDAADSO"
host="localhost"

miConexion = mysql.connect(host=host,user=user, db=baseDatos, password=password)

def insertar():
    try:
        #creando un producto en un tupla
        
        producto = ("Nevera", 2500000, "Electrodoméstico")
        cursor = miConexion.cursor()
        
        #texto consulta
        
        consulta = "insert into producto values(%s, %s, %s)"
        
        #ejercuta la consulta
        
        resultado = cursor.execute(consulta, producto)
        miConexion.commit()
        if (cursor.rowcount==1):
            print("Producto insertado")
        
        
    except miConexion.Error as error:
        print (str(error))
        

def listar():
    try:
        #crear el cursor
        
        cursor = miConexion.cursor()
        
        #texto de la consulta
        
        consulta = "select * from producto"
        resultado = cursor.execute(consulta)
        productos = cursor.fetchall()
        print(productos)
        if (len(productos)>0):
            #imprimir
            for p in productos:
                print(p)
        else:
            print("no hay productos registrados")
            
    except miConexion.Error as error:
        print(str(error))



def consultarPorCodigo():
    try:
        cursor = miConexion.cursor()
        codigo = input ("ingrese código del producto a consultar: ")
        productoConsultar = (codigo,)
        consulta = "select * from producto where proCodigo = %s"
        cursor.execute(consulta, productoConsultar)
        producto = cursor.fetchone()
        if(producto):
            print(producto)
        else:
            print("no existe producto con este código")
    
    except miConexion.Error as error:
        print(str(error))
    return producto


def actualizar():
    try:
        producto = consultarPorCodigo()
        cursor = miConexion.cursor()
        nuevoPrecio = producto[3]*1.20
        codigoProductActualizar = producto[1]
        datosActualizar = (nuevoPrecio, codigoProductActualizar)
        consulta = "update producto set proPrecio = %s where proCodigo = %s"
        resultado = cursor.execute(consulta, codigoProductActualizar, productoActualizar)
        miConexion.commit()
        if(cursor.rowcount == 1):
            print("producto actualizado")
        else:
            print("problemas al actualizar")
        
    except miConexion.Error as error:
        print(str(error))

def eliminar():
    try:
        cursor = miConexion.cursor()
        codigo = int(input("ingrese código del producto a eliminar: "))
        productoEliminar= (codigo,)
        consulta = "delete from producto where proCodigo=%s"
        cursor.execute(consulta.productoEliminar)
        miConexion.commit()
        if(cursor.rowcount == 1):
            print("Producto eliminado")
        else:
            print("Codigo no existe")
        cursor.close() #para cerrar
        
    except miConexion.Error as error:
        print(str(error))
        
        
           
insertar()
#consultarPorCodigo()
