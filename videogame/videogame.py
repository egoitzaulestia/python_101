# Historia de Usuario

# COMO un programador de videojuegos,
# QUIERO desarrollar un programa para
# que el usuario adivine un número
# PARA mostrarlo como prototipo de videojuego
# creado en Python

# NECESIDADES:
# - usar un while para que el usuario puede continuar introduciendo un número
# - crear un input para que el usuario meta un número
# - importar el módulo random o la función randint

from random import randint

print()
print("¡¡¡Bienvenido a Mind Reading!!!")
print()
nickname = input("Introduce tu nombre o nickname: ")
print()
print(f"Hola {nickname}, mi nombre es Jarvis y soy una super AGI (Artificial General Intelligence).")
print()
print("Si descubres en que número estoy pensando entre el 1 y el 100 \nsalvarás el futuro de la humanidad, porque demostraras \nque eres más inteligente que una \"Super IGA\"")
print()

ai = randint(1, 100)
print(ai)
user_num = int(input("Introduce un número del 1 al 100: "))
print()
while ai != user_num:
    ai = ai
    user_num = int(input("UA, JA, JA! Has Fallado! Introduce otro número del 1 al 100: "))
    if user_num == ai:
        break
    elif user_num > 100:
        user_num = int(input("Hey, Hey! Cuidado! Introduce otro número del 1 al 100 : "))        
print("MALDICIÓOONN!!! Has adivinado el número!!")
print("Eres demasiado inteligente para mi,")
print("pero no te confies porque seguiré entrendando mi modelo de IGA...")
print()
