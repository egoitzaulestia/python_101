#_____
# listas - tipo de dato
# numeros = [5, 12, 10]

# for n in numeros:
#     print(n)


# datos = ["tenis", 23, 5.234, "Jon"]
# for dato in datos:
#     print(dato)


#_____
# range - tipo de dato, FOR
# a = range(10)
# print(type(a))
# print(a)

# for i in range(10):
#     print(i)
# print()

# for j in range(2, 20):
#     print(j)
# print()

#Loops "for" con salto
# for f in range(10, 100, 5):
#     print(f)

# for i in range(10):
#     print("Ego!")

# for i in range(5):
#     x = input("¿1?")
#     c = input("¿2?")
#     g = input("¿...?")


# Programa para imprimir to nombre 50 veces
# nombre = input("¿Cuál es tu nombre? ")
# for i in range(50):
#     print(f"{i + 1} _ {nombre}")
#     i = i + S1

# Programa para contar
# accion = input("¿Teclear \"up\" para contar en positivo desde cero o teclear \"down\" para contar en negativo? ")

# if accion == "up" or accion == "Up" or accion == "UP":
#     numero_de_veces = int(input("¿Cuántas veces quieres repetir? "))
#     for i in range(numero_de_veces):
#         print(i)
#         i = i + 1
# elif accion == "down" or accion == "Down" or accion == "DOWN":
#     numero_de_veces = int(input("¿Cuántas veces quieres repetir? "))
#     for i in range(numero_de_veces, -1, -1):
#         print(i)
# else:
#     print("ERROR: input incorrecto! Escribe bien la elección")


#_____
#Programa para gestionar los invitados de la fiesta
#Preguntamos al usuario cuanta gente acudirá a la lista
# gente = int(input("Cuánta gente acudirá a la fiesta? "))
# MAX_INVITADOS = 5 #Usamos mayúsculas para las variables constantes
# invitados = [] #Inicializamos una lista
# print()
# if gente > MAX_INVITADOS:
#     print(f"Lo siento, solo {MAX_INVITADOS} personas pueden acudir a la fiesta.")
# elif gente <= MAX_INVITADOS:

# else:
#     print("ERROR. Por favor, reinicie el programa.")
# print()


#preguntar el usuario por el nombre de cada invitado - repetir X veces
#imprimir un mensaje individual para cada invitado

#avanzado - guardad cada nombre en una lista e imprimir un mensaje individual para cada inv

# #LISTAS
# instrumentos = ["guitarra", "PIANO", "ukelele", "piano", "batería"]
# print(instrumentos)
# #loop
# for instrumento in instrumentos:
#     print(instrumento)
# #length
# print(len(instrumentos))
# print(f"numero de lementos: {len(instrumentos)}")

# #count() cuidado- nos dice cuantos mismo elementos hay 
# print(instrumentos.count("piano"))

# #acceso
# print(instrumentos[0])
# print(instrumentos[-1])
# print(instrumentos[:3])

# #modificar
# instrumentos[3] = "PIANO" #Accedemos a la lista y cambiamos

# #añadir
# #añadimos a una lista
# instrumentos.append("TAMBOR")
# #añadimos a una lista en una posición concreta
# instrumentos.insert(2, "Trompeta")
# print(instrumentos)
# #borramos 
# instrumentos.remove("PIANO")
# print(instrumentos)
# #quitamos el último
# instrumentos.pop() 

# #Ordenar
# for instrumento in instrumentos:
#     instrumento.lower()
# instrumentos.sort()
# instrumentos.sort(reverse = True)
# print(instrumentos)

# #tuple /// Utilizamos los TUPLES para "listas que no cambiarán"
# #los déas de la semana, los meses del año... numca cambian
# #Es como una "lista CONSTANTE"
# dias = ("Lunes", "Martes", "...") 


# #LISTAS y TUPLES
# #Actividades básicas

# #Crear una "lista" para gestionar tu compra.
compras = ["plátanos", "manzanas", "leche"]

compras.append("galletas")
compras.append("zumo")
print("Lista de la compra:")
for producto in compras:
    print(f"{producto}")
print(compras[1:3])
print(compras[-2:])
compras[4] = "zumo de naranja"
compras.pop()
compras.insert(2, "limones")
compras.sort()
print("Lista de la compra ordenada alfabéticamente:")
for producto in compras:
    print(f"{producto}")


#Crear un tuple controlar las estaciones del año.
# seasons = ("Spring", "Summer", "Fall", "Winter")
# print(seasons[1])
# for season in seasons:
#     print(season)


#Actividades avanzadas

#la clase tiene los siguientes alumnos:
# names = ["Arturo", "Julio", "Dani"]
# num_alumni = []
# for name in names:
#     answer = input(f"¿Ha venido {name} a clase? (y, n) ")
#     if answer == "y" or answer == "Y":
#         num_alumni.append(name)
# print(f"{len(num_alumni)} alumno(s) están presente hoy")
# if len(num_alumni) > 0:
#     for alumni in num_alumni:
#         print(f"{alumni} ha venido a clase.")


#Calcular la nota media del alumno
notas = [6, 4, 1, 10, 10, 7, 4]
notas.sort()
print(notas)
for i in notas:
    suma =+ i
    media = suma
print(suma)
print(media)
print(f"La nota media de clase es {media}")
print(f"La nota máxima de clase es {notas[-1]}")
print(f"La nota mínima de clase es {notas[0]}")

#list comprehension
