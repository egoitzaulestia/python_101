from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

listaPersonas = ["Maria", "Juan", "Jon", "Isabel", "Diego", "Ego"]

listaObjs = []

class Empleado:
    def __init__(self, id, nombre, apellido, edad):
        self.id       = id
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad

maria = Empleado(1, "Maria", "Rubio", 34)
juan = Empleado(2, "Juan", "Bravo", 58)
jon = Empleado(3, "Jon", "Smith", 25)
isabel = Empleado(4, "Isabel", "Padilla", 63)
listaObjs.append(maria)
listaObjs.append(juan)
listaObjs.append(jon)
listaObjs.append(isabel)

@app.route("/")
def hola():
    jon = Empleado(1, "Jon", "Smith", 43)
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

@app.route("/aboutus")
def aboutus():
    # print("<p>hola</p>")
    # print("fasdf")
    return app.send_static_file("aboutus.html")


@app.route("/personas")
def personas():
    return render_template("personas.html", personas = listaPersonas, empleados = listaObjs)


@app.route("/dinamica/<int:id>")
def dicamica(id):
    if id == 10:
        return "Has seleccionado dinámica 10!!!"
    else:
        # return redirect("/index")
        return redirect(url_for("hola")) # El nombre debe ser la misma que la definición de la ruta a la que nos dirigimas
    


if __name__ == "__main__":


    app.run(debug=True)
