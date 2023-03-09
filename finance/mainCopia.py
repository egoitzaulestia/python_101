class Empleado:
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.exp = exp
        self.pais = pais
        self.ciudad = ciudad
        self.__salario = 2000
        if self.exp >= 2:
            self.__salario += 200
        if self.exp >= 5:
            self.__salario += 500
        if self.exp >= 10:
            self.__salario += 1000
        self.__sueldo = self.__salario

    def calcular_salario(self):
        return self.__sueldo

    def get_salario(self):
        return self.__sueldo

    
class Programador(Empleado):
    def __init__(self, nombre, apellido, exp, pais, ciudad, lenguaje_de_programacion):
        super().__init__(nombre, apellido, exp, pais, ciudad)
        self.lenguaje_de_programacion = lenguaje_de_programacion
        self.__salario_bonus = self.__salario
        if self.lenguaje_de_programacion == "HTML":
            self.__salario_bonus += 100
        if self.lenguaje_de_programacion == "Python":
            self.__salario_bonus += 400
        if self.lenguaje_de_programacion == "Java":
            self.__salario_bonus += 850
        if self.lenguaje_de_programacion == "Assembly":
            self.__salario_bonus += 1300
    
    def calcular_salario(self):
        return self.__salario_bonus + self.__salario

    def __info(self):
        pass
        print(f"Nombre: {self.nombre}; Apellido: {self.apellido}; Exp: {self.exp}; Pais: {self.pais}; Ciudad: {self.ciudad}; Lenguaje de Programación: {self.lenguaje_de_programacion}")

    def get_info(self):
        return self.__info()

    def get_salario(self):
        print(f"Sueldo: {self.calcular_salario()}")


class Sistema_Nominas:
    def calcular_nominas(self, empleados):
        print("Calculando nominas")
        print("==================")
        for empleado in empleados:
            print(f"Nomina para : {empleado.nombre} - {empleado.lenguaje_de_programacion}")
            print(f"- $ : {empleado.calcular_salario()}")

if __name__ == "__main__":
    
    empleados = []
    
    nominas = Sistema_Nominas()
    nominas.calcular_nominas(empleados)
    print()
    
    elliot = Programador("Elliot", "Alderson", 5, "EEUU", "NYC", "Python")
    naira = Programador("Naira", "Guirado", 0, "E
