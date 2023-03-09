from modules.empleado import *
from modules.modules import *
from modules.sistema_nominas import *

if __name__ == "__main__":
    
    empleados = []
    
    # Ejecutar el método para calcular los salarios
    nominas = Sistema_Nominas()
        
     # rellenar la lista de empleados con datos de diferentes tipos de empleados

    elliot = Programador("Elliot", "Alderson", 5, "EEUU", "NYC", "Python")
    # elliot.get_info()
    naira = Programador("Naira", "Guirado", 0, "Euskadi", "Donostia", "Java")
    steve = Programador("Steve", "Wozniak", 8, "EEUU", "San José", "Assembly")
    empleados.append(elliot)
    empleados.append(naira)
    empleados.append(steve)
    nominas.calcular_nominas(empleados)

    print()
    for empleado in empleados:
        empleado.get_salario()
    elliot.get_salario()
    print(elliot.calcular_salario())
    print(naira.calcular_salario())
    print(steve.calcular_salario())

    # empleados.calcular_nominas()
