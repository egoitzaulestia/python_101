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

class Persona(db.Model):
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




if __name__ == "__main__":

    app.run()

    