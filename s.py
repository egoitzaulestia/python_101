# s = "    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  "

# # lstrip() para quitar los espacios de la izquierda
# # rstrip() para quitar los expacios de la dereche
# s = s.strip() 
# a = s.split(",") # El split nos crea una lista
# print("X" + s + "X")
# print(a)
# print(type(a))
# print(type(a[0]))

# # b = []
# # for i in a:
# #     if not i.isnumeric():
# #         b.append(i)
    
# # LIST COMPREHENSION = Crear una nueva lista de una lista previa
# b = [str(i) for i in a if not i.isnumeric()]
# print(b)
# texto_final = ""
# for i in b:
#     texto_final = texto_final + i + " "
# texto_final = " ".join(str(i) for i in b)
# print(texto_final)
# print(texto_final.upper())
# print(texto_final.lower())
# print(texto_final.capitalize())


# i = "3"
# print(i.isnumeric())

# # for char in a:
# #     if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
# #         char = int(char)
# #         b.append(char) 


# l = "    Palabra     "
# o = "    Palabra"
# p = "hola|mundo|como|estas"

# l = l.strip()
# print(l)
# print(type(l))

# o = o.lstrip()
# print(o)
# print(type(o))

# p = p.split("|")
# print(p)
# print(type(p))
# final_text = ""
# for i in p:
#     texto_final = texto_final + i + " "
# final_text = " ".join(i for i in p)
# print(final_text)
# print(final_text.upper())
# print(final_text.lower())
# print(final_text.capitalize())
# y = []
# camelCase = [i.capitalize() for i in p]
# # for i in p:
# #     y.append(i.capitalize())
# # print(y)

# camelCase = " ".join(str(i) for i in camelCase)

# # for i in y:
# #     camelCase = camelCase + i + " "
# # print(camelCase)
# print(camelCase)


# texto ="programazio gustatzen zait"

# print(len(texto))
# print(texto.capitalize())
# print(texto.upper())

# t = "###hola###"
# t = t.strip("#")
# print("X" + t + "X") 

# u = "Hola a todos todos todos"
# u = u.replace("todos", "TODOS")
# print(u)



### ACTIVIDADES ###
# Usando replace() corregir el sigueite texto
# "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
# texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
# texto = texto.replace("Pitón", "Python")
# texto = texto.replace("Bill Gates", "Guido van Rossum")
# texto = texto.replace("1960", "1989")
# texto = texto.replace("es difícil", "es muy fácil")
# print(texto)

# # Usando este texto, llevar a cabo:
# texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "

# # Usar swapcase, replace, upper, in, count, find, strip
# print(texto[5])

# # Contar las veces que la palabra Python aparece en el texto...y si a veces aparece en el texto con mayusculas y minusculas - Python, python
# print("Python: ", texto.upper().count("PYTHON"))
# print("python: ", texto.count("python"))

# # Encontrar la ubicación (numero/indice de carácter) donde esta la primera ocurrencia de la palabra Python. ¿Y la segunda?
# print(texto.find("P"))

# # ¿La palabra 'código' está en el texto? Usar if ... in ...:
# # c_text = [word for word in texto if "código" in texto]
# # print(c_text)

# if "código" in texto:
#     print("La palabra \"código\" está en el texto")
#     print(f"Puedes hallarlo en la posición ", {texto.find("código")})

# # ¿La palabra 'código' está en el texto? Usar if ... in ...:
# n_text = texto.replace("python", "Python")
# n_text = n_text.replace("Python", "PYTHON")
# print(n_text)
# n_text = n_text.upper()
# print(n_text)

# # Quitar los espacios al inicio/final
# n_text = texto.strip()
# print(n_text)

# # Cambiar la letra de todo el texto a "lO MÁS IMPORTANTE QUE NOS HA MANTENIDO EN pYTHON... " - no usar replace
# n_text = n_text.swapcase()



# GESTIÓN DE LOS CORREOS ELECTRÓNICOS
# Generar un informe con:
# - los nombres de los usuarios
# - los dominios únicos (sin repetir el dominio)

emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]

names = []
domines = []

# for email in emails:
#     name = email.split("@") 
#     names.append(name[0])
# print(names)

## names = " ".join(name.replace(".", " ") for name in names) NO ESTA BIEN

# for email in emails: 
#     domine = email.split("@")
#     if domine not in domines:
#         domines.append(domine)
# print(domines)
# print(domines.count("microsoft.es"))

for email in emails:
    name, domine = email.split("@")
    names.append(name)
    print(name)
    if domine not in domines:
        domines.append(domine)
print(domines)



# names = [email.split("@") for email in emails]
# names = [names.append(name[0]) for name in names]
# print(names)

# for n in name:
#     names.append(n[0])
# names = [names.append(n[0]) for n in name]
# print(names)





### EJERCICIO DE MAILING ###
#separa los nombres de los dominios
# emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
# nombres=""
# dominios=""
# for email in emails:
#     nombre,dominio=email.split("@")
#     if "." in nombre:
#         aux1=nombre.split(".")
#         nombre_completo=" ".join(i for i in aux1)
#     else:
#         nombre_completo=nombre
#     nombres=nombres+ "," + nombre_completo
#     if dominio not in dominios:
#        dominios=dominios + "," + dominio
# print(nombres)
# print(dominios)

# ### EJERCICIO DE MAILING ###
# #devuelve un texto con nuevos correos
# nombres = ("maria", "jon", "david")
# texto=",".join(nombre+"@nazaret.eus" for nombre in nombres)
# print(texto) 
