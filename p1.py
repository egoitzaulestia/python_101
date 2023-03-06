# PPO

# # Creamos un objeto persona
# class Persona:
#     nombre = ""
#     edad = 0

# jon = Persona()
# jon.nombre = "Jon"
# jon.edad = 32

# print(jon.edad)
# print(jon.nombre)

# Creamos una clase persona con un constructor
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Estoy vivo")

    def hablar(self):
        print(f"Hola, soy {self.nombre}")

# jon = Persona("Jon", 32)
# print(jon.nombre)
# print(jon.edad)

# maria = Persona("Maria", 43)
power = Persona("Power", 22)
power.hablar()

# jon.edad = 35
# print(jon.edad)

maria = Persona("Maria", 40)
maria.hablar()
print(f"Tengo {maria.edad} años")

personas = []

if __name__ == "__main__":
    nombre = input("Nombre: ")
    edad = input("Edad: ")

    persona = Persona(nombre, edad)
    personas.append(persona)
