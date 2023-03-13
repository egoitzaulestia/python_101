from flask import Flask, render_template


app = Flask(__name__)


class Empleado:
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad


@app.route("/")
def hola():
    jon = Empleado("Jon", "Smith", 43)
    # nombre = "Jon"
    # apellido = "Smith"
    # return render_template("index.html", name = nombre, lastname = apellido)
    return render_template("index.html", empleado = jon)


@app.route("/adios")
def adios():
    # sHTML = "<h1>ADIOOOOOOOS</h1>"
    # sHTML = sHTML + "<h2>ADIOOOOOOOS</h2>"
    return render_template("adios.html")

@app.route("/middle")
def middle():
    return render_template("middle.html")

if __name__ == "__main__":


    app.run()
