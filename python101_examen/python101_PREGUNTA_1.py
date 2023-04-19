# Examen Python101
# PREGUNTA_1
# ————————————————————————————————————————————————————————————————————
# Hemos recibido unas notas de una programadora,
# donde nos dice que tenemos que construir las clases necesarias para Animal, Perro y Pajaro.
# ————————————————————————————————————————————————————————————————————
# Tenemos que crear la clase Animal y después dos clases, Perro y Pajaro, 
# que heredarán algunos atributos y métodos de la clase Animal
# ————————————————————————————————————————————————————————————————————
# Características de la clase Perro:
# - patas (por ejemplo, 4)
# - nombre
# - raza
# - hacerRuido() # imprime Woof, woof
# - correr() # imprime estoy corriendo

# Características de la clase Pajaro:
# - patas (por ejemplo, 2)
# - nombre
# - hacerRuido() # imprime Tweet, tweet
# - volar() # todavia no tenemos detalles de este método
# ————————————————————————————————————————————————————————————————————
# Requisitos del programa a realizar:
# • Crear 3 objetos y sus atributos y métodos
# • Crear código para instanciar un Perro
# • Ejecutar el método hacerRuido() y correr() del Perro
# ————————————————————————————————————————————————————————————————————


# Creamos la clase Animal
class Animal:
    def __init__(self, nombre, edad, especie, raza, patas, pais, velocidad, ruido):
        # Iniciamos los atributos de la clase mediante "self. ...""
        self.nombre = nombre
        self.edad   = edad
        self.especie = especie
        self.raza   = raza
        self.patas  = patas
        self.pais   = pais
        self.alive  = "vivo" 
        self.velocidad = velocidad
        self.ruido = ruido

        if velocidad <= 5:
            pass
        elif velocidad >=6 or velocidad <=20:
            pass
        else:
            pass
    
    def hacerRuido(self):
        return print(f"{self.nombre} hace: {self.ruido}!")
    
    def correr(self):
        return print(f"{self.nombre} está corriendo!")
    
    def volar(self):
        return print(f"{self.nombre} está volando!")

    def salud(self):
        if self.alive == "muerto":
            return print(f"{self.nombre} está {self.alive} :_(")
        else:
            return print(f"{self.nombre} está {self.alive} :)")

    def getNombre(self):
        return print(f"Nombre del {self.especie}: {self.nombre}")
    

# Creamos la clase Perro que hereda atributos y métodos de la calse Animal
class Perro(Animal):
    def __init__(self, nombre, edad, especie, raza, patas, pais, velocidad, ruido):
        # Heredamos atributos y métodos  mediante super(). 
        super().__init__(nombre, edad, especie, raza, patas, pais, velocidad, ruido)

    def hacerRuido(self):
        return print(f"{self.nombre} hace: {self.ruido}!")
    
    def correr(self):
        return print(f"{self.nombre} está corriendo!")


# Creamos la clase Pajaro que hereda atributos y métodos de la calse Animal
class Pajaro(Animal):
    def __init__(self, nombre, edad, especie, raza, patas, pais, velocidad, ruido, alas):
        # Heredamos atributos y métodos  mediante super(). 
        super().__init__(nombre, edad, especie, raza, patas, pais, velocidad, ruido)
        self.alas = alas

    def hacerRuido(self):
        return print(f"{self.nombre} hace: {self.ruido}!")
    
    def volar(self):
        return print(f"{self.nombre} está volando!")

    def tipoAlas(self):
        return print(f"{self.nombre} es un {self.especie} de alas {self.alas}.")

# Inicializamos el programa
if __name__ == "__main__":
    # pass # El pass nos deja correr el programa sin haber introducido un dato (aunque no muestre nada)

    # Instanciamos el objeto Perro
    dax = Perro("Dax", 7, "perro", "German Shepard", 4, "Germany", 34, "WOOF! WOOF!!")
    dax.hacerRuido()
    dax.getNombre()
    dax.correr()

    # Instanciamos el objeto Pajaro
    piolin = Pajaro("Piolin", 0.2, "pájaro", "Canary", 2, "US", 13, "Tweet, tweet, tweet!", "pequeñas")
    piolin.hacerRuido()
    piolin.volar()
    piolin.getNombre()
    piolin.tipoAlas()
    piolin.salud()
    piolin.alive = "muerto"
    piolin.salud()


    """
    Salida en terminal:

    WOOF! WOOF!!
    Nombre del perro: Dax
    Dax está corriendo!
    Tweet, tweet, tweet!
    Piolin está volando!
    Nombre del pájaro: Piolin
    Piolin es un pájaro de alas pequeñas.
    Piolin está vivo :)
    Piolin está muerto :_(
    
    """
