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
        return redirect("/bienvenido")
      elif request.form['boton'] == "registro":
        return redirect("/crearUsuario")

@app.route("/bienvenido", methods=["GET", "POST"])
def bienvenido():
  name = session['nombre']
  return render_template('bienvenido.html', nombre = name)

@app.route("/registro", methods=["POST","GET"])
def registro():
  if request.method == 'POST': 
      name = request.form['nombre'] 
      session['nombre'] = name
      return redirect("/crearUsuario")
  else:
      return render_template('home.html')

@app.route("/crearUsuario", methods=["GET", "POST"])
def crearUsuario():
  name = session['nombre']
  return render_template('registro.html', nombre = name)


app.run(host='0.0.0.0', port=81)