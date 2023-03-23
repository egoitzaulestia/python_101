from flask import Flask, request, render_template, redirect, url_for
# import sqlalchemy
from flask_sqlalchemy import *
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# la RUTA PRINCIPAL DE ESTE ARCHIVO
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Persona(db.Model): # " db.Model " ---> Hace qeu cualquier objeto que lo ereda es mandado a una tabla llamada de la misma manera. 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)


# ESTO SE CORRE SOLO UNA VEZ PARA CREAR LA BASE DE DATOS. DESPUÉS SE BORRA
## with app.app_context():
##     db.create_all()

# jon = Persona()
# jon.id = 4
# jon.nombre = "Jon"


@app.route("/")
def index():
    jon = Persona()
    jon.name = "jon"
    db.session.add(jon)
    db.session.commit()

    return "Hola"


@app.route("/sql_todos")
def sql_todos():
    # personas = Persona.query.all() # Una lista de objetos
    # return render_template("personas.html", personas = personas)
    personas = Persona.query.filter_by(name = "Maria") # esto es como si fuera un WHERE, esto es ORM
    # personas = Persona.query.filter_by(salario > 2000)
    s = ""
    for p in personas:
        s = s + " " + p.name
    return s


@app.route("/sql_todo")
def sql_todo():
    # jon = Persona.query.get(1) # esto es como si fuera un WHERE
    # # persona = Persona.query.get(3) # esto saca el primero de la lista

    # db.session.delete(jon)
    # db.session.commit()

    ego = Persona.query.get(3) # esto es como si fuera un WHERE
    ego.name = "Egoitz"
    db.session.add(ego)
    db.session.commit()
    
    # s = "User deleted"
    s = "User updated"
    return s

# @app.route("/sql_delete")
# def sql_delete()

if __name__ == "__main__":

    app.run(debug=True)

    