from flask import Flask, render_template

app = Flask(__name__)


class Producto:
    def __init__(self, marca, modelo, precio, electrodos):
        self.marca      = marca
        self.modele     = modelo
        self.precio     = precio
        self.electrodos = electrodos

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/proposito")
def inicio(): # Es posible que no pueda repetir el nombre
    return render_template("proposito.html")


