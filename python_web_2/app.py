from flask import Flask, render_template

app = Flask(__name__)


class Producto:
    def __init__(self, marca, modelo, precio, electrodos):
        self.marca      = marca
        self.modelo     = modelo
        self.precio     = precio
        self.electrodos = electrodos

@app.route("/")
def inicio():
    napse = Producto("NIT", "Napse", 250, 4)
    egx   = Producto("Upside Down Labs", "EXG Pill", 45, 2)

    nit = "Neural Interface Technologies"

    productos = [napse, egx]

    return render_template("index.html", nit = nit, pd1 = napse, pd2 = egx, productos = productos)

@app.route("/proposito")
def proposito(): # Es posible que no pueda repetir el nombre
    return render_template("proposito.html")


if __name__ == "__main__":

    app.run()
