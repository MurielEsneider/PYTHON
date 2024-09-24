from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config["UPLOAD_FOLDER"]="./static/image"

contactos=[]


@app.route("/")
def index():
    return "Hola mundo"


@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"



@app.route("/otrosaludo/<mensaje>")
def otroSaludo(mensaje):
    return f"Hola {mensaje}..."



@app.route("/tabla")
def mostrarTabla():    
    return render_template("tabla.html", contactos=contactos) 



@app.route("/vistaRegistrarContacto")
def vistaRegistrarContacto():
    return render_template("frmContacto.html")



@app.route("/producto/<nombre>")
def producto(nombre):
    codigo = request.args.get("codigo")
    return f"Hola {nombre} con código {codigo}"



@app.route("/agregarContacto", methods=["POST"])
def agregarContacto():
    if request.method == "POST":
        nombre= request.form["txtNombre"]
        apellido= request.form["txtApellido"]
        correo= request.form["txtCorreo"]
        
        
        contacto = [nombre,apellido,correo]
        contactos.append(contacto)
        
        archivo = request.files["filefoto"]
        nombreArchivo = secure_filename(archivo.filename)
        listaNombreArchivo = nombreArchivo.rsplit(".",1)
        extension = listaNombreArchivo[1].lower()
        
        posicionUltimoAgregado = len(contactos)-1
        
        nombreFoto = str(posicionUltimoAgregado) + "." + str(extension)
        archivo.save(os.path.join(app.config["UPLOAD_FOLDER"],nombreFoto))
        
        mensaje = "contacto agregardo correctamente"
        return render_template("tabla.html", contactos = contactos)




if __name__ == "__main__":
    app.run(port=3000, debug=True)
