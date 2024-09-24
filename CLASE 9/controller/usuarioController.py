from app import app, usuarios
from flask import render_template, request, redirect, session
import yagmail
import threading


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("frmLogin.html")
    else:
        if request.method == 'POST':
            username = request.form['txtUsername']
            password = request.form['txtPassword']
            usuario = {
                "username":username,
                "password":password
            }
            userExiste = usuarios.find_one(usuario)
            if(userExiste):
                session['user']=usuario   
                email = yagmail.SMTP("eesneider2118@gmail.com", open(".password").read(),
                                encoding='UTF-8')
                asunto="Reporte ingreso al sistema usuario"
                mensaje = f"Se informa que el usuario {username} ha ingresado al sistema"
                
                thread = threading.Thread( target=enviarCorreo, 
                    args=(email,"eesneider2118@gmail.com",asunto, mensaje ))
                thread.start()
                return redirect("/listarProductos")
            else:
                mensaje="Credenciales no validas"
                return render_template("frmLogin.html",mensaje=mensaje)
            
@app.route("/salir")
def salir():
    session.pop('user', None)
    session.clear()
    return render_template("frmLogin.html",mensaje="Ha cerrado la sesión..")

def enviarCorreo(email=None, destinatario=None, asunto=None, mensaje=None):
    email.send(to=destinatario, subject=asunto, contents=mensaje)