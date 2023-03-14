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


class Coche:
    def __init__(self, id, image, marca, modelo, features, precioContado, precioFinanciado):
        self.id               = id
        self.image            = image
        self.marca            = marca
        self.modelo           = modelo
        self.features         = features
        self.precioContado    = precioContado
        self.precioFinanciado = precioFinanciado

coches = []

coche1 = Coche(1, "PEUGEOT", "308", "308 1.2 pUREtECH S&S Alture Pack 102kW", 22900, 19913)
coche2 = Coche(2, "AUDI", "A5", "A5 Sportback 2.0 TFSI 140kW", 25900, 23900)
coche3 = Coche(3, "RENAULT", "Mégane", "Mégane 1.5dCi Energy Intens 66kW", 12300, "")

coches.append(coche1)
coches.append(coche2)
coches.append(coche3)

@app.route("/")
def hola():
    jon = Empleado(1, "Jon", "Smith", 43)
    # nombre = "Jon"
    # apellido = "Smith"
    # return render_template("index.html", name = nombre, lastname = apellido)
    return render_template("index.html", empleado = jon)


@app.route("/aboutus")
def aboutus():
    # print("<p>hola</p>")
    # print("fasdf")
    return app.send_static_file("aboutus.html")


@app.route("/personas")
def personas():
    return render_template("personas.html", personas = listaPersonas, empleados = listaObjs)


@app.route("/coches")
def cars():
    return render_template("coches.html", coches = coches)
    
@app.route("/dinamica/<int:id>")
def dicamica(id):
    if id == 10:
        return "Has seleccionado dinámica 10!!!"
    else:
        # return redirect("/index")
        return redirect(url_for("hola")) # El nombre debe ser la misma que la definición de la ruta a la que nos dirigimas
    


if __name__ == "__main__":


    app.run(debug=True)
