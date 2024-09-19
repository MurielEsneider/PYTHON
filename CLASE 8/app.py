from flask import Flask, render_template, request, redirect
import pymongo
import pymongo.errors
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
#Crear configuración de carpeta donde se va a guardar las imagenes
app.config["UPLOAD_FOLDER"]= "./static/image"

miConexion = pymongo.MongoClient("mongodb://localhost:27017")
baseDatos = miConexion["Tienda"]
productos = baseDatos["Productos"]

@app.route("/")
def inicio():
    try: 
        mensaje= ""
        listaProductos = productos.find()
        if (listaProductos is None):
            mensaje= "No hay productos registrados"
        
    except pymongo.errors as error:
        mensaje= str(error)
        
    return render_template("index.html", productos=listaProductos, mensaje=mensaje)

@app.route("/agregar", methods=["POST", "GET"])
def agregar():
    if(request.method=="POST"):
        try:
            producto= None
            codigo= int(request.form["txtCodigo"])
            nombre= request.form["txtNombre"]
            precio= int(request.form["txtPrecio"])
            categoria= request.form["txtCategoria"]
            foto= request.files["fileFoto"]
            nombreArchivo = secure_filename(foto.filename)
            listaNombreArchivo = nombreArchivo.rsplit(".",1)
            extension = nombreArchivo[1].lower()
            nombreFoto = f"{codigo}.{extension}"
                    
            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "categoria": categoria,
                "foto": nombreFoto
            }
            
            existe = existeProducto(codigo)
            if (not existe):
                resultado = productos.insert_one(producto)
                if(resultado.acknowledged): 
                    mensaje= "producto agregado correctamente"
                    foto.save(os.path.join(app.config["UPLOAD_FOLDER"],nombreFoto))
                    return redirect("/")
                else:
                    mensaje= "problemas al agregar producto"
            else:
                mensaje = "Ya existe un producto con ese código"
        except pymongo.errors as error:
            mensaje=str(error)
    
        return render_template("frmAgregarProducto.html", mensaje = mensaje, producto = producto)

    else:
        if(request.method == "GET"):
            return render_template("")


def consultar():
    try:
        consulta = {"condigo": codigo}
        producto = productos.find_one(consulta)
        if(producto is not None):
            return True
        else:
            return False
    except pymongo.errors as error:
        mensaje=str(error)



@app.route("/actualizar", methods= ["POST"])
def actualizarProducto():
    try:
        if(request.method=="POST"):
            codigo= int(request.form["txtCodigo"])
            nombre=request.form["txtNombre"]
            precio= int(request.form["txtPrecio"])
            categoria=request.form["txtCategoria"]
            id=objectId(request.form["id"])
            foto = request.files["fileFoto"]
            if(foto.filename!= ""):
                nombreArchivo = secure_filename(foto.filename)
                listaNombreArchivo = nombreArchivo.rsplit(".", 1)
                extension = listaNombre[1].lower()
                nombreFoto = f"{codigo}. {extension}"
                producto = {
                    "_id": id,
                    "codigo": codigo,
                    "nombre": nombre,
                    "precio": precio,
                    "categoria": categoria,
                    "foto": nombreFoto
                }
            else:
                producto = {
                    "_id": id,
                    "codigo": codigo,
                    "nombre": nombre,
                    "precio": precio,
                    "categoria": categoria
                }
            criterio = {"_id": id}
            consulta = {"$set": producto}
            
            existe = productos.find_one({"codigo": codigo, "_id":{"$ne": id}})
            if existe:
                mensaje= "Producto ya existe con este código"
                return render_template("frmAgregarProducto.html", producto = producto, mensaje = mensaje)
            else:
                resultado=productos.update_one(criterio,consulta)
                if(resultado.acknowledged):
                    mensaje="Producto Actualizado"
                    if(foto.filename!= ""):
                        foto.save(os.path.join(app.config["UPLOAD_FOLDER"],nombreFoto))
                    return redirect("/")
    except pymongo.errors as error:
        mensaje= error
        return redirect("/")   


def existeProducto(codigo):
    try:
        consulta = {"codigo": codigo}
        producto = productos.find_one(consulta)
        if(producto is not None):
            return True
        else:
            return False
    except pymongo.errors as error:
        print(error)
        return False
    

if __name__ == "__main__":
    app.run(port= 8000, debug=True)