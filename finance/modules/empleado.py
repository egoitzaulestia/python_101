# Clase Empleado
class Empleado:
    def __init__(self, nombre, apellido, exp, pais, ciudad): # Constructor con los distintos atributos de la clase Empleado
        # Iniciamos los atributos de la clase Empleado:
        self.nombre     = nombre    # Nombre
        self.apellido   = apellido  # Apellido
        self.exp        = exp       # Años de experiencia del empleado
        self.pais       = pais      # País
        self.ciudad     = ciudad    # Ciudad
        self.role       = " "      # Role en la start-up
        self._salario   = 2000      # Sueldo base de un empleado mediante la variable protegida _salario (accesible por distintas clases)
        
        # Creamos un sistema para identificar el tiempo de experiencia de trabajo de cada empleado
        # para que así cobre de acuerdo a lo que se le debe.
        if self.exp < 2: # ——————————————————— Empleado JUNIOR cobrara + 100€
            self._salario += 100
        elif self.exp >= 2 and self.exp < 6: # Empleado SEMI-SENIOR: cobrará + 600€
            self._salario += 600 
        elif self.exp >= 6: #————————————————— Empleado SENIOR cobrará + 1000€
            self._salario += 1000

    # Método para calcular el salario
    def calcular_salario(self): 
        return self._salario

    # método para devolver el salario
    def get_salario(self): 
        return self._salario
