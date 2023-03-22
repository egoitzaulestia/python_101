from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

class User:
    def __init__(self, nombre, apellido, email):
        self.nombre   = nombre
        self.apellido = apellido
        self.email    = email


@app.route("/")
def index():
    return "Main Page - Index"

@app.route("/form1", methods = ["GET", "POST"])
def form1():
    if request.method == "POST":
        nombre = request.form.get("txtNombre")
        apellido = request.form["txtApellido"]
        email = request.form["txtEmail"]
        textArea = request.form["txtArea"]

        if nombre != "admin":
            sText = "Admin: " + nombre + ", " + apellido + ", " + email
        # if nombre == "admin" and pwd == "qwerty":
        #     return redirect("admin.hmtl")
        # else:
        #     return redirect("login.html")
        
        # with open("datos.txt"):
        #     f.write(nombre)
        
        # user = User()
        # user.nombre = nombre
        # user.email = email
        # user.save()



        # print(nombre)
        # print(apellido)
        # print(email)
        # # print(textArea)
        # listaDatos = []
        # listaDatos.append(nombre)
        # listaDatos.append(apellido)
        # listaDatos.append(email)

        with open("data.txt", "a") as f:
            f.write(nombre, apellido, email)
            f.write("\n")
            # f.write(nombre, apellido, email, textArea)

        return "Datos " + nombre + apellido + email
    else: # GET
        return render_template("form1.html")



if __name__ == "__main__":

    app.run(debug=False)

    
