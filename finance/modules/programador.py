# Importamos todo de la clase Empleado
from modules.empleado import *

# Clase Programador  
class Programador(Empleado): # la clase Programador hereda la clase Empleado (lo introducimos como parametro), con sus respectivos atributos y métodos.
    def __init__(self, nombre, apellido, exp, pais, ciudad, lenguaje_de_programacion): # Constructor con los distintos atributos de la clase Programador
        super().__init__(nombre, apellido, exp, pais, ciudad) # Utillizamos super().__init__(bla, bla, bla) para heredar atributos y metedos de la clse Empleado.
        self.role = "Programador/a"                                # Role del empleado: programador
        self.lenguaje_de_programacion = lenguaje_de_programacion   # Lenguje de programación que domina el programador
        self._salario_bonus = 0                                    # Establecemos el salario bonus en 0

        # Creamos un sistema para identificar el tipo de lenguaje de cada empleado
        # para que así cobre de acuerdo a lo que se le debe.
        if self.lenguaje_de_programacion == "HTML":         # Saber HTML cobrará + 100€    
            self.role = self.role + " HTML"
            self._salario_bonus += 100
        elif self.lenguaje_de_programacion == "Python":     # Saber Python cobrará + 400€
            self.role = self.role + " Python"
            self._salario_bonus += 400
        elif self.lenguaje_de_programacion == "Java":       # Saber Java cobrará + 850€
            self.role = self.role + " Java"
            self._salario_bonus += 850
        elif self.lenguaje_de_programacion == "Assembly":   # Saber Assembly cobrará + 1300€
            self.role = self.role + " Assembly"
            self._salario_bonus += 1300

    # Método para calcular el salario    
    def calcular_salario(self):
        return self._salario_bonus + self._salario

    # Método para privado que imprime la informción del empleado programador    
    def __info(self):
        print(f"\n------------------------------------\nInforamación de la persona empleada:\n------------------------------------")
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nExp: {self.exp} años\nPais: {self.pais}\nCiudad: {self.ciudad}\nPuesto: {self.role}\nSalario: {self._salario} $\n")

    # Métdo para devolver la información del empleado programador
    def get_info(self):
        return self.__info()
