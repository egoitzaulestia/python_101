# Historia de Usuario
"""
COMO un programador de videojuegos,
QUIERO desarrollar un programa para
que el usuario adivine un número
PARA mostrarlo como prototipo de videojuego
creado en Python.
"""

# NECESIDADES:
# - usar un while para que el usuario puede continuar introduciendo un número
# - crear un input para que el usuario meta un número
# - importar el módulo random o la función randint

from random import randint 
import time

print()
print("Loading ...")
#time.sleep(2)
print()
print("¡¡¡Bienvenido a Mind Reading!!!")
#time.sleep(1)
print()
nickname = input("¿Cuál es tu nickname? ")
#time.sleep(1)
print()
print(f"Hola {nickname}, mi nombre es Jarvis y soy una IA de última generación.")
#time.sleep(0.75)
print("Si descubres en que número estoy pensando entre el 1 y el 10")
#time.sleep(0.5)
print("salvarás el futuro de la humanidad, porque demostraras")
#time.sleep(0.25)
print("que eres más inteligente que una Super Inteligencia Artificial!!!")
#time.sleep(1)
print()

ai = randint(1, 10)
i = 0
print(ai)
user_num = int(input("Introduce un número del 1 al 10: "))

while ai != user_num:
    print()
    user_num = int(input("UA-JA-JA! Has Fallado!\nIntroduce otro número del 1 al 10: "))
    if i == 3:
        print()
        print()
        print("Ti@, eres malísim@!!!!")
        print()
        user_answer = input("Seguro que quieres seguir juagando? (y, n) ")
        if user_answer == "y" or user_answer == "Y":
            user_num = int(input("Introduce otro número del 1 al 10: "))
            if user_num == ai:
                break
            # i = 1
            else:
                continue
        elif user_answer == "n" or user_answer == "N":
            break
        continue
    if user_num == ai:
        break
    elif user_num > 100:
        user_num = int(input("Hey, Hey! Cuidado! Introduce otro número del 1 al 10 : "))        
    i = i + 1
if user_num == ai:
    print()
    time.sleep(0.25)
    print("MALDICIÓOONN!!! Has adivinado el número!!")
    time.sleep(1.25)
    print("Eres demasiado inteligente para mi,")
    time.sleep(1.25)
    print("pero no te confies porque seguiré entrendando mi modelo de IA...")
print()
print()
print("T H E  E N D")
print()
print()
time.sleep(2)
print("Game developed by:")
time.sleep(1)
print("Unai Del Rio")
time.sleep(0.3)
print("     &       ")
time.sleep(0.3)
print("Egoitz Aulestia")
print()
time.sleep(0.5)
