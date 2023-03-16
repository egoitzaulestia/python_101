from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

coches = []
coches2 = []

class Coche:
    def __init__(self, id, marca, modelo, features, precioContado, precioFinanciado, image):
        self.id               = id
        self.marca            = marca
        self.modelo           = modelo
        self.features         = features
        self.precioContado    = precioContado
        self.precioFinanciado = precioFinanciado
        self.image            = image


coche1 = Coche(1,"PEUGEOT", "308", "308 1.2 pUREtECH S&S Alture Pack 102kW", 22900, 19913, "coche1b.jpg")
coche2 = Coche(2, "AUDI", "A5", "A5 Sportback 2.0 TFSI 140kW", 25900, 23900, "coche2b.jpg")
coche3 = Coche(3, "RENAULT", "Megane", "Megane 1.5dCi Energy Intens 66kW", 12300, "", "coche3b.jpg")

coches.append(coche1)
coches.append(coche2)
coches.append(coche3)

coche4 = Coche(4,"TESLA", "S", "Tesla S 233kW", 42500, 39000, "coche4b.png")
coche5 = Coche(5, "AUDI", "A5", "A5 Sportback 2.0 TFSI 140kW", 25900, 23900, "coche2b.jpg")
coche6 = Coche(6, "RENAULT", "Megane", "Megane 1.5dCi Energy Intens 66kW", 12300, "", "coche3b.jpg")

coches.append(coche4)
coches2.append(coche5)
coches2.append(coche6)


@app.route("/")
def hola():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    # print("<p>hola</p>")
    # print("fasdf")
    return app.send_static_file("aboutus.html")

# @app.route("/personas")
# def personas():
#     return render_template("personas.html", personas = listaPersonas, empleados = listaObjs)


@app.route("/coches")
def cars():
    return render_template("coches.html", coches = coches, coches2 = coches2)
    

# @app.route("/coches")
# def car():
#     return render_template("coches.html", coches = coches, coches2 = coches2)


@app.route("/coche/<int:id>")
def dicamica(id): # la función tiene un parametro
    # buscar el objeto id == en la lista
    for coche in coches:
        if coche.id == id:
            return render_template("coche.html", coches = coche)
        # elif c.id == 2:
        #     return render_template("coche.html", coches = c)
        # elif c.id == 3:
        #     return render_template("coche.html", coches = c)
        # else:
        #     # return redirect("/index")
        #     return redirect(url_for("hola")) # El nombre debe ser la misma que la definición de la ruta a la que nos dirigimas
    



if __name__ == "__main__":


    app.run(debug=True)
