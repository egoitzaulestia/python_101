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

# Importamos las clases: Empleado, Programador, Analista, Scrum_Master, Product_Owner, Sistema_Nominas
from modules.empleado import *
from modules.programador import *
from modules.analista import *
from modules.scrum_master import *
from modules.product_owner import *
from modules.sistema_nominas import *


# Entrada principal - Comienzo del programa
if __name__ == "__main__":
    
    # Creamos una lista vacia llamada "empleados"
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
