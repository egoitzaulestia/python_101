"""
# RETO: Sistema para calcular las nóminas.

Acaba de irse de la empresa la programadora que se encargaba del desarrollo del proyecto de nóminas.
Ella ya ha creado una clase Sistema_Nominas, y ha hecho los primeros diseños para las clases de Empleados.
Usando su trabajo ya hecho, termina el programa.

La antigua programadora dejo las siguientes notas escritas a mano:

    - Creo seria conveniente crear clases para: 
      Empledo (atributos: nombre salario; métodos: calcular_salario(salario * 1.1)
      (Hay que desarrollar más el método de cálculo = hablar con analistas)
    - Quizás otros tipos de empleados:
      (Analista, Scrum Master, Product Owner)
"""

### Clase Empleado ###
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

### Clase Programador ###   
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

### Clase Analista de datos ###
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

### Clase Scrum Master ###
class Scrum_Master(Empleado):
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        super().__init__(nombre, apellido, exp, pais, ciudad)
        self.role = "Scrum Master"
        self._salario += 1550

    # Método para calcular el salario    
    def calcular_salario(self):
        return self._salario

    # Método para privado que imprime la informción del empleado scrum master    
    def __info(self):
        print(f"\n------------------------------------\nInforamación de la persona empleada:\n------------------------------------")
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nExp: {self.exp} años\nPais: {self.pais}\nCiudad: {self.ciudad}\nPuesto: {self.role}\nSalario: {self._salario} $\n")

    # Métdo para devolver la información del empleado scrum master
    def get_info(self):
        return self.__info()

### Clase Product Owner ###
class Product_Owner(Empleado):
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        super().__init__(nombre, apellido, exp, pais, ciudad)
        self.role = "Scrum Master"
        self._salario += 1550

    # Método para calcular el salario    
    def calcular_salario(self):
        return self._salario

    # Método para privado que imprime la informción del empleado Product Owner    
    def __info(self):
        print(f"\n------------------------------------\nInforamación de la persona empleada:\n------------------------------------")
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nExp: {self.exp} años\nPais: {self.pais}\nCiudad: {self.ciudad}\nPuesto: {self.role}\nSalario: {self._salario} $\n")

    # Métdo para devolver la información del empleado Product Owner
    def get_info(self):
        return self.__info()

### Calse Sistema_Nominas ###
class Sistema_Nominas:
    # Método calcular nóminas. Le pasamos un parámetro - una lista de de objetos de los distintos tipos de empleados/as
    def calcular_nominas(self, empleados):
        print("\n==================\nCalculando nominas\n==================\n")
        # Bucle for para recorrer la lista "empleados"
        for empleado in empleados:
            print(f"Nomina para : {empleado.nombre} {empleado.apellido} - {empleado.role}")
            print(f"- $ : {empleado.calcular_salario()}")



### Entrada de comienzo del programa ###
if __name__ == "__main__":
    
    # Creamos una empleados vacia
    empleados = []
    

    # Creamos objetos de la clase Programador
    elliot = Programador("Elliot", "Alderson", 5, "US", "NYC", "Python")
    naira = Programador("Naira", "Guirado", 0, "Euskadi", "Donostia", "Java")
    steve = Programador("Steve", "Wozniak", 8, "US", "San José", "Assembly")
    # Creamos objeto de la clase Scrum Master
    ego = Scrum_Master("Egoitz", "Aulestia", 0, "Euskadi", "Donostia")
    # Creamos objeto de la clase Analista
    che = Analista("Abu", "Haldul", 4, "India", "Bangalore")
    # Creamos objeto de la clase Product_Owner
    andrew = Product_Owner("Andrew", "NG", 18, "UK", "London")
        
    # añadimos a la lista de empleados diferentes tipos de empleados
    empleados.append(elliot)
    empleados.append(naira)
    empleados.append(steve)
    empleados.append(ego)
    empleados.append(che)
    empleados.append(andrew)

    # Ceamos objeto de la clase de Sistema Nominas
    nominas = Sistema_Nominas()
      
    # Ejecutamos el método para calcular los salarios
    nominas.calcular_nominas(empleados)

    # Obtenemos información de empleado
    ego.get_info()
    naira.get_info()
