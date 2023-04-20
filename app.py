from flask import Flask, request, render_template, session

#crear objeto de tipo flask
app = Flask(__name__)

#contraeña secreta
app.secret_key = "mySecretKey"

#Raiz del sitio
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/mision")
def mision():
    return render_template("mision.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/login")
def loging():
    return render_template("login.html")

@app.route("/iniciarSesion", methods=["POST"])
def iniciarSesion():
    usuario = request.form["txtUsuario"]
    password = request.form["txtPassword"]
    if(usuario == "Admin" and password == "Admin"):
        session["user"] = "Admin"
        return render_template("administrador/inicio.html")
    elif(usuario == "Asis" and password == "Asis"):
        session["user"] = "Asis"
        return render_template("asistente/inicio.html")
    else:
        return render_template("login.html", mensaje="Credenciales NO validas!")

@app.route("/salir")
def salir():
    session.clear()
    return render_template("login.html", mensaje="Ha cerrado sesión!")

@app.route("/administrador")
def inicioAdmin():
    if("Admin" in session):
        return render_template("administrador/inicio.html")
    else:
        return render_template("login.html",mensaje="Debe primero inciar sesión!")
    
@app.route("/asistente")
def inicioAsis():
    if("User" in session):
        return render_template("asistente.html")
    else:
        return render_template("login.html",mensaje="Debe primero inciar sesión!")
    
#iniciar el servidor web
if __name__=='__main__':
    app.run(port=3000,debug=True)