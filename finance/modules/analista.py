# Importamos todo de la clase Empleado
from modules.empleado import *

# Clase Analista de datos
class Analista(Empleado):
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        super().__init__(nombre, apellido, exp, pais, ciudad)
        self.role = "Analista de Datos"
        self._salario += 2100

    # Método para calcular el salario    
    def calcular_salario(self):
        return self._salario

    # Método para privado que imprime la informción del empleado analista    
    def __info(self):
        print(f"\n------------------------------------\nInforamación de la persona empleada:\n------------------------------------")
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nExp: {self.exp} años\nPais: {self.pais}\nCiudad: {self.ciudad}\nPuesto: {self.role}\nSalario: {self._salario}\n")

    # Métdo para devolver la información del empleado analista
    def get_info(self):
        return self.__info()
