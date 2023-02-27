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

path = os.path.join(os.getcwd())
print(path)

print(os.path.split(os.getcwd()))

# Cambiar "abc" para un archivo en tu directorio working
print(os.path.isfile(os.path.join(os.getcwd(), "oSys.py")))

# Cambiar "carpeta" para una carpeta en tu directorio working
print(os.path.isdir(os.path.join(os.getcwd(), "carpeta")))

# cambiar "carpeta" para una carpate en tu directorio working
print(os.path.exists(os.path.join(os.getcwd(), "neuro")))

# print(os.listdir(path))

# os.mkdir("neuro2")
# print(os.listdir(path))
