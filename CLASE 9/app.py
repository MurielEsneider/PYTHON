from flask import Flask
import pymongo
from flask_cors import CORS
app = Flask(__name__) #crear objeto de tipo flask

CORS(app)

app.secret_key="444"

app.config['UPLOAD_FOLDER']='./static/images'

miConexion = pymongo.MongoClient("mongodb://localhost:27017")

baseDatos = miConexion['Tienda']

productos = baseDatos['Productos']

usuarios = baseDatos['Usuarios']

if __name__=="__main__":
    from controlador.productoController import *
    from controlador.usuarioController import * 
    app.run(port=4000,debug=True)
    
    
