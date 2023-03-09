class Empleado:
    def __init__(self, nombre, apellido, exp, pais, ciudad):
        self.nombre     = nombre
        self.apellido   = apellido
        self.exp        = exp
        self.pais       = pais
        self.ciudad     = ciudad

    def calcular_salario():
        pass

    
class Programador(Empleado):
    def __init__(self, nombre, apellido, exp, pais, ciudad, lenguaje_de_programacion):
        super().__init__(nombre, apellido, exp, pais, ciudad)
        self.lenguaje_de_programacion = lenguaje_de_programacion
    
    def __info(self):
        pass
        print(f"Nombre: {self.nombre}; Apellido: {self.apellido}; Exp: {self.exp}; Pais: {self.pais}; Ciudad: {self.ciudad}; Lenguaje de Progrmación: {self.lenguaje_de_programacion}")

    def get_info(self):
        return self.__info()

class Sistema_Nominas:

    # parámetro - una lista de clase Empleado
    def calcular_nominas(self, empleados):
        print("Calculando nominas")
        print("==================")
        for empleado in empleados:
            print(f"Nomina para : {empleado.nombre} - {empleado.lenguaje_de_programacion}")
            print(f"- $ : {empleado.calcular_nomina}")





if __name__ == "__main__":
    
    empleados = []
    
    # Ejecutar el método para calcular los salarios
    nominas = Sistema_Nominas()
    nominas.calcular_nominas(empleados)
    print()

    
    # rellenar la lista de empleados con datos de diferentes tipos de empleados

    # Jon, programador de Python
    # Maria, progrmadora de Java
    # Leo, programador de HTML

    elliot = Programador("Elliot", "Alderson", 5, "EEUU", "NYC", "Python")
    # elliot.get_info()
    naira = Programador("Naira", "Guirado", 0, "Euskadi", "Donostia", "Java")
    steve = Programador("Steve", "Wozniak", 8, "EEUU", "San José", "Assembly")
    empleados.append(elliot)
    empleados.append(naira)
    empleados.append(steve)

    for empleado in empleados:
        empleado.get_info()
