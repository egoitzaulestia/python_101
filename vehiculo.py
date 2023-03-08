# Creamos la clase vehículo
class Vehiculo:
    def __init__(self, marca, modelo, tipo, ruedas, color, bastidor):
        self.marca              = marca
        self.modelo             = modelo
        self.tipo               = tipo
        self.fuel_max           = 10
        self.fuel_nivel_actual  = 1 ### Podría ser interesante poner este en privado " self.__fuel_nivel_actual "
        # self.__salario = 2000
        self.averiado           = False
        self.ruedas             = ruedas
        self.estado_reudas      = 20
        self.color              = color
        self.__bastidor         = bastidor

    def get_bastidor(self):
        return self.__bastidor
        

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

    def derrapar(self):
        self.estado_reudas -= 5
        print(f"{self.marca} {self.modelo} esta derrapando.")
        if self.estado_reudas < 5:
            print(f"Cuidado! {self.marca} {self.modelo} tiene las ruedas muy gastadas")
    
    def tocar_bocina(self):
        print("PII-PIIII!")

class Camion(Vehiculo):
    def __init__(self, marca, modelo, tipo, ruedas, color, cabina):
        super().__init__(marca, modelo, tipo, ruedas, color)
        self.cabina = cabina

    def dormir(self):
        print("Hora de echar una cabezada.")
    
    def transportar_producto(self):
        print("Hora de echar una cabezada.")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo, ruedas, color, cadena, manillar):
        super().__init__(marca, modelo, tipo, ruedas, color)
        self.cadena = True
        self.manillar = manillar
    
    def caballito(self):
        print(f"{self.marca} {self.modelo} esta haciendo un cabillito.")

    def pinito(self):
        print(f"{self.marca} {self.modelo} esta haciendo un pinito.")


# El programa se inicializa aquí
if __name__ == "__main__":
    tesla = Vehiculo("Tesla", "S", "Electrico", 4, "negro", "987014NME")
    r8    = Vehiculo("Audi", "R8", "Gasolina", 4, "Azul", "978233KSL")
    # print(tesla.fuel_max)

    # tesla.conducir()
    # # tesla.fuel_nivel_actual = 0
    # tesla.conducir()
    # # tesla.llenar_deposito()
    print(tesla.fuel_nivel_actual)
    tesla.llenar_deposito()
    
    for i in range(5):
        tesla.conducir()
    # print(tesla.tipo)
    # tesla.accidente(r8)
    # print(tesla.fuel_nivel_actual)
    # print(r8.fuel_nivel_actual)
    print(tesla.estado_reudas)
    tesla.derrapar()
    print(tesla.estado_reudas)
    # print(tesla.get_bastidor())
    # honda_cbr = Moto()
