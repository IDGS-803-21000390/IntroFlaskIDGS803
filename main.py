from flask import Flask,render_template,request,flash,Response,g
from flask_wtf.csrf import CSRFProtect
from flask import redirect
import forms

app=Flask(__name__)
app.secret_key='esta es la clave secreta'


@app.route("/index")
def index():
    g.nombre='Daniel'
    escuela="UTL!!"
    alumnos=["yazmin","simon","mary","sergio"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    print('dentro del alumno')
    print('Hola {}'.format(g.nombre))
    alum_form=forms.UsarForm(request.form)
    nom=''
    apa=''
    ama=''
    mensaje=''
    #para validar que los campos no tengan un error se agrega el validate 
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("Apellido Paterno: {}".format(apa))
        print("Apellido Materno: {}".format(ama))
    return render_template("alumnos.html",form=alum_form,nom=nom,apa=apa,ama=ama)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.before_request
def before_request():
    #g.nombre='Daniel valencia'
    #regresa la direcion de la pagina endpoint
  
    print('before_request')

@app.after_request
def after_request(response):
    print('ultimo')
    if 'Daniel' not in g.nombre and request.endpoint not in ['/index']:
        return redirect('index.html')
    return response

@app.route("/maestros")
def maes():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return"<p> <h1> hola desde hola <br>Mundo</h1></p>"
@app.route("/user/<string:name>")
def user(name):
    return "<h1> Hola "+name

@app.route("/numero/<int:n>")
def numero(n):
    return "En numeroes {}".format(n)

@app.route("/numero/<int:id>/<string:name>")
def func(id,name):
    return "Id {} Nombre {}".format(id,name)

@app.route("/suma/<float:n1>/<float:n2>")
def fun(n1,n2):
    return "El valor de {} +{} ={}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab="UTL"):
    return "El valor es "+ab


@app.route("/multiplicar",methods=["GET","POST"])
def mul():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return  f'<h1>La multiplicación es: {str(int(num1) * int(num2))} </h1>'
    else:
        return '''
        <from action"/multiplicar" method="POST">
        <laber>n1:</label>
        <input type="text" name="n1"/><br>
        <laber>n2:</label>
        <input type="text" name="n2"/><br>
        <input type="submit"/>
        </from>


    '''


@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")

@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return  f'<h1>La multiplicación es: {str(int(num1) * int(num2))} </h1>'
    

#especificar el metodo que va a arrancar la aplicacion 
if __name__=="__main__":
    app.run(debug=True)    


    