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
        print(f"{self.nombre}, es un perro de la raza {self.raza} y mide {self.altura} metros.")

# Este es el programa principal
if __name__ == "__main__":

    # miles = Perro("Miles", "Jack Russell Terrier", 0.55)
    # buddy = Perro("Buddy", "Dachshund", 0.7)
    # ozzy  = Perro("Ozzy", "French Bulldog", 0.4)
    # dax   = Perro("Dax", "Spanish Mastiff", 1.35)

    # perros = [miles, buddy, ozzy, dax]

    # for perro in perros:
    #     # print(f"{perro.nombre} es un perro de la raza {perro.raza} y mide {perro.altura}")
    #     perro.presentar()

    # print(f"{perros[0].nombre} es un perro de la raza {perros[0].raza} y mide {perros[0].altura}")

    perros = []
    contador = 0

    archivado = input("¿Quieres crear la ficha de un perro nuevo? (Y/N)")
    
    while archivado.upper() == "Y":

        nombre = input("Nombre del perro: ")
        raza = input("Raza del perro: ")
        altura = input("Altura del perro: ")
    
        perro = Perro(nombre, raza, altura)

        perros.append(perro)

        archivado = input("¿Quieres crear la ficha de un perro nuevo? (Y/N)")
        if archivado.upper() == "Y":
            continue
        else:
            break
    contador += 1
    
    for perro in perros:
        perro.presentar()
