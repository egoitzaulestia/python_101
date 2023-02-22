nombres = ["Jon", "Maria", "Juan", "Javier"]
nueva_lista = [nombre for nombre in nombres if nombre[0] == "J"]

nueva_lista = []
for nombre in nombres:
    if nombre[0] == "J":
        nueva_lista.append(nombre)

numeros = [3, 54, -12, 4, -64, 99, -120]
# Usando una compresión de lista,
# crear una nueva lista llamada
# "lista positiva" fuera de la lista
# "numeros", que contenga solo los números positivos
# de la lista

lista_positiva = [pos_num for pos_num in numeros if pos_num >= 0] # elegimos los números positivos
print(lista_positiva)
lista_positiva = [pos_num * 2 for pos_num in numeros if pos_num >= 0] # elegimos numeros positivos y los mutiplicamos
print(lista_positiva)
lista_positiva = [pos_num for pos_num in numeros if not pos_num >= 0] 
print(lista_positiva)
lista_negativa = [neg_num for neg_num in numeros if neg_num <= 0]
print(lista_negativa)
