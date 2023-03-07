Seguimiento
# Semana 04

---

# Lunes 06.03.2023

## Materia impartido:
- SCRUM - Reunión Retrospectiva del Sprint
- POO = Progamación Orientada a Objetos
  - Las 4 características clave de POO:
    - ABSTRACCIÓN
    - ENCAPSULACIÓN
    - HERENCIA
    - POLIMORFISMO 

## Ejercicios de clase:
### Blocky.games ---> Programación mediante bloques
#### objeto animal (pato, abeja, caracol, gato
    - foto
    - numero de patas
    - más caracteristicas (pico/plumaje, aguijón/miel, caparazón/baba, pelaje/bigote)
### p1.py ---> Creacion de una CLASE con ATRIBUTOS
#### class Persona:
    nombre = nombre
    edad = edad
### p2.py ---> Creación de una CLASE con MÉTODOS y ATRIBUTOS
#### class Perro:
    def __init__(self, nombre, raza, altura): ---> CONSTRUCTOR __init__
      self.nombre = nombre
      self.raza = raza
      self.altura = altura
    def comer(self)
    def dormir(self)
    def ladrar(self)
    def presentar(self) 

---

# Martes 07.02.2023

## Materia impartido:
- POO - Programación Orientada a Objetos
  - Abstracción: Modelar el mundo real en objetos. Hemos modelado un coche.
  - Encapsulación: 
    - Public Member (self.model)
    - Portected Member (self._whatever) 1 "_"
    - Pribate Member (self.__andEver) 2 "_"

## Ejercicios de clase:
### Clase Vehiculo
#### class Vehiculo:
    def __init__(self, marca, modelo, tipo)
      self.marca = marca
      self.modelo = modelo
      self.tipo = tipo
      self.fuel_max = 10 // inicializamos fuel_max con 10
      self.fuel_nivel_actual = 1 // inicializamos con 1
    def conducir(self)
    def llenar_deposito(self)
    def chocar(self)
    def accidente(self, otro)
    
