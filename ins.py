class Instrumento:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.__precio_coste = precio - 20
    
    def tocar(self):
         print(f"{self.nombre} está sonando.")

class Piano(Instrumento):
    def __init__(self, nombre, tipo, precio, teclas, musico):
        super().__init__(nombre, tipo, precio)
        self.teclas = teclas
        self.musico = musico

    def tocar(self): # Estamos copiando
        print(f"{self.musico.nombre} esta tocando: ding ding ding")
    
class Bateria(Instrumento):
    def __init__(self, nombre, tipo, precio, tambores, platos):
        super().__init__(nombre, tipo, precio)
        self.tambores = tambores
        self.platos = platos
    
    def tocar(self):
        print(f"{self.nombre} esta tocando: Tu-pa-tutu-pa!")

class Trompeta(Instrumento):
    def __init__(self, nombre, tipo, precio, boquilla):
        super().__init__(nombre, tipo, precio)
        self.boquilla = boquilla

    def tocar(self):
        print(f"{self.nombre} esta tocando: Pa-pa-para-ba!!")

class Musico:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tocar(self):
        print(f"{self.nombre} esta tocando: Pa-pa-para-ba!!")


if __name__ == "__main__":

    jon = Musico("Jon")
    guitarra = Instrumento("Guitarra", "cuerdas", 100)
    bateria = Instrumento("Bateria", "Percusión", 250)
    guitarra.tocar()
    piano1 = Piano("Piano X", "Cuerdas-Percusión", 200, 50, jon)
    print(piano1.teclas)
    piano1.tocar()

    trompeta = Trompeta("Trompeta", "Metal", 175, True)

    ego = Musico("Ego")
    # jon = Musico("Jon")
    piano1.musico = ego 
    piano1.tocar()
