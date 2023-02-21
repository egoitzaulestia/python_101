s = "    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  "

# lstrip() para quitar los espacios de la izquierda
# rstrip() para quitar los expacios de la dereche
s = s.strip() 
a = s.split(",") # El split nos crea una lista
print("X" + s + "X")
print(a)
print(type(a))
print(type(a[0]))

# b = []
# for i in a:
#     if not i.isnumeric():
#         b.append(i)
    
# LIST COMPREHENSION = Crear una nueva lista de una lista previa
b = [str(i) for i in a if not i.isnumeric()]
print(b)
texto_final = ""
for i in b:
    texto_final = texto_final + i + " "
texto_final = " ".join(str(i) for i in b)
print(texto_final)
print(texto_final.upper())
print(texto_final.lower())
print(texto_final.capitalize())

i = "3"
print(i.isnumeric())

# for char in a:
#     if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
#         char = int(char)
#         b.append(char) 


l = "    Palabra     "
o = "    Palabra"
p = "hola|mundo|como|estas"

l = l.strip()
print(l)
print(type(l))

o = o.lstrip()
print(o)
print(type(o))

p = p.split("|")
print(p)
print(type(p))
final_text = ""
for i in p:
    texto_final = texto_final + i + " "
final_text = " ".join(i for i in p)
print(final_text)
print(final_text.upper())
print(final_text.lower())
print(final_text.capitalize())
y = []
camelCase = [i.capitalize() for i in p]
# for i in p:
#     y.append(i.capitalize())
# print(y)

camelCase = " ".join(str(i) for i in camelCase)

# for i in y:
#     camelCase = camelCase + i + " "
# print(camelCase)
print(camelCase)
