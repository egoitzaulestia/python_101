# Clase perro
class Perro:
    def __init__(self, nombre, raza, altura):
        self.nombre = nombre
        self.raza   = raza
        self.altura = altura
    
    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def ladrar(self):
        print(f"{self.nombre} dice: \"GUAU!-GUAU!\"")

    def presentar(self):
        print(f"{self.nombre} mide {self.altura} y su raza es {self.raza}")

# Este es el programa principal
if __name__ == "__main__":

    perros = []
    
    # archivado = input("¿Quieres crear la ficha de un perro nuevo? (Y/N)")
    
    # while archivado != "n":
    #     nombre = input("Nombre de el perro: ")
    #     raza = input("Raza del perro: ")
    #     altura = input("Altura del perro: ")
    
    #     perro = Perro(nombre, raza, altura)

    #     perros.append(perro)

    miles = Perro("Miles", "Jack Russell Terrier", 1.2)
    buddy = Perro("Buddy", "Dachshund", 0.3)
    jack = Perro("Jack", "Bulldog", 0.45)
    jim = Perro("Jim", "Buldog", 0.3)

    for perro in perros:
        print(perro.nombre)
