class Empleado:
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        self.nombre     = nombre
        self.apellido   = apellido
        self.exp        = exp
        self.pais       = pais
        self.ciudad     = ciudad
        self._salario  = 2000
        if self.exp >= 2:
            self._salario += 200
        elif self.exp >= 5:
            self._salario += 500
        elif self.exp >= 10:
            self._salario += 1000
        # self.__sueldo = self._salario # A revisar

    def calcular_salario(self):
        return self._salario

    def get_salario(self):
        return self._salario

    
class Programador(Empleado):
    def __init__(self, nombre, apellido, exp, pais, ciudad, lenguaje_de_programacion):
        super().__init__(nombre, apellido, exp, pais, ciudad)
        self.lenguaje_de_programacion = lenguaje_de_programacion
        self.__salario_bonus = 0
        if self.lenguaje_de_programacion == "HTML":
            self.__salario_bonus += 100
        elif self.lenguaje_de_programacion == "Python":
            self.__salario_bonus += 400
        elif self.lenguaje_de_programacion == "Java":
            self.__salario_bonus += 850
        elif self.lenguaje_de_programacion == "Assembbly":
            self.__salario_bonus += 1300
        self.__sueldo = self.__salario_bonus
    
    def calcular_salario(self):
        return self.__salario_bonus + self._salario

    def __info(self):
        pass
        print(f"Nombre: {self.nombre}; Apellido: {self.apellido}; Exp: {self.exp}; Pais: {self.pais}; Ciudad: {self.ciudad}; Lenguaje de Progrmación: {self.lenguaje_de_programacion}")

    def get_info(self):
        return self.__info()

    def get_salario(self):
        print(f"Sueldo: {self.__sueldo}")

class Sistema_Nominas:
    # parámetro - una lista de clase Empleado
    def calcular_nominas(self, empleados):
        print("Calculando nominas")
        print("==================")
        for empleado in empleados:
            print(f"Nomina para : {empleado.nombre} - {empleado.lenguaje_de_programacion}")
            print(f"- $ : {empleado.calcular_salario()}")

