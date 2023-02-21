# Historia de Usuario

# COMO un programador de videojuegos,
# QUIERO desarrollar un programa para
# que el usuario adivine un número
# PARA mostrarlo como prototipo de videojuego
#creado en Python.

# NECESIDADES:
# - usar un while para que el usuario puede continuar introduciendo un número
# - crear un input para que el usuario meta un número
# - importar el módulo random o la función randint

# Importamos la función randint() del módulo random bult-in de Python
# La función randint(x, y) nos dara un numero integro aleatorio entre 2 parámetro
from random import randint 

# Importamos la función sleep() del módulo time bult-in de Python
# Usaremos la función sleep(x) para dinamizar el rampeo de respuestas impresas en la terminal o cmd 
from time import sleep

print()
print("Loading ...") # El jueho se está "cargando", ;)
sleep(2) # Espera de 2 seg
print()
print("¡¡¡Bienvenido a Mind Reading!!!") # Saludo de Bienvenida
sleep(0.75) # Espera de 0.75 seg
print()
nickname = input("¿Cuál es tu nickname? ") # input para que el/la usuari@ meta su nombre
sleep(1) # Espera de 1 seg
print()
print(f"Hola {nickname}, mi nombre es Jarvis") # Saludo personalizado al/a la jugador/a
sleep(0.25) # Espera de 0.25 seg
print("y soy una IA de última generación.")
sleep(0.75) # Espera de 0.75 seg
print()
print("Si descubres en que número estoy pensando entre el 1 y el 10") # 1.1 Intro del juego
sleep(0.5) # Espera de 0.5 seg
print("salvarás el futuro de la humanidad, porque demostraras") # 1.2 Intro del juego
sleep(0.25) # Espera de 0.25 seg
print("que eres más inteligente que una Super Inteligencia Artificial!!!") # 1.2 Intro del juego
sleep(1) # Espera de 1 seg
print()

ai = randint(1, 10) # El programa genera un número random.
i = 1 # Variable que contiene el contador de intentos.

# print(ai) # print creado para pruebas de testeo. Nos dice el numero random.

# Informamos al usuario que tiene 5 intentos antes de que el programa "piense" en otro número
print("Tienes 5 intentos para adivinar que número tengo en \"mente\", sino, pensaré en otro número") 
user_num = int(input("Introduce un número del 1 al 10: ")) # Le preguntamos al usuario por el númro

# Creamos un loop while. 
# Si el usuari@ no acierta a la primera, elprograma entrara en el loop while.
# El loop while se ejecutará de manera infinita hasta que se den las conciones que hagan que se pare.
# Esas condiciones pueden ser: 
# a) Que el usuario acierte el número que el programa ha creado 
# b) que el juagador decida salir.
while ai != user_num:
    print()
    # A continuación creamos un input para que el/la usuari@ introduzca un nuevo numero mediante un nuevo intento
    user_num = int(input(f"UA-JA-JA-JAA!\nHas Fallado!!!\nLlevas {i} intento/s\nIntroduce otro número del 1 al 10: "))
    # Si el usuario no ha acertado en 5 intentos el programa entra al "if".
    if i == 5:
        print()
        print()
        print("Ti@, eres malísim@!!!!") # Mensaje al usuari@
        print()
        print("Voy a pensar en otro número") # Mensaje al usuari@
        print()
        print("a ver si esta vez aciertas \"más fácil ;)\"") # Mensaje al usuari@
        print("¿Quién dijo que las IAs no eramos irónicas?") # Mensaje al usuari@
        print("BUA-JA-JA-JA-JAAA!") # Mensaje al usuari@
        ai = randint(1, 10) # El programa genera un NUEVO número random.
        # print(ai) # print creado para pruebas de testeo. Nos dice el numero random.
        print()
        # Preguntamos al usuario si quiere seguir jugando "y" o "Y" para seguir, "n" o "N" para para
        user_answer = input("Seguro que quieres seguir juagando? (y, n) ")
        print()
        # Si el/la usuari@ pulsa "y" o "Y", quiere seguir juagando
        if user_answer == "y" or user_answer == "Y": 
            user_num = int(input("Introduce otro número del 1 al 10: ")) # El usuario introduce un nuevo número
            i = 0 # Reincializamos el contador de intentos
            if user_num == ai: # Si el/la usuari@ acierta el numero...
                break # ...salimos del bucle while mediante el break
        # Si el/la usuari@ pulsa "n" o "N" quiere seguir juagando
        elif user_answer == "n" or user_answer == "N":
            print()
            print("I KNEW IT! Soy más inteligente que tú.") # Mensaje al usuari@
            print("Es el fin del a la humanidad, BUU-UH-UH-UA-JA-JA-JAAAAA!!!") # Mensaje al usuari@
            break # ...salimos del bucle while mediante el break
    elif user_num == ai:
        break
    ### elif user_num > 10:
    ###     user_num = int(input("Hey, Hey! Cuidado! Introduce otro número del 1 al 10 : "))        
    i = i + 1 # Hacemos el contador incremente
if user_num == ai: # Si el/la usuari@ acierta el número, GANA la partida y el juego acaba.
    print()
    sleep(0.5) # Espera de 0.5 seg
    print("MALDICIÓOONN!!! Has adivinado el número!!") # Mensaje al usuari@
    sleep(0.25) # Espera de 0.25 seg
    print("Eres demasiado inteligente para mi,") # Mensaje al usuari@
    sleep(0.15) # Espera de 0.15 seg
    print("pero no te confies porque seguiré entrendando mi modelo de IA...") # Mensaje al usuari@
# Mensaje con los creadores del juego
print()
sleep(1.25) # Espera de 1.25 seg
print("Game developed by:")
print()
sleep(0.75) # Espera de 0.75 seg
print("Unai Del Rio") # Nombre del desarrollador del juego 1
sleep(0.3) # Espera de 0.3 seg
print("     &       ")
sleep(0.3) # Espera de 0.3 seg
print("Egoitz Aulestia") # Nombre del desarrollador del juego 2
sleep(0.75) # Espera de 0.75 seg
print()
print()
print("T H E  E N D") # Mensaje de fin del juego
print()
print()
sleep(0.5) # Espera de 0.5 seg
# Fin del programa
