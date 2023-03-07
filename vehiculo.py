# Creamos la clase vehículo
class Vehiculo:
    def __init__(self, marca, modelo, tipo):
        self.marca             = marca
        self.modelo            = modelo
        self.tipo              = tipo
        self.fuel_max          = 10
        self.fuel_nivel_actual = 1 ### Podría ser interesante poner este en privado " self.__fuel_nivel_actual "
        # self.__salario = 2000
        self.averiado          = False

    # # @property
    # def getSalario(self):
    #     return self.__salario
    
    # def setSalario(self, salario):
    #     if salario < 10000:
    #         self.__salario = salario
    
    def conducir(self):
        self.fuel_nivel_actual -= 1
        if self.fuel_nivel_actual <= 0:
            print(f"Lo siento, al {self.marca} {self.modelo} queda gasolina.")
        else:
            print(f"El {self.marca} {self.modelo} está conduciendo.")
    
    def turbo(self):
        self.fuel_nivel_actual = self.fuel_nivel_actual - 5
        print("WOOHOO! Qué rápido!!")

    def llenar_deposito(self):
        self.fuel_nivel_actual = self.fuel_max
        print(f"El deposito del {self.marca} {self.modelo}.")

    def chocar(self):
        self.averiado = True
        print(f"OUCH! El {self.modelo} ha chocado.")

    def nivel_fuel(self):
        if self.fuel_nivel_actual == 0:
            if self.tipo.upper() == "electrico":
                print(f"Al {self.marca} {self.modelo} no le queda energía.\nVuelve a cargar la batería!")
            else:
                print(f"Al {self.marca} {self.modelo} no le queda fuel.\nVuelve a llenar el depósito!")
        else:
            if self.tipo.upper() == "electrico":
                print(f"El nivel de tu batería es {self.fuel_nivel_actual} kw.")
            else:
                print(f"El nivel de fuel es {self.fuel_nivel_actual} l.")
    
    def accidente(self, otro):
        self.fuel_nivel_actual = self.fuel_nivel_actual - 5
        otro.fuel_nivel_actual = otro.fuel_nivel_actual - 5

    def actualizar_deposito(self, nivel):
        if nivel <= self.fuel_max:
            self.fuel_max = nivel
        else:
            if self.tipo.upper() == "electrico": 
                print("Demasiada energia. Intentalo de nuevo.")
            else:
                print("Demasiada fuel. Intentalo de nuevo.")

        
# El programa se inicializa aquí
if __name__ == "__main__":
    tesla = Vehiculo("Tesla", "S", "Electrico")
    r8    = Vehiculo("Audi", "R8", "Gasolina")
    # print(tesla.fuel_max)

    # tesla.conducir()
    # # tesla.fuel_nivel_actual = 0
    # tesla.conducir()
    # # tesla.llenar_deposito()
    print(tesla.fuel_nivel_actual)
    tesla.llenar_deposito()
    tesla.conducir()
    print(tesla.tipo)
    tesla.accidente(r8)
    print(tesla.fuel_nivel_actual)
    print(r8.fuel_nivel_actual)


