import os

# print(os.environ)
# print(os.getlogin())

# print(os.getcwd())

# path = os.getcwd()
# print(os.listdir(path))
# print(type(path))

# os.chdir("../")
# path = os.getcwd()
# print(path)
# print(os.listdir(path))
# print(type(path))


# lastLog = os.getlogin()
# print(lastLog)


######################
# Ejercicios OS module
import platform

print(os.name)
print(platform.uname())

print(os.getcwd())

path = os.path.join(os.getcwd(), "carpeta")
print(path)

print(os.path.split(os.getcwd()))

# Cambiar "abc" para un archivo en tu directorio working
print(os.path.isfile(os.path.join(os.getcwd(), "oSys.py")))

# Cambiar "carpeta"
