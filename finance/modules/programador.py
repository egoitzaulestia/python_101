from empleado import *

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
