#help("keywords")
#help("for")
import keyword
print(keyword.kwlist)
a = keyword.kwlist
print(type(a))


b = 4.345
print(type(a))
print(isinstance(a, float))

sentence = "Hello world"
print(type(sentence))
print(isinstance(sentence, str))

num_entero = 5
print(type(num_entero))
print(isinstance(num_entero, int))

x = 10
#print(hex(id(x)))
print(id(x))
x = 20
print(id(x))
nombres = ["Jon", "Maria"]
print(id(nombres))
nombres.append("Pedro")
print(id(nombres))
print(nombres)

str1 = "PYTHON"
print(id(str1))
str2 = str1
print(id(str2))
del str1

exists = True
if exists == True:
    print("True")
    print("True")
print("FIN")

x = 3
if (x > 1):
    print("mas que uno")

x = 10
y = 4
if (x >= 1):
    print("más que uno")
elif (x < 3) and (y < 3):
    print("klas")
else:
    print("holly shit")

lista = [242, 444, "Ego"]
print(lista)

for i in lista:
    print(i)

s = range(10)
print(s)
print(type(s))
