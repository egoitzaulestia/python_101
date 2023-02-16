### BIBLIOTECAS ###
#Módulos, librerías, bibliotecas, ...

#help("modules") #Nos da info 
#help("this")

#___Teoría_de_Clase
#import this #Importar una librería
#import os   #Importar una librería

#from this import d,s #Para importar un módulo (o dos) de una librería

#import this as t #Para crear un alias 

#print(d)


#___Ejercicios_de_Clase

#Opción 1
# import this

# #print(this.c)
# #print(this.s)
# print(this.i)
# #print(this.d)

# #Opción 2
# import this as t
# print(t.c)
# print(t.s)

# #Opción 3
# from this import c, s

# print(c)
# print(s)


#Bibliotecas útiles y divertidas

# from urllib.request import urlopen

# page = urlopen("http://info.cern.ch/")
# content = page.read()

# print(content)

import requests #Uses urllib3

# currency = "eur"
# basecurrency = "aud"

# url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"
# resp = requests.get(url)

# print(resp.text)
# print(resp.json())

url = "https://jsonplaceholder.typicode.com/users"
resp = requests.get(url)

print(resp.text)
print(resp.json())


# import uuid
# print ("El UUId uuid1() es : ", end = "")
# print(uuid.uuid1())

# import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# for i in range(4):
#     myTurtle.forward(20)
#     myTurtle.right(90)

# myWin.exitonclick()