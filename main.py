from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "clave_cualquiera"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ingreso', methods=["GET", "POST"])
def ingreso():
    if request.method == 'POST': 
      if request.form['boton'] == "ingreso":
        name = request.form['nombre'] 
        session['nombre'] = name
        password = request.form['contraseña'] 
        return redirect("/bienvenido")
      elif request.form['boton'] == "registro":
        name = request.form['nombre'] 
        password = request.form['contraseña'] 
        return redirect("/registro")

@app.route("/bienvenido", methods=["GET", "POST"])
def bienvenido():
  name = session['nombre']
  return render_template('bienvenido.html', nombre = name)

@app.route("/registro", methods=["POST","GET"])
def registro():
  return render_template('registro.html')

@app.route("/crearUsuario", methods=["GET", "POST"])
def crearUsuario():
  if request.method == 'POST': 
    name = session['nombre']
    session['nombre']= request.form['nombre']
    session['contraseña']=request.form['contraseña']
    return render_template('bienvenido.html', nombre = name)


app.run(host='0.0.0.0', port=81)